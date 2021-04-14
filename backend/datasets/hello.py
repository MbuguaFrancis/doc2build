import json

def resp_proxy(code, message):

    msg = {
        code: code,
        message: message
    }

    return {
        "statusCode": code,
        "headers": {
            "Access-Control-Allow-Origin": '*',
            "Content-Type": 'application/json'
        },
        "body": json.dumps(msg)
    }


def lambda_handler(event, context):


    return resp_proxy(200, "Digifarm Agronomy")