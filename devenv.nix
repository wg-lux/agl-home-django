{ pkgs, lib, config, inputs, ... }:
let
  buildInputs = with pkgs; [
    python312Full
    # cudaPackages.cuda_cudart
    # cudaPackages.cudnn
    stdenv.cc.cc
  ];
in
{
  packages = with pkgs; [
    cudaPackages.cuda_nvcc
  ];

  env = {
    LD_LIBRARY_PATH = "${lib.makeLibraryPath buildInputs}:/run/opengl-driver/lib:/run/opengl-driver-32/lib";
  };

  languages.python = {
    enable = true;
    uv = {
      enable = true;
      sync.enable = true;
    };
  };

  scripts = {
    hello = {
      exec = "${pkgs.uv}/bin/uv run python hello.py";
    };
    run-dev-server = {
      exec = "${pkgs.uv}/bin/uv run python manage.py runserver";
    };
    run-prod-server = {
      exec = "${pkgs.uv}/bin/uv run daphne devenv_deployment.asgi:application";
    };
  };

  tasks = {
    "deploy:make-migrations" = {
      exec = "${pkgs.uv}/bin/uv run python manage.py makemigrations";
    };
    "deploy:migrate" = {
      exec = "${pkgs.uv}/bin/uv run python manage.py migrate";
    };
    "deploy:load-base-db-data" = {
      exec = "${pkgs.uv}/bin/uv run python manage.py load_base_db_data";
    };
    "dev:runserver" = {
      exec = "${pkgs.uv}/bin/uv run python manage.py runserver";
    };
    "prod:runserver" = {
      exec = "${pkgs.uv}/bin/uv run daphne devenv_deployment.asgi:application";
    };
  };

  processes = {
    silly-example = {
      exec = "while true; do echo hello && sleep 1; done";
    };
    ping = {
      exec = "ping localhost";
    };
    nvidia = {
      exec = "nvidia-smi -l";
    };
    django = {
      exec = "run-prod-server";
    };
  };

  hooks = {
    postShell = ''
      mkdir -p data
      export DJANGO_SETTINGS_MODULE=endoreg_home.settings_prod
      export DJANGO_SECRET_KEY=$(cat .env/secret)
      export KEYCLOAK_CLIENT=$(cat .env/keycloak-client)
      export KEYCLOAK_SECRET=$(cat .env/keycloak-secret)
      echo "DJANGO_SECRET_KEY: $DJANGO_SECRET_KEY"
      echo "KEYCLOAK_CLIENT: $KEYCLOAK_CLIENT"
      echo "KEYCLOAK_SECRET: $KEYCLOAK_SECRET"
    '';
  };

  enterShell = ''
    . .devenv/state/venv/bin/activate
    nvcc -V
    hello
  '';
}
