const puppeteer = require("puppeteer")
const fastify = require('fastify')()
const path = require('path');

fastify.register(require('@fastify/static'), {
    root: path.join(__dirname, 'public'),
    prefix: '/',
});

let browser;
const port = 3000;

// Apply a rate limit of 3/min per IP for /submit as it  launches my admin bot which is a bit expensive
const rateLimit = {
    max: 3,
    timeWindow: '1 minute',
    allowList: [],
    onExceeded: function (request, key) {
        console.log(`Exceeded rate limit for ip: ${key} `)
    }
};

(async () => {
    await fastify.register(require('@fastify/rate-limit'), { global: false })

    // I'll launch an admin bot that checks the answers at /answers?
    // before all that, let me hide the flag in my cookie inside
    // see if you can get the cookie from my bot!
    const cookies = [{
        'name': 'flag',
        'value': process.env.FLAG || "REP{FAKE_FLAG}"
    }];
    const verify_answers = async (answers) => {
        const query_param = new URLSearchParams(answers).toString();
        const base_url = `http://localhost:${port}`
        const ctx = await browser.createBrowserContext()
        const page = await ctx.newPage()
        await page.goto(base_url, { timeout: 5000, waitUntil: 'networkidle2' })
        await page.setCookie(...cookies);
        try {
            const url_with_answers = `${base_url}/answers?${query_param}`
            await page.goto(url_with_answers, { timeout: 5000, waitUntil: 'networkidle2' })
        } catch (error) {
            console.error("Error in puppeteer here:", error)
        } finally {
            await page.close()
            await ctx.close()
        }
    }

    fastify.post('/submit', { config: { rateLimit } }, (request, reply) => {
        try {
            const answers = request.body;
            const queryParams = new URLSearchParams(answers).toString();
            reply.redirect(`/answers?${queryParams}`);
            verify_answers(answers)
        } catch (error) {
            console.error('Error:', error);
            reply.status(500).send({ status: 'error', message: 'Internal Server Error' });
        }
    });

    // Render my answers on the screen, surely there's no problem here... right? 🫠
    fastify.get('/answers', (request, reply) => {
        const answers = request.query;
        let html = "<h1>Answers:</h1><br/>"
        for (const [key, value] of Object.entries(answers)) {
            html += `<div><b>${key}:</b> ${value}</div>`
        }
        reply.header('Content-Type', 'text/html').send(`<html><code>${html}</code></html>`);
    });

    fastify.get('/', (req, reply) => {
        reply.sendFile('index.html');
    });

    fastify.listen({ port }, async (err, address) => {
        console.log(`[*] Listening on port ${port} ${address}`)
        browser = await puppeteer.launch({
            pipe: true,
            dumpio: true,
            args: [
                '--incognito',
                '--disable-dev-shm-usage', // Docker stuff
                '--js-flags=--noexpose_wasm,--jitless', // No Chrome n-days please
                '--disable-background-networking',
                '--disable-default-apps',
                '--disable-extensions',
                '--disable-sync',
                '--no-first-run' // Skip first-run setup
            ]
        })
    })
})();
// I am sad about this IIFE nonsense due to fastify4 affecting fastify.register(...) and CommonJS not supporting top level awaits
// if the above sentence means nothing to you, don't worry about it
// it just explains why the whole server code is wrapped in a bunch of weird brackets