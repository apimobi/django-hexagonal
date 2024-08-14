import json
import pika
ROUTING_KEY = 'message.key'
EXCHANGE = 'message_exchange'
QUEUE = 'message'

class MessageListener():
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=QUEUE)
        self.channel.queue_bind(queue=QUEUE, exchange=EXCHANGE, routing_key=ROUTING_KEY)
        

        # self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        # self.channel = self.onnection.channel()
        # self.channel.exchange_declare(exchange=EXCHANGE, exchange_type='direct')
        # result = self.channel.queue_declare(queue='', exclusive=True)
        # queue_name = result.method.queue
        # self.channel.queue_bind(queue=queue_name, exchange=EXCHANGE, routing_key=ROUTING_KEY)
        # # self.channel.basic_qos(prefetch_count=THREADS*10)
        # self.channel.basic_consume(queue=queue_name, on_message_callback=self.callback)
        
    # channel: Channel used for communication
    # method : Message delivery details (if curious, print it to see the result)
    # property: user-defined properties on the message
    # body : contains message
    def callback(self, channel, method, properties, body):
        print(f" [x] Received {body}")
        
    def run(self):
        print ('Message Listener :  Created Listener ')
        self.channel.basic_consume(queue=QUEUE, on_message_callback=self.callback, auto_ack=True)
        self.channel.start_consuming()
    
   