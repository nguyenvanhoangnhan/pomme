FROM node:lts-alpine
WORKDIR /app
COPY package*.json ./
RUN yarn install
COPY . .
EXPOSE 4173
RUN yarn build
ENTRYPOINT ["yarn"]
CMD ["preview", "--host"]
