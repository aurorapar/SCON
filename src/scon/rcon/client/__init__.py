import json
import socket

from ...settings import ROUTES_FILE
from ...settings import RCON_SETTINGS


class RconClient:

    def __init__(self, server_address, password, *args, **kwargs):

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(RCON_SETTINGS['TIMEOUT'])

        route = self.load_route(server_address)

        self.server_address = route['INTERNAL ADDRESS']
        self.server_port = route['PORT']
        self.server_password = password

    def load_route(self, server_address):
        with open(ROUTES_FILE, 'r') as f:
            data = json.load(f)
        return data[server_address]

    def authenticate(self, game_module):
        auth_message = game_module.generate_auth_message(self.server_password)
        self.socket.connect((self.server_address, self.server_port))
        self.socket.sendall(auth_message)

        try:
            response = self.socket.recv(1024)
            if not response:
                return False
            response = response.decode('ASCII')
            print(response)
            return game_module.validate_authentication(response)
        except TimeoutError:
            print(f'timed out waiting for server {self.server_address}')
            return False

    def send_message(self, command):
        self.socket.sendall(command)
