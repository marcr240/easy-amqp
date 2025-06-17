import pika.channel
from easy_amqp.EasyAMQP import EasyAMQP
from easy_amqp.models import Message
from pika.connection import ConnectionParameters

import pika

credentials = pika.PlainCredentials('test', 'test')
connection_params = ConnectionParameters("localhost", credentials=credentials)

rabbit = EasyAMQP(connection_parameters=connection_params)



@rabbit.declare_queue("test")
@rabbit.listen("test", message_type=str)
@rabbit.batch()
@rabbit.prefetch()
def consume(message: Message, channel: pika.channel.Channel):
    print(message.body)


rabbit.run()