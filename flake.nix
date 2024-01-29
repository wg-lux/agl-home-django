{
  description = "Application packaged using poetry2nix";
# ../lib/python3.11/site-packages/agl_home_django/manage.py
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

          }; # mkPoetryScriptsPackage or mkPoetryApplication

          # default = self.packages.${system}.agl-home-django;
          default = mkPoetryEnv {
            projectDir = ./.;
            python = pkgs.python311;
          };
        };

        # devShells.default = pkgs.mkShell {
        #   inputsFrom = [ self.packages.${system}.agl-home-django ];
        #   packages = [ pkgs.python pkgs.poetry pkgs.django ];
        # };

      devShells.default = self.packages.${system}.pythonEnv;

      });
}



# ### DOCS
# # mkPoetryApplication

# # Creates a Python application using the Python interpreter specified based on the designated poetry project and lock files. mkPoetryApplication takes an attribute set with the following attributes (attributes without default are mandatory):

# #     projectDir: path to the root of the project.
# #     src: project source (default: cleanPythonSources { src = projectDir; }).
# #     pyproject: path to pyproject.toml (default: projectDir + "/pyproject.toml").
# #     poetrylock: poetry.lock file path (default: projectDir + "/poetry.lock").
# #     overrides: Python overrides to apply (default: defaultPoetryOverrides).
# #     meta: application meta data (default: {}).
# #     python: The Python interpreter to use (default: pkgs.python3).
# #     preferWheels : Use wheels rather than sdist as much as possible (default: false).
# #     groups: Which Poetry 1.2.0+ dependency groups to install (default: [ ]).
# #     checkGroups: Which Poetry 1.2.0+ dependency groups to run unit tests (default: [  "dev" ]).
# #     extras: Which Poetry extras to install (default: [ "*" ], all extras).
