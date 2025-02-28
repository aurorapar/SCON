#
# Oddly, this game doesn't actually use RCON. As far as I can tell, you add the byte data 2 to indicate a command (1
# for auth), and then append your payload ended by a null-byte (\x00).
#

def generate_auth_message(password):
    message = bytearray()

    message.extend((1).to_bytes())
    message.extend(password.encode())
    message.extend(''.encode())
    return message


def validate_authentication(response):
    return 'password accepted' in response.lower()
