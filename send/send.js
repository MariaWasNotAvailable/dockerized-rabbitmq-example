#!/usr/bin/env node

var amqp = require("amqplib/callback_api");
const url = `amqp://${process.env.AMQP_HOST}`;
const queue = process.env.QUEUE_NAME;
const timeout = 1000;

amqp.connect(url, (err0, connection) => {
    if (err0) {
        throw err0;
    }

    connection.createChannel((err1, channel) => {
        if (err1) {
            throw err1;
        }

        const msg = "It works!";

        channel.assertQueue(queue, {
            durable: false
        });

        channel.sendToQueue(queue, Buffer.from(msg));

        console.log(`Sent: ${msg}`);
    });

    setTimeout(() => {
        connection.close();
        process.exit(0);
    }, timeout);
});
