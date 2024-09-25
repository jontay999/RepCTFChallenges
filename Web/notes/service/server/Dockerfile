FROM node:20-alpine

RUN apk add --update dumb-init && \
rm -rf /var/lib/apt/lists/* && \
addgroup inmate && \
adduser --disabled-password --gecos "" --ingroup inmate inmate

WORKDIR /home/inmate/app
COPY package*.json ./
COPY server.js ./
COPY public/ ./public/

ENV NODE_ENV=production 
ENV flag=REP{have_you_heard_of_xs_leaks_before?}
RUN chown -R inmate:inmate . && \
npm ci --omit=dev --ignore-scripts --no-audit --no-fund
USER inmate

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["node", "./server.js"]