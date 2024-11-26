FROM php:8.1-apache

# Установить зависимости
RUN apt-get update && apt-get install -y \
    zip unzip curl libpng-dev libjpeg-dev libfreetype6-dev \
    && docker-php-ext-install pdo pdo_mysql gd

# Установить Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Скопировать проект
COPY src/ /var/www/html/

# Установить права
RUN chown -R www-data:www-data /var/www/html/
