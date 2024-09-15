#!/usr/bin/env python

import pika, sys, os

host = os.environ.get('AMQP_HOST')
port = os.environ.get('AMQP_PORT')
queue = os.environ.get('QUEUE_NAME')

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port))
    channel = connection.channel()

    channel.queue_declare(queue=queue)

    def on_message_callback(ch, method, properties, body):
        print(f"Received: {body}")

    channel.basic_consume(queue=queue, on_message_callback=on_message_callback, auto_ack=True)

    print("Waiting for messages...")

    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)