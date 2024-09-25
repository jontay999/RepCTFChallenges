FROM node:16-alpine

WORKDIR /usr/src/app

COPY package*.json ./
COPY public ./public/
COPY server.js ./

ENV FLAG=REP{y0ur_f1r5t_5ql_1nj3ct10n_well_done!!!}
ENV ADMIN_PASSWORD=bfe033bd878eadbb7e50a1c3bae3543b
RUN npm install && npm cache clean --force

CMD [ "node", "server.js" ]