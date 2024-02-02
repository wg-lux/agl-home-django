let
  pkgs = import <nixpkgs> {};
  python3Packages = pkgs.python3Packages;
in
python3Packages.buildPythonPackage rec {
  pname = "agl-home-django";
  version = "0.1.0";

  src = ./.;

  format = "pyproject";

  # Include poetry in nativeBuildInputs
  nativeBuildInputs = with python3Packages; [ 
    poetry-core
    setuptools
    wheel
  ];

  propagatedBuildInputs = with python3Packages; [
    numpy
    pandas
    # other dependencies...
  ];

  # Post-installation steps, if any
  # postInstall = ''
  #   # your post-installation commands
  #   pip install poetry
  # '';

  meta = with pkgs.lib; {
    description = "A brief description of your package";
    homepage = "https://yourprojecthomepage.com";
    license = pkgs.lib.licenses.mit;
    maintainers = with pkgs.lib.maintainers; [ pkgs.lib.maintainers.yourname ];
  };
}
