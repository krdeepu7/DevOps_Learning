FROM node:20-alpine

ENV backend_url=http://localhost:4000

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]