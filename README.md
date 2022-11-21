# Schetchiki

## Данный интернет магазин сделан при помощи Django
![Github Repo Size](https://img.shields.io/github/repo-size/WEBGROUP-TUJ/Schetchiki?style=for-the-badge) ![Heroku](https://img.shields.io/github/workflow/status/WEBGROUP-TUJ/Schetchiki/Heroku%20Deploy?label=Heroku%20deploy&style=for-the-badge) ![Docker](https://img.shields.io/github/workflow/status/WEBGROUP-TUJ/Schetchiki/Docker?color=%232496ED&label=Docker&logo=%232496ED&logoColor=%232496ED&style=for-the-badge)

## О проекте

Магазин выполненный на django версии 2.1, python 3.9. С bootstrap, CSS, HTML5, JavaScript для фронта и PostgreSQL.
Магазин имеет такой функционал:

- Список всех продуктов;
- Список категорий;
- Добавление изображений к продукту;
- Возможность добавлять и удалять из корзины;
- Оформлять заказ через корзину, тем самым добавляя его в БД;

## Бэкенд разработчик

* [**Муслитдинов Улугбек**](https://github.com/UlugbekMuslitdinov) - @UlugbekMuslitdinov

## Фронтенд разработчик

* [**Тимур Касимов**](https://github.com/timakasimovkra) - @timakasimovkra

## Установка:
### С помощью Docker:

```properties
docker-compose up -d --build
```
```properties
docker-compose exec web python manage.py migrate
```

### Проект находится под лицензией [MIT](https://github.com/WEBGROUP-TUJ/Rozgor/blob/main/LICENSE)

### Все полезные ссылки к этому проекту:
* [Docker image](https://hub.docker.com/repository/docker/ulugbekus/rozgor)
* [Website](https://schetchiki.herokuapp.com)
