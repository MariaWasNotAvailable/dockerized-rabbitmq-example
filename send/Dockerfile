FROM node:current-alpine

WORKDIR /usr/src/rmq_app

ENV QUEUE_NAME=test
ENV AMQP_HOST=guest:guest@rabbitmq:5672

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD [ "npm", "start" ]