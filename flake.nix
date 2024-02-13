{
  description = "Application packaged using poetry2nix";
  inputs = {
    # flake-utils.url = "github:numtide/flake-utils";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  };
  outputs = { self, nixpkgs, flake-utils, poetry2nix }:
    # flake-utils.lib.eachDefaultSystem (system:
    let
        system = "x86_64-linux";
        pkgs = nixpkgs.legacyPackages.${system};

    in
        {

          # Call with nix develop
          devShell."${system}" = pkgs.mkShell {
            buildInputs = [ 
              pkgs.python311
              pkgs.python311Packages.pip
              pkgs.python311Packages.virtualenv
              # pkgs.python3Packages.venvShellHook
            ];

            # Define Environment Variables
            TEST_VAR = "test";

            shellHook = ''
            source .venv/bin/activate

            export DJANGO_SETTINGS_MODULE=endoreg_home.settings_prod
            export DJANGO_SECRET_KEY=$(cat .env/secret)
            export KEYCLOAK_CLIENT=$(cat .env/keycloak-client)
            export KEYCLOAK_SECRET=$(cat .env/keycloak-secret)

            # print out the environment variables
            echo "DJANGO_SECRET_KEY: $DJANGO_SECRET_KEY"
            echo "KEYCLOAK_CLIENT: $KEYCLOAK_CLIENT"
            echo "KEYCLOAK_SECRET: $KEYCLOAK_SECRET"
            
            mkdir -p data
            '';

          };

        };
}
