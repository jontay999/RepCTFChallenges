FROM node:20-alpine

WORKDIR /usr/src/app

COPY package*.json ./
COPY public ./public/
COPY server* ./

ENV FLAG=REP{sp00f1ng_ips_4nd_w31rd_str1ng_r3PL4C3m3nts}
RUN npm ci --omit=dev --ignore-scripts --no-audit --no-fund

CMD [ "node", "server.js" ]