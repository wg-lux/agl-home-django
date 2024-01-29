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
          agl-home-django = mkPoetryApplication { 
            projectDir = ./.;
            python = pkgs.python311;

          }; 

          default = mkPoetryEnv {
            projectDir = ./.;
            python = pkgs.python311;
          };
        };

      devShells.default = self.packages.${system}.pythonEnv;

      });
}
