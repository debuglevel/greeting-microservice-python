#!/bin/usr/python3
import logging.config
from typing import Optional
from fastapi import FastAPI
from app import health

fastapi = FastAPI()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@fastapi.get("/health")
def get_health():
    logger.debug("Received GET request on /health")
    return health.get_health()

@fastapi.get("/health_async")
async def get_health():
    logger.debug("Received GET request on /health")
    return await health.get_health_async()


@fastapi.get("/")
def read_root():
    return {"Hello": "World"}


@fastapi.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    # def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


# def main():
#     logger.info("Starting...")
#
#     # sleeptime = int(os.environ['SLEEP_INTERVAL'])
#
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--some-host", help="some host", type=str, default="localhost")
#     parser.add_argument("--some-port", help="some port", type=int, default=8080)
#     args = parser.parse_args()
#     # args.some_port
#     # args.some_host
#
#     uvicorn.run(fastapi, host="0.0.0.0", port=8080)
#
#
# # This only runs if the script is called instead of uvicorn; should probably not be used.
# if __name__ == "__main__":
#     main()
