import uvicorn
from fastapi import FastAPI

from src.config.settings import (
    DESCRIPTION,
    ENTRYPOINT,
    HOST,
    PORT,
    RELOAD,
    TITLE,
    VERSION,
)

app = FastAPI(title=TITLE, description=DESCRIPTION, version=VERSION)

if __name__ == "__main__":
    uvicorn.run(ENTRYPOINT, host=HOST, port=PORT, reload=RELOAD)
