## SSH rucio client access

Testing access to the rucio client using the Python API with SSH keys for retrieving an auth token. Currently doesn't work - here are the steps I've taken to try and make it work

1. Create ssh key and add the public key to the IAM Escape account
2. Install Rucio python Client and try to create a client using ssh with private key. Note the key pair has to be created with RSA due to some error with `paramiko==3.4.0`.

```
client = Client(
    auth_type='ssh',
    creds={
        'ssh_private_key': 'ssh/id_rsa'
    },
    ...
)
```

3. This fails. Can try doing this manually with Python `requests` but it also doesn't work for some reason.

Manual steps:

* GET request to `/auth/challenge_token` with `X-Rucio-SSH-Challenge-Token` header set to account name (OK)
* `__get_token_ssh` function [permalink](https://github.com/rucio/rucio/blob/1443bd55dea181598de833d43ad19c548366411f/lib/rucio/client/baseclient.py#L727)
* `ssh_sign` function for private key + challenge token for signature [link](https://github.com/rucio/rucio/blob/1443bd55dea181598de833d43ad19c548366411f/lib/rucio/common/utils.py#L1292)
* GET request to `/auth/ssh` with signature as `X-Rucio-SSH-Signature` in header (NOT OK)

## Links

* Rucio Python client API: https://rucio.github.io/documentation/client_api/client
* Rucio REST API: https://rucio.github.io/documentation/html/rest_api_doc.html#tag/Account
