{ pkgs ? import <nixpkgs> {} }:
pkgs.poetry2nix.mkPoetryApplication {
  projectDir = ./.; # translates to nix packages  
}