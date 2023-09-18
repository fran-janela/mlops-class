import sys

def hello_from_docker(event, context):
    return {
        "created_by": "your name",
        "message": "Hello World!",
        "version": sys.version
    }