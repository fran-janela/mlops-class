import time

def do_something(event, context):
    # Simulate slow processing
    time.sleep(5)
    return {"created_by": "your name", "message": "data was processed"}