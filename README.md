## Joke Roulette

### Развертывание docker
- docker-compose up -d --build
- docker-compose exec web python manage.py makemigrations
- docker-compose exec web python manage.py migrate - сделать миграции

#### Регистрация пользователя:
POST http://127.0.0.1:8000/api/auth/users с username и password (email опционально)

#### Аутентификации пользователя (получение токена)
POST http://127.0.0.1:8000/auth/token/login/ с username и password
- Вернется "auth_token": "{token}"

### Дальнейшие запросы выполнять с ключем "Authorization" и параметром "Token {token}" в Headers

### Старт нового раунда рулетки и первый спин
POST http://127.0.0.1:8000/api/games/ 

### Последующие спины рулетки
PATCH http://127.0.0.1:8000/api/games/{id}

### Статистика в JSON по раундам (id, количество гроков)
GET http://127.0.0.1:8000/api/games/

### Статистика по игрокам (id, сыграно раундов, среднее кол-во спинов за раунд)
GET http://127.0.0.1:8000/api/players/