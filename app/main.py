#!/bin/usr/python3
import argparse
import logging.config
import yaml
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

# app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logging.config.dictConfig(yaml.load(open("logging-config.yaml", 'r')))


@app.get("/")
# async def read_root():
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    # def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
#
#
# @app.route("/health")
# def health():
#     print('Received GET request on /health', file=sys.stderr)
#     return jsonify(
#         {
#             "status": "up",
#         }
#     )

#
# def main():
#     logger.info('Starting...')
#
#     sleeptime = int(os.environ['SLEEP_INTERVAL'])
#
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--some-host", help="some host", type=str, default="localhost")
#     parser.add_argument("--some-port", help="some port", type=int, default=8080)
#     args = parser.parse_args()
#     # args.some_port
#     # args.some_host
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     main()
