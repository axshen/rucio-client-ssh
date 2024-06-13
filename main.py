#!/usr/bin/env python3

import logging
from rucio.client import Client

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')

rucio_host = 'https://rucio.srcdev.skao.int'
auth_host = 'https://rucio.srcdev.skao.int'

client = Client(
    rucio_host=rucio_host,
    auth_host=auth_host,
    account='axshen',
    ca_cert='',
    auth_type='ssh',
    creds={
        'ssh_private_key': '/Users/she393/Documents/rucio/ssh/id_rsa'
    },
    timeout=90000,
    vo='skatelescope.eu',
    logger=logger
)
