{
  description = "Application packaged using poetry2nix";
  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, flake-utils, poetry2nix }:
    
    flake-utils.lib.eachDefaultSystem (system:
      let
        # see https://github.com/nix-community/poetry2nix/tree/master#api for more functions and examples.
        pkgs = nixpkgs.legacyPackages.${system};
        inherit (poetry2nix.lib.mkPoetry2Nix { inherit pkgs; }) mkPoetryEnv;
        inherit (poetry2nix.lib.mkPoetry2Nix { inherit pkgs; }) mkPoetryApplication ; # or mkPoetryScriptsPackage or mkPoetryApplication

      in
      {
        
        packages = {

          # default = mkPoetryEnv {
          #   projectDir = ./.;
          #   python = pkgs.python311;
          #   extraPackages = (ps: [
          #     ps.opencv4
          #   ]);
          # };

          default = mkPoetryEnv {
            projectDir = ./.;
            python = pkgs.python311;
            extraPackages = (ps: with ps; [
              (opencv4.overrideAttrs (oldAttrs: {
                format = "setuptools";
              }))
            ]);
            overrides = self: super: {
              opencv4 = super.opencv4.overrideAttrs (oldAttrs: {
                propagatedBuildInputs = oldAttrs.propagatedBuildInputs or [] ++ [ /* other dependencies if needed */ ];
              });
            };
          };

        };

      devShells.default = pkgs.mkShell {
          # inputsFrom = [ self.packages.${system}.agl-home-django ];
          packages = [ 
            pkgs.poetry
          ];
        };
      });
}