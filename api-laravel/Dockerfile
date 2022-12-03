FROM php:8.0-fpm
COPY composer.lock composer.json /var/www/
COPY database /var/www/database
WORKDIR /var/www
RUN apt-get update && apt-get -y install git && apt-get -y install zip
COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer
COPY . /var/www
RUN COMPOSER_ALLOW_SUPERUSER=1 composer update

RUN chown -R www-data:www-data \
       /var/www/storage \
       /var/www/bootstrap/cache

RUN php artisan cache:clear
RUN php artisan optimize
RUN php artisan config:clear
RUN docker-php-ext-install pdo_mysql

RUN php artisan optimize
RUN php artisan key:generate
RUN php artisan config:cache
RUN php artisan route:clear
EXPOSE 8000

CMD ["php", "artisan", "serve", "--host=0.0.0.0", "--port=8000"]
