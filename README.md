# agl-home-django

## Components
- shell.nix + .envrc -> builds shell environment using nix direnv
- flake.nix -> used with nix build to translate poetry package to nix package using poetry2nix
    - `nix build ./flake.nix`
    - save to specific path: `nix build ./flake.nix -o nix-agl-home-django`
- run with: `nix-agl-home-django/bin/start-server`

## Build Docker Container
'nix build .#dockerImages.x86_64-linux.agl-home-django'

# FAQ
## Run during development (NixOS)
- Use poetry shell ('poetry shell')
