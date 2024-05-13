# ElasticDjango

Django application for managing users stored on ElasticSearch.

## Running the project

Most of the project configuration comes from environment variables, see ``.env-example`` file. You can run the project by executing:

```
   ./run.sh
```

Tested with:

  - Docker version 24.0.6, build ed223bc
  - docker-compose version 1.29.2, build 5becea4c

The application will be available on [http://localhost:8000/](http://localhost:8000/)

## Running tests

To run tests, use:

```
docker compose run mysite bash -c "poetry run pytest mysite/apps --cov ."
```

A coverage report will be displayed.

## API docs

Swagger api docs are available on [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/) application will be available on [localhost:8000](http://localhost:8000/)

[![API docs](/assets/api-docs-screen.png)

## Application details

The django application has 4 django apps:

- authentication: Auth endpoints for JWT authentication
  * POST ```/api/v1/auth/token/```: Takes a set of user credentials and returns an access and refresh JSON web token;
  * POST ```/api/v1/auth/refresh/```: Takes a refresh type JSON web token and returns an access type JSON web token;
  * POST ```/api/v1/auth/logout/```: Logs out the logged-in user;
- core: Responsible for core functionalities used by other apps
- users: Users related stuff, such as custom user model, api endpoints for registering new user and managing profile
  * POST ```/api/v1/users/register/```: Registers a new users;
  * PUT/PATCH/GET: ```/api/v1/users/me/```: Manage logged user data;
- elastic: API endpoints for ElasticSearch interaction (documents creation, update and searching)
  * POST ```/api/v1/elastic/documents/```: Stores a new document on ES;
  * GET ```/api/v1/elastic/documents/```: Queries documents from a given timestamp (1 hour drift);
  * GET ```/api/v1/elastic/documents/{id}/```: Queries documents by id;
  * PUT ```/api/v1/elastic/documents/{id}/```: Updates a document;
  * GET ```/api/v1/elastic/documents/{id}/```: Partial update of a document;

## Technologies

- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Django](https://www.djangoproject.com/)
- [Django rest framework](https://www.django-rest-framework.org/)
- [Django rest framework SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [Pytest](https://docs.pytest.org/en/8.2.x/)
- [Black](https://pypi.org/project/black/)
- [ElasticSearch Python DSL](https://elasticsearch-dsl.readthedocs.io/en/latest/)
- [Poetry](https://python-poetry.org/)
