{
  description = "Django development environment using devenv";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
    flake-utils.url = "github:numtide/flake-utils";
    devenv.url = "github:cachix/devenv";
  };

  outputs = { self, nixpkgs, flake-utils, devenv, ... }: devenv.lib.mkFlake {
    systems = ["x86_64-linux", "x86_64-darwin"];

    devShells = { system, ... }: let
      pkgs = import nixpkgs {
        inherit system;
        config.allowUnfree = true;
      };
    in {
      default = {
        packages = [
          pkgs.poetry
          pkgs.libGLU pkgs.libGL pkgs.libgcc pkgs.gcc
          pkgs.xorg.libXi pkgs.xorg.libXmu pkgs.freeglut
          pkgs.xorg.libXext pkgs.xorg.libX11 pkgs.xorg.libXv pkgs.xorg.libXrandr
          pkgs.zlib pkgs.ncurses5 pkgs.stdenv.cc pkgs.binutils
          pkgs.python311
          pkgs.python311Packages.pandas
          pkgs.python311Packages.numpy
        ];

        shell = {
          preShell = ''
            mkdir -p data
          '';
          postShell = ''
            export DJANGO_SETTINGS_MODULE=endoreg_home.settings_prod
            export DJANGO_SECRET_KEY=$(cat .env/secret)
            export KEYCLOAK_CLIENT=$(cat .env/keycloak-client)
            export KEYCLOAK_SECRET=$(cat .env/keycloak-secret)
            echo "DJANGO_SECRET_KEY: $DJANGO_SECRET_KEY"
            echo "KEYCLOAK_CLIENT: $KEYCLOAK_CLIENT"
            echo "KEYCLOAK_SECRET: $KEYCLOAK_SECRET"
          '';
          environmentVariables = {
            DJANGO_SETTINGS_MODULE = "endoreg_home.settings_prod";
          };
        };

        python = {
          venvDir = ".venv";
          venvEnabled = true;
        };
      };
    };
  };
}
