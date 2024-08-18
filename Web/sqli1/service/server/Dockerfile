FROM node:16-buster-slim

WORKDIR /usr/src/app

COPY package*.json ./
COPY public ./public/
COPY server.js ./

ENV FLAG=REP{y0ur_f1r5t_5ql_1nj3ct10n_well_done!!!}
RUN npm install

CMD [ "node", "server.js" ]