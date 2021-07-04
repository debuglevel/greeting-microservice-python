import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_health():
    logger.debug("Getting health status...")
    return {"status": "up"}


async def get_health_async():
    logger.debug("Getting health status (async)...")
    return {"status": "up"}
