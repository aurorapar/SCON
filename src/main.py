import os
import traceback
from multiprocessing import Process

from scon.https_server import start_https_server

from scon.secrets import generate_secrets
from scon.secrets import KEY_FILE_PATH
from scon.secrets import CERT_FILE_PATH


def main():
    try:
        if not (os.path.exists(KEY_FILE_PATH) and os.path.exists(CERT_FILE_PATH)):
            print("Generating key file and certificate....")
            generate_secrets()
    except Exception as e:
        traceback.print_exception(e)
        exit(0)

    https_server_process = Process(target=start_https_server)
    https_server_process.start()
    while True:
        entry = input("Enter 'stop' or 'exit' exactly to stop the application:\n")
        if entry in ['stop', 'exit']:
            https_server_process.terminate()
            print("Exiting")
            exit(0)

    print("Exited outside of main loop. Unintended behavior")


if __name__ == "__main__":
    main()
