FROM node:15-alpine

RUN npm install -g http-server

WORKDIR /frontend-v2

COPY package*.json /frontend-v2/

RUN npm install

COPY . /frontend-v2/

RUN npm run build

EXPOSE 8080

CMD [ "http-server", "dist" ]
