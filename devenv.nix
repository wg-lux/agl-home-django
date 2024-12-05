{
  description = "Application packaged using uv2nix and managed with devenv";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
    flake-utils.url = "github:numtide/flake-utils";
    devenv.url = "github:cachix/devenv";
    uv2nix.url = "github:pyproject-nix/uv2nix";
  };

  outputs = { self, nixpkgs, flake-utils, devenv, uv2nix, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          config.allowUnfree = true;
        };
      in {
        devShells.default = devenv.lib.mkShell {
          inputs = {
            inherit pkgs;
          };
          modules = [
            {
              packages = with pkgs; [
                libGLU libGL libgcc gcc
                xorg.libXi xorg.libXmu freeglut
                xorg.libXext xorg.libX11 xorg.libXv xorg.libXrandr zlib
                ncurses5 stdenv.cc binutils
                python311
                python311Packages.pandas
                python311Packages.numpy
              ];

              environmentVariables = {
                DJANGO_SETTINGS_MODULE = "endoreg_home.settings_prod";
              };

              shell = {
                hooks.postShellHook = ''
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

              languages.python = {
                enable = true;
                uv = {
                  enable = true;
                  sync.enable = true;
                };
              };

              scripts = {
                "run-dev-server" = {
                  exec = "${pkgs.uv}/bin/uv run python manage.py runserver";
                };
                "run-prod-server" = {
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
                django = {
                  exec = "run-prod-server";
                };
              };

              shell = {
                hooks.enterShell = ''
                  . .devenv/state/venv/bin/activate
                  nvcc -V
                '';
              };
            }
          ];
        };
      }
    );
}
