HTTPS_SERVER_ADDRESS = "127.0.0.1"
HTTPS_SERVER_PORT = 27000

# This should probably just be 'openssl' on *nix systems
OPENSSL_BINARY_LOCATION = r'C:\Program Files\Git\usr\bin\openssl.exe'

OPENSSL_CONFIGURATIONS = {
      'COUNTRY': 'US'
    , 'STATE/PROVINCE': 'MN'
    , 'LOCALITY': 'Woodbury'
    , 'ORGANIZATION': 'SpawningPool.net'
    , 'DEPARTMENT': 'N/A'  # blank will cause errors
    #, 'COMMON NAME': 'spawningpool.net'
    , 'COMMON NAME': '127.0.0.1'
    , 'EMAIL ADDRESS': 'aurorapariseau@gmail.com'
    # , 'ALT DNS ENTRIES': ['localhost']
    # , 'ALT ADDRESSES': ['127.0.0.1']
    , 'ALT ADDRESS': '127.0.0.1'
}

KEY_EXPIRE_DAYS = 365

KEY_OUTPUT_DIR = r"C:\secrets\keys"
KEY_FILE_NAME = "scon_https_server_key.pem"

CERT_OUTPUT_DIR = r"C:\secrets\certs"
CERT_FILE_NAME = "scon_https_server_cert.pem"

RCON_SETTINGS = {
    'TIMEOUT': 2
}

ROUTES_FILE = r"C:\Users\Aurora\Documents\programming\scon\src\routes.json"
