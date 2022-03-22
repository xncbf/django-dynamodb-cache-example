# django-dynamodb-cache-example

## Quick start

```sh
pipenv install
pipenv run python manage.py createcachetable
pipenv run python manage.py runserver
```

Connect to <localhost:8000>

This page is supposed to show a random number every time you log in.

And it's wrapped in a decorator that caches for 5 seconds.

The page is held for 5 seconds by the `@cache_page(5)` decorator.
