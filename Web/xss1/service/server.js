const fastify = require('fastify')()
const path = require('path');

fastify.register(require('@fastify/static'), {
    root: path.join(__dirname, 'public'),
    prefix: '/',
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