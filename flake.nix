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
        pkgs = nixpkgs.legacyPackages.${system};
        inherit (poetry2nix.lib.mkPoetry2Nix { inherit pkgs; }) mkPoetryEnv;

      in
      {
        packages = {
          default = mkPoetryEnv {
            projectDir = ./.;
            python = pkgs.python311;
            extraPackages = ps: with ps; [
              # pkgs.python311Packages.opencv4
            ];
          };
        };

        devShells.default = pkgs.mkShell {
          packages = [ 
            pkgs.poetry
          ];
        };
      }
  );
}
