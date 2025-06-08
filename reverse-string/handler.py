'''
def handle(event, context):
    return {
        "statusCode": 200,
        "body": "Hello from OpenFaaS!"
    }
''' 
def handle(req):
    return req[::-1]

