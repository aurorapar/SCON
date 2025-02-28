# Secure Communication Over the Net

The goal of this broker application is to facilitate communications for RCON over a HTTP *Secure* connection and then
forward those communications to an RCON application for use. This should allow for:

* Secure Credentials to *not* be sent in clear text
* Reduce the attack surface of RCON by disallowing RCON communications over a WAN

An example exists at `src/scon_client/__init__.py`. For use, the client needs to send the following payload in a JSON 
payload.

```commandline
data = {
    'PASSWORD': 'passwordtest',
    'RCON_STATEMENT': None,
    'GAME': 'theisle',
    'SERVER_ADDRESS': '70.59.116.217'
}
```

The server address is the address of the game server to connect to for RCON which is typically always exposed on the
WAN. A 'routes.json' file found at the root of this application routes the binary RCON command data from `RCON_STATEMENT`
forwarding that to the route set in the routes file.

```commandline
{
    "70.59.116.217": {
        "INTERNAL ADDRESS": "192.168.1.142",
        "PORT": 8888
    }
}
```