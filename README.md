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

## Troubleshooting
### nix build not working
- check whether poetry.lock and pyproject.toml are in sync, useful commands:
    - poetry lock --no-update
    - poetry lock
    - poetry update

# TODO 
- [ ] (not really necessary since we can just use poetry) Somehow manage production and dev smart. The problem we need to solve: For a working nix dev env of packages we need to import non-nix-packaged modules in our flake postShellHook; for working and testing releases we need to add them in our pyproject.toml file 