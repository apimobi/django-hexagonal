import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='message')
channel.basic_publish(exchange='message_exchange',
                      routing_key='message.key',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
