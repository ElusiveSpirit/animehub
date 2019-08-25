FROM node:12-alpine
LABEL maintainer="info@rubyfire.ru"

RUN apk update \
  && apk add git yarn

RUN addgroup -S nuxt \
    && adduser -S -G nuxt nuxt


WORKDIR /app

COPY ./package.json /app/package.json
COPY ./yarn.lock /app/yarn.lock
RUN yarn install

COPY ./config/production/nuxt/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start
RUN chown nuxt /start

COPY . /app

RUN chown nuxt /app

USER nuxt
ENV HOST 0.0.0.0

RUN yarn run build
