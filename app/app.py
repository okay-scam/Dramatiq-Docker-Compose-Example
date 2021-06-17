import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

import requests

broker = RabbitmqBroker(url="amqp://rabbit:rabbit@rabbitmq:5672")
dramatiq.set_broker(broker)

@dramatiq.actor
def count_words(url):
    response = requests.get(url)
    count = len(response.text.split(" "))
    print(f"There are {count} words at {url!r}.")

if __name__ == "__main__":
    count_words.send("https://dramatiq.io/guide.html")
