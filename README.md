# EasyAMQP

---

EasyAMQP is a Python library built on top of `pika` that simplifies interacting with RabbitMQ. It provides a decorator-based approach for declaring queues, exchanges, bindings, and setting up message listeners, aiming to reduce boilerplate code and improve readability.

## Features

* **Simplified Connection Management**: Handles connections and reconnections to RabbitMQ.
* **Decorator-based Topology Definition**: Easily declare queues, exchanges, and bindings using decorators.
* **Listener Management**: Define message consumers with automatic message parsing and acknowledgment.
* **Batch Consumption**: Support for processing messages in batches.
* **Dead Letter Queues**: Configure dead-lettering for queues directly.
* **Prefetch Control**: Set QoS prefetch settings for consumers.
* **Flexible Deployment**: Run your AMQP operations in a separate thread or in the main thread.

---

## Installation

```bash
pip install easyamqp # (Assuming this will be the package name)
```

## Usage

### Basic consuming

```python
import pika
from easyamqp import EasyAMQP

# Single connection parameter
amqp = EasyAMQP(pika.ConnectionParameters('localhost'))

@amqp.listen(queue='my_queue', message_type=MyMessage, auto_ack=True)
def process_message(message: MyMessage):
    print(f"Received message: {message.value} with ID {message.id}")


```

### Basic Setup and Connection

To get started, instantiate EasyAMQP with your RabbitMQ connection parameters.

```python
import pika
from easyamqp import EasyAMQP

# Single connection parameter
amqp = EasyAMQP(pika.ConnectionParameters('localhost'))



# or use multiple connection parameters for high availability
amqp_ha = EasyAMQP([
    pika.ConnectionParameters('rabbitmq1'),
    pika.ConnectionParameters('rabbitmq2'),
])

# use retry mechanism in case of connection errors
amqp_robust = EasyAMQP(
    pika.ConnectionParameters('localhost'),
    retry=Retry(max_retries=5, initial_delay=1.0)
)

# with connection callbacks and retry
def on_connection_open(connection: pika.connection.Connection):
    print(f"Connection opened: {connection}")

def on_connection_error(connection: pika.connection.Connection, error: Union[str, Exception]):
    print(f"Connection error: {error}")

amqp_connection_callback = EasyAMQP(
    pika.ConnectionParameters('localhost'),
    retry=Retry(max_retries=5, initial_delay=1.0),
    on_connection_open=on_connection_open,
    on_connection_error=on_connection_error
)
```



