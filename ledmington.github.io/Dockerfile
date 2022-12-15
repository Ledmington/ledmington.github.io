FROM node:19.3.0-alpine3.16

RUN apk update && apk upgrade
WORKDIR /home
EXPOSE 80
COPY package.json .
COPY package-lock.json .
RUN npm install
COPY . .
RUN npm run build
CMD npm run serve -- -p 80
