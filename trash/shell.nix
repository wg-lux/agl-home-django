
{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  buildInputs = [
    pkgs.python311
    pkgs.python311Packages.poetry-core
    pkgs.python311Packages.django
    # pkgs.python311Packages.opencv4
  ];
}