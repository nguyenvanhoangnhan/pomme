FROM node:lts-alpine
WORKDIR /app
COPY package*.json ./
RUN yarn install
COPY . .
EXPOSE 5173
ENTRYPOINT ["yarn"]
CMD ["dev"]
