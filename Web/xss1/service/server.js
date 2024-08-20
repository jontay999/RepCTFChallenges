const puppeteer = require("puppeteer")
const fastify = require('fastify')()
const path = require('path');

fastify.register(require('@fastify/static'), {
    root: path.join(__dirname, 'public'),
    prefix: '/',
});

// This variable will be initialised later
// I dont want to keep launching new puppeteer instances so everyone will share this instance of the browser
let browser;
const port = 3000;

// Since each request to /submit launches my admin bot
// I limit requests to max 3 per minute on the /submit route
(async () => {
    await fastify.register(require('@fastify/rate-limit'), {
        max: 3,
        timeWindow: '1 minute',
        allowList: [],
        onExceeding: function (request, key) {
            console.log('callback on exceededing ... executed before response to client')
        },
        onExceeded: function (request, key) {
            console.log('callback on exceeded ... ')
        }
    })

    // Well technically I could verify them here but where's the fun in that
    // let me launch a bot that can visit my own website to see if the answers are posted nicely there
    // before all that, let me hide my cookie inside
    const cookies = [{
        'name': 'flag',
        'value': 'REP{fake_flag}'
    }];
    const verify_answers = async (answers) => {
        const query_param = new URLSearchParams(answers).toString();
        const base_url = `http://localhost:${port}`
        console.log("visiting url:", base_url)
        const ctx = await browser.createBrowserContext()
        const page = await ctx.newPage()
        await page.goto(base_url, { timeout: 5000, waitUntil: 'networkidle2' })
        await page.setCookie(...cookies);
        try {
            const url_with_answers = `http://localhost:${port}?${query_param}`
            console.log("visiting url with answers:", url_with_answers)
            await page.goto(url_with_answers, { timeout: 5000, waitUntil: 'networkidle2' })
            await page.waitForSelector('textarea')
        } finally {
            await page.close()
            await ctx.close()
        }
    }

    fastify.post('/submit', (request, reply) => {
        console.log("just happily submitting")
        try {
            const answers = request.body;
            // reply.send({ message: "Answers submitted! I'll get an admin to check those answers soon..." });
            const queryParams = new URLSearchParams(answers).toString();
            console.log("hello")
            reply.redirect(`/answers?${queryParams}`);
            // verify_answers(answers)
        } catch (error) {
            console.error('Error:', error);
            reply.status(500).send({ status: 'error', message: 'Internal Server Error' });
        }
    });

    fastify.get('/answers', (request, reply) => {
        const answers = request.query;
        reply.send(answers);
    });

    fastify.get('/', {
        config: {
            rateLimit: false
        }
    }, (req, reply) => {
        reply.sendFile('index.html');
    });

    // Run the server!
    fastify.listen({ port }, async (err, address) => {

        console.log(`[*] Listening on port ${port} ${address}`)
        if (err) {
            console.error(err)
            process.exit(1)
        }

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