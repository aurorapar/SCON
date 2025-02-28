import json


HTTP_RESPONSES = {
    200: {
        'Response': 200
        ,'Header': ('Content-Type', 'application/json')
        ,'Content': {'Received': True}
    },

    400: {
        'Response': 400
        ,'Header': ('Content-Type', 'application/json')
        ,'Content': {'Invalid Request': 'SCON Format Violated'}
    },
    403: {
        'Response': 403
        ,'Header': ('Content-Type', 'application/json')
        ,'Content': {'Forbidden': 'Failed to authenticate'}
    },
    404: {
        'Response': 404
        ,'Header': ('Content-Type', 'application/json')
        ,'Content': {'Not Found': 'Game Not Supported'}
    },
}


def generate_response(request_handler, response_code):
    response = HTTP_RESPONSES[response_code]

    request_handler.send_response(response['Response'])
    request_handler.send_header(*response['Header'])
    request_handler.end_headers()

    match response['Header'][1]:

        case 'application/json':
            request_handler.wfile.write(json.dumps(response['Content']).encode())

        # Currently unused, leaving in just in case
        case 'text/html':
            request_handler.wfile.write(response['Content'].encode())

        case _:
            request_handler.wfile.write('unhandled response'.encode())
