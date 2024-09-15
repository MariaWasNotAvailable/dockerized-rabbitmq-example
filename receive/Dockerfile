FROM python:alpine

WORKDIR /usr/src/rmq_app

ENV QUEUE_NAME=test
ENV AMQP_HOST=rabbitmq
ENV AMQP_PORT=5672

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-u", "receive.py" ]