def word_count(event, context):
    try:
        received_body = event["body"]
        words = received_body.split(" ")
        count = len(words)
    
        return {
            "received_string": received_body,
            "word_count": count
        }
    except Exception as e:
        print(e)
        return {
            "error": "could not count words",
        }