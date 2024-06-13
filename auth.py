#!/usr/bin/env python3

import requests
import base64
from io import StringIO
from paramiko import RSAKey


def ssh_sign(private_key: str, message: str) -> str:
    """
    Sign a string message using the private key.

    :param private_key: The SSH RSA private key as a string.
    :param message: The message to sign as a string.
    :return: Base64 encoded signature as a string.
    """
    encoded_message = message.encode()
    sio_private_key = StringIO(private_key)
    priv_k = RSAKey.from_private_key(sio_private_key)
    sio_private_key.close()
    signature_stream = priv_k.sign_ssh_data(encoded_message)
    signature_stream.rewind()
    base64_encoded = base64.b64encode(signature_stream.get_remainder())
    base64_encoded = base64_encoded.decode()
    return base64_encoded


rucio_host = 'https://rucio.srcdev.skao.int'
auth_host = 'https://rucio.srcdev.skao.int'

headers = {
    'X-Rucio-Account': 'axshen'
}

# GET Challenge token
url = f'{auth_host}/auth/ssh_challenge_token'
res = requests.get(url, headers=headers)
ssh_challenge_token = res.headers['X-Rucio-SSH-Challenge-Token']

# GET Auth token
url = f'{auth_host}/auth/ssh'
with open('/Users/she393/Documents/rucio/ssh/id_rsa', 'r') as fd_private_key_path:
    private_key = fd_private_key_path.read()
signature = ssh_sign(private_key, ssh_challenge_token)
headers['X-Rucio-SSH-Signature'] = signature
res = requests.get(url, headers=headers)
print(res.__dict__)