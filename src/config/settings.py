from starlette.config import Config

config = Config(".env")

# Project information
TITLE = "Proposal system"
DESCRIPTION = "Project to generate a customer proposal."
VERSION = "1.0.0"

# Uvicorn configuration
ENTRYPOINT = "src.main:app"
HOST = "0.0.0.0"
PORT = 8000
RELOAD = True if config("DEBUG", cast=bool, default=False) is True else False

# Environment
ENV = config("ENV", default=None)
