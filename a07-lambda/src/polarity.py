from textblob import TextBlob
import json

def get_polarity(event, context):
    try:
        received_body = json.loads(event["body"])
        text = received_body["text"]
        blob = TextBlob(text)
        if blob.polarity > 0.2:
            feeling = "positive"
        elif blob.polarity > -0.8:
            feeling = "neutral"
        else:
            feeling = "negative"
    
        return {
            "received_text": text,
            "polarity": str(blob.polarity),
            "feeling": feeling
        }
    except Exception as e:
        print(e)
        return {
            "error": "could not assert polarity",
        }