FROM node:lts-alpine
WORKDIR /app
COPY package*.json ./
RUN yarn install
COPY . .
EXPOSE 4173
ENV VITE_API_URL=https://pomme.tech/api
ENV VITE_CLOUDINARY_PRESET=pomme-img
ENV VITE_CLOUDINARY_URL=https://api.cloudinary.com/v1_1/:cloud_name/
RUN yarn build
ENTRYPOINT ["yarn"]
CMD ["preview", "--host"]
