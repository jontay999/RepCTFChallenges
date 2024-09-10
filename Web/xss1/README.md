# XSS 1

**Author**: jontay999

**Category**: Web

[Solution](solve/solve.py)

## Description

Whats XSS?

## Difficulty

Easy

## Deployment

```bash
docker build -t repctf-web-3 .
docker run -d -p 3002:3000 --name web-3 repctf-web-3
```

Note that my puppeteer version is `"puppeteer": "^15.5.0"`
even though the latest is v23 because there is issues with the chromium that can be downloaded onto the node18 slim buster image

- also note that it has to bind to the `0.0.0.0` interface or it won't be able to launch, [ref](https://github.com/fastify/fastify/issues/935#issuecomment-629351328)
