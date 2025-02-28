import os
import shlex
import subprocess

from ..settings import OPENSSL_BINARY_LOCATION
from ..settings import OPENSSL_CONFIGURATIONS
from ..settings import KEY_EXPIRE_DAYS
from ..settings import KEY_OUTPUT_DIR
from ..settings import KEY_FILE_NAME
from ..settings import CERT_OUTPUT_DIR
from ..settings import CERT_FILE_NAME

KEY_FILE_PATH = os.path.join(KEY_OUTPUT_DIR, KEY_FILE_NAME)
CERT_FILE_PATH = os.path.join(CERT_OUTPUT_DIR, CERT_FILE_NAME)


def generate_secrets():

    for secret_dir in [KEY_OUTPUT_DIR, CERT_OUTPUT_DIR]:
        if not os.path.exists(secret_dir):
            os.makedirs(secret_dir)

    print(f"Generating:\n\t{KEY_FILE_PATH}\n\t{CERT_FILE_PATH}")

    ext = f'-subj "/CN={OPENSSL_CONFIGURATIONS['COMMON NAME']}" -addext ' +\
          f'"subjectAltName=DNS:{OPENSSL_CONFIGURATIONS['COMMON NAME']},DNS:*.{OPENSSL_CONFIGURATIONS['COMMON NAME']}' +\
          f',IP:{OPENSSL_CONFIGURATIONS['ALT ADDRESS']}"'

    commands = [
        f'ecparam -out "{KEY_FILE_PATH}" -name secp521r1 -genkey',
        f'req -new -key "{KEY_FILE_PATH}" -x509 -nodes -days {KEY_EXPIRE_DAYS} out "{CERT_FILE_PATH}" ' + ext
    ]

    parameters = list(map(shlex.split, commands))
    for parameter in parameters:
        subprocess.call([OPENSSL_BINARY_LOCATION] + parameter)

