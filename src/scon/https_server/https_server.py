import http.server
import ssl
from threading import Thread

from .process_request import process_request
from ..settings import HTTPS_SERVER_PORT
from ..settings import HTTPS_SERVER_ADDRESS
from ..secrets import KEY_FILE_PATH
from ..secrets import CERT_FILE_PATH


def get_ssl_context(certfile, keyfile):
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(certfile, keyfile)
    context.set_ciphers("@SECLEVEL=1:ALL")
    return context


class MyHandler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
        process_request(self)


def start_https_server():
    server_address = (HTTPS_SERVER_ADDRESS, HTTPS_SERVER_PORT)
    httpd = http.server.HTTPServer(server_address, MyHandler)

    context = get_ssl_context(CERT_FILE_PATH, KEY_FILE_PATH)
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    httpd.serve_forever()
