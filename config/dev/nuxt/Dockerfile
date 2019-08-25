FROM node:12-alpine
LABEL maintainer="info@rubyfire.ru"

RUN apk update \
  && apk add git yarn

WORKDIR /app

COPY ./package.json /app/package.json
COPY ./yarn.lock /app/yarn.lock
RUN yarn install

ENV HOST 0.0.0.0
