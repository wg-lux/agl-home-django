{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  buildInputs = [
    pkgs.python311
    pkgs.poetry
    pkgs.python311Packages.django
    # pkgs.python311Packages.opencv4
  ];
}