# Secure Communication Over the Net

The goal of this broker application is to facilitate communications for RCON over a HTTP *Secure* connection and then
forward those communications to an RCON application for use. This should allow for:

* Secure Credentials to *not* be sent in clear text
* Reduce the attack surface of RCON by disallowing RCON communications over a WAN 