{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    pkgs.poetry
    pkgs.python311Packages.django
    # pkgs.docker
  ];
}