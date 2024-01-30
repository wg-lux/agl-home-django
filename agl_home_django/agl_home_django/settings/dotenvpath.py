from pathlib import Path

NIX_DEPLOYMENT = True

if NIX_DEPLOYMENT:
    dotenvpath = Path("/home/agl-admin/.config/agl-home-django.env")
else:
    dotenvpath = Path(__file__).resolve().parent / 'agl-home-django.env'
