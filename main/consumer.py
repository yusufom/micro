import pika, json
from main import Product, db

params = pika.URLParameters('amqps://qyjrctbm:XX5LOh47f3hmvqwoPx3ayPbFM0yiHSkZ@beaver.rmq.cloudamqp.com/qyjrctbm')

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)
    print(properties, data)

    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['images'])
        db.session.add(product)
        db.session.commit()
        print('product_created')

    elif properties.content_type == 'product_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['images']
        db.session.commit()
        print('product_updated')


    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print('product_deleted')




channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)
print('Started Consuming')

channel.start_consuming()
channel.close()

# callback()