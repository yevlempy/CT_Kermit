import logging
from webui.platforms.utils import read_file_info

logger = logging.getLogger(__name__)

def read_server_info(hostname):
    prefix = '*postgresqlinventory-'
    suffix = '-compact.json'
    logger.info("PostgreSQL Inventory for " + hostname)
    return read_file_info(hostname, prefix, suffix)