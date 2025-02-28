import requests

host = 'https://127.0.0.1:27000'  # where SCON server is hosted

data = {
    'PASSWORD': 'passwordtest',
    'RCON_STATEMENT': None,
    'GAME': 'theisle',
    'SERVER_ADDRESS': '70.59.116.217'
}
cert_file = 'C:\\secrets\\certs\\scon_https_server_cert.pem'


def generate_auth_message(password):
    message = bytearray()

    datas = [(1).to_bytes(4), password.encode(), ''.encode()]
    for byte_data in datas:
        message.extend(byte_data)

    return message


def main():
    data['RCON_STATEMENT'] = [bin(byte_data) for byte_data in generate_auth_message('test')]
    req = requests.post(host, json=data, verify=cert_file)
    print(req.status_code)
    print(req.text)


if __name__ == "__main__":
    main()
