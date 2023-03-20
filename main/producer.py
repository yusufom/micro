import pika, json

params = pika.URLParameters('amqps://qyjrctbm:XX5LOh47f3hmvqwoPx3ayPbFM0yiHSkZ@beaver.rmq.cloudamqp.com/qyjrctbm')

connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)