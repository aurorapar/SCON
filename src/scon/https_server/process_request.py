import traceback
from enum import Enum, auto
import importlib.util
import json

from .responses import generate_response
from ..rcon.client import RconClient


class SCONFormat(Enum):
    PASSWORD = auto()
    RCON_STATEMENT = auto()
    GAME = auto()
    SERVER_ADDRESS = auto()


def get_request_content(request_handler):
    content_length = int(request_handler.headers["Content-Length"])
    post_data = request_handler.rfile.read(content_length)
    content = post_data.decode("ASCII")
    return json.loads(content)


def validate_request_format(request_handler, content):
    for scon_key in SCONFormat:
        if scon_key.name not in content.keys():
            generate_response(request_handler, 400)
            return

    match content['RCON_STATEMENT']:

        case list():
            try:
                [int(byte_data, 2) for byte_data in content['RCON_STATEMENT']]
            except Exception as format_exception:
                traceback.print_exception(format_exception)
                generate_response(request_handler, 400)
                return
            pass

        case _:
            print(f"no type matched??? {type(content['RCON_STATEMENT'])}")
            generate_response(request_handler, 400)
            return


def parse_game_module(request_handler, content):
    test_module_name = f"scon.rcon.authentication.{content['GAME']}"
    game_name = importlib.util.find_spec(test_module_name)
    if not game_name:
        generate_response(request_handler, 404)
        return None
    return importlib.import_module(test_module_name)


def process_request(request_handler):
    content = get_request_content(request_handler)

    validate_request_format(request_handler, content)

    game_module = parse_game_module(request_handler, content)
    if not game_module:
        return

    rcon_client = RconClient(content['SERVER_ADDRESS'], content['PASSWORD'])
    if not rcon_client.authenticate(game_module):
        generate_response(request_handler, 403)
        return
    command_message = bytearray([int(byte_data, 2) for byte_data in content['RCON_STATEMENT']])
    rcon_client.send_message(command_message)


    generate_response(request_handler, 200)

