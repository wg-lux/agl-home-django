{
  description = "Django development environment using devenv";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
    flake-utils.url = "github:numtide/flake-utils";
    devenv.url = "github:cachix/devenv";
  };

  outputs = { self, nixpkgs, flake-utils, devenv, ... }:

  let
    buildInputs = with pkgs; [
      python312Full
      stdenv.cc.cc
    ];

  in {
      packages = with pkgs;  [

      ];
      env = {
        LD_LIBRARY_PATH = "${
        with pkgs;
        lib.makeLibraryPath buildInputs
        }:/run/opengl-driver/lib:/run/opengl-driver-64/lib";
      };
      languages.python = {
        enable = true;
        uv = {
          enable = true;
          sync.enable= true;
        };
      };

      scripts.hello.exec = "${pkgs.uv}/bin/uv" run python helo.py;
      scripts.run-dev-server.exec = 
      "${pkgs.uv}/bin/uv" run python manage.py runserver;
      scripts.run-prod-server.exec =
      "${pkgs.uv}/bin/uv" run gunicorn endoreg_home.asgi:application;
        tasks = {
    "deploy:make-migrations".exec = "${pkgs.uv}/bin/uv run python manage.py makemigrations";
    "deploy:migrate".exec = "${pkgs.uv}/bin/uv run python manage.py migrate";
    "deploy:load-base-db-data".exec = "${pkgs.uv}/bin/uv run python manage.py load_base_db_data";
    
    "dev:runserver".exec = "${pkgs.uv}/bin/uv run python manage.py runserver";
    "prod:runserver".exec = "${pkgs.uv}/bin/uv run daphne devenv_deployment.asgi:application";
  };

  processes = {
    silly-example.exec = "while true; do echo hello && sleep 1; done";
    ping.exec = "ping localhost";
    nvidia.exec = "nvidia-smi -l";
    django.exec = "run-prod-server";
  };

  enterShell = ''
    mkdir -p data
    . .devenv/state/venv/bin/activate
    nvcc -V
    export DJANGO_SETTINGS_MODULE=endoreg_home.settings_prod
    export DJANGO_SECRET_KEY=$(cat .env/secret)
    export KEYCLOAK_CLIENT=$(cat .env/keycloak-client)
    export KEYCLOAK_SECRET=$(cat .env/keycloak-secret)
    echo "DJANGO_SECRET_KEY: $DJANGO_SECRET_KEY"
    echo "KEYCLOAK_CLIENT: $KEYCLOAK_CLIENT"
    echo "KEYCLOAK_SECRET: $KEYCLOAK_SECRET"
  '';
};
}
