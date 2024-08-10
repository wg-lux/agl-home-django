{
  description = "Application packaged using poetry2nix";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";

  };

  outputs = { self, nixpkgs, poetry2nix, ... }:
    let
        system = "x86_64-linux";
        pkgs = import nixpkgs {
          inherit system;
          config.allowUnfree = true;
        };
        
    in
        {
          # Call with nix develop
          devShell."${system}" = pkgs.mkShell {
            buildInputs = with pkgs; [ 
              poetry
              
              libGLU libGL libgcc gcc
              xorg.libXi xorg.libXmu freeglut
              xorg.libXext xorg.libX11 xorg.libXv xorg.libXrandr zlib 
              ncurses5 stdenv.cc binutils

              python311
              python311Packages.pandas
              python311Packages.numpy

              # Make venv (not very nixy but easy workaround to use current non-nix-packaged python module)
              python3Packages.venvShellHook
            ];

            # Define Environment Variables
            DJANGO_SETTINGS_MODULE="endoreg_home.settings_prod";
            


            # Define Python venv
            venvDir = ".venv";
            postShellHook = ''
              # source .venv/bin/activate
              mkdir -p data
              
              export DJANGO_SETTINGS_MODULE=endoreg_home.settings_prod
              export DJANGO_SECRET_KEY=$(cat .env/secret)
              export KEYCLOAK_CLIENT=$(cat .env/keycloak-client)
              export KEYCLOAK_SECRET=$(cat .env/keycloak-secret)

              # print out the environment variables
              echo "DJANGO_SECRET_KEY: $DJANGO_SECRET_KEY"
              echo "KEYCLOAK_CLIENT: $KEYCLOAK_CLIENT"
              echo "KEYCLOAK_SECRET: $KEYCLOAK_SECRET"

              
            '';
          };


        # });
        };
}
