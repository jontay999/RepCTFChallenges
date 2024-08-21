```bash
docker build -t repctf-web-3 .
docker run -d -p 3002:3000 --name web-3 repctf-web-3
```

Note that my puppeteer version is `"puppeteer": "^15.5.0"`
even though the latest is v23 because there is issues with the chromium that can be downloaded onto the node18 slim buster image
