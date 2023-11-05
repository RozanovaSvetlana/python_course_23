from celery import Celery

app = Celery("hw_4", broker="amqp://", backend="rpc://", include=["hw_4.task"])
