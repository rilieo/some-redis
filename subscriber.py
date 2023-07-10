import redis

def main() -> None:
    r = redis.Redis(
        host='localhost',
        port=6379,
        decode_responses=True
        )
    
    topics = [
        "info",
        "email",
        "marital_status",
        "relationship",
        "spouse"
    ]

    # creates subscriber model
    sub = r.pubsub()
    sub.subscribe(topics)

    # listens for messages that are in one of subscribed channels
    for message in sub.listen():
        print(message['channel'], end=": ")
        print(message['data'])

if __name__ == "__main__":
    main()