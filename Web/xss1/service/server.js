const fastify = require('fastify')()
const path = require('path');

fastify.register(require('@fastify/static'), {
    root: path.join(__dirname, 'public'),
    prefix: '/',
});


fastify.post('/submit', async (request, reply) => {
    try {
        const answers = request.body;
        console.log('Received answers:', answers);
        reply.send({ status: 'success', data: answers });
    } catch (error) {
        console.error('Error:', error);
        reply.status(500).send({ status: 'error', message: 'Internal Server Error' });
    }
});

fastify.get('/', (req, reply) => {
    reply.sendFile('index.html');
});

// Run the server!
fastify.listen({ port: 3000 }, function (err, address) {
    if (err) {
        console.error(err)
        process.exit(1)
    }
})