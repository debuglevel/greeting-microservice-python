#!/bin/usr/python3
from flask import Flask
from flask import send_file
from flask import request
from flask import send_from_directory
import sys
import tempfile
import uuid
import os
import shutil
import base64
from flask import Flask
from flask import send_file
from flask import request
from flask import send_from_directory, jsonify, make_response
import sys
import tempfile
import uuid
import os
import shutil
import base64
import uuid
import json
import argparse
import logging
import mysql.connector
import urllib.request
import logging, logging.config, yaml
from pprint import pprint

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logging.config.dictConfig(yaml.load(open("logging-config.yaml", 'r')))


@app.route("/health")
def health():
    print('Received GET request on /health', file=sys.stderr)
    return jsonify(
        {
            "status": "up",
        }
    )


def main():
    logger.info('Starting...')

    sleeptime = int(os.environ['SLEEP_INTERVAL'])

    parser = argparse.ArgumentParser()
    parser.add_argument("--some-host", help="some host", type=str, default="localhost")
    parser.add_argument("--some-port", help="some port", type=int, default=8080)
    args = parser.parse_args()
    # args.some_port
    # args.some_host


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
