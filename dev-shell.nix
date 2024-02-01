with import <nixpkgs> {};

# use like: nix-shell dev-shell.nix -A py311

let 
  makeShell = python: (mkShell {
    name = "endo-reg-db-dev-env";
    buildInputs = with python3Packages; [
      poetry-core
      numpy
      pandas
      django
      # pytest

      # if packages are not available for nix
      venvShellHook
    ];

    # Required for venvShellHook
    venvDir = ".venv${python.version}";
    postShellHook = ''
      pip install endo-reg-db
    '';
  }
);

in
  {
    py39 = makeShell python39; #doesnt need pkgs prefix due to how we import nixpgs as top level
    py310 = makeShell python310;
    py311 = makeShell python311;
  }