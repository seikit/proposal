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
from src.routers import system_information

app = FastAPI(title=TITLE, description=DESCRIPTION, version=VERSION)

app.include_router(system_information.router)

if __name__ == "__main__":
    uvicorn.run(ENTRYPOINT, host=HOST, port=PORT, reload=RELOAD)
