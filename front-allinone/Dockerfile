# build
FROM node:15.7.0-alpine3.10 as build
WORKDIR /app

COPY . .

RUN npm install
RUN npm install -g @vue/cli

ENV PATH="/app/node_modules/.bin:${PATH}"
RUN npm run build

# production
FROM nginx:1.25-alpine-slim as production
WORKDIR /usr/share/nginx/html
COPY --from=build /app/dist .

# Copiez le fichier de configuration Nginx
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf