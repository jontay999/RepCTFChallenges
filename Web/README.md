### Challenges

- typically zip file including Dockerfile
- double check with zeyu to see if i need to do stuff about rce

### Dockerfiles

- For express apps

```Dockerfile
FROM node:16-buster-slim

WORKDIR /usr/src/app

COPY package*.json ./
COPY public ./public/
COPY server.js ./

ENV FLAG=REP{fake_flag}
RUN npm install

CMD [ "node", "server.js" ]
```

- Standard just deploy SPA

```Dockerfile
FROM nginx:latest

COPY public /usr/share/nginx/html

```

## Challenges

1. inspect (done)

- just read code

2. sqli1 (done)

- simple sqli to login as `admin`

3. xss1 (done)

- quiz app, admin bot can read the notes

4. careless mistake (done)

- figure out token

5. dom clobbering

-
