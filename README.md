# <span style="color:#FF0000">📚 ДОКУМЕНТАЦИЯ</span>

## Backend проекта TMPAUTH

---
Приложение с аутентификацией созданной с помощью FastAPI Users

## 🚀 **Запуск приложения через Docker:**

Добавляем в .env
```bash
TMPAUTH_SQLALCHEMY_HOST=127.0.0.1
TMPAUTH_SQLALCHEMY_PORT=5432
TMPAUTH_SQLALCHEMY_USERNAME=tmpauth
TMPAUTH_SQLALCHEMY_PASSWORD=tmpauth
TMPAUTH_SQLALCHEMY_BASE_NAME=tmpauth

TMPAUTH_AUTH_RESET_PASSWORD_TOKEN_SECRET=dcf38976fa88e8bd281c491d180fd2d34f510eb1a9cc57c22f514499430a0f34
TMPAUTH_AUTH_VERIFICATION_TOKEN_SECRET=48683743363d588d7d64d97384366079215c48f6365f2ca36ff4a9d3bd55eadf

POSTGRES_DB=tmpauth
POSTGRES_USER=tmpauth
POSTGRES_PASSWORD=tmpauth
```
token secrets можно перегенирировать перед стартом приложения или вставить текущие.


```bash
docker-compose --project-directory . -f deploy/docker-compose.yml up -d
```
Создаются автоматически бд, миграции и создается суперпользователь log: admin@site.com pass: admin

страница документации доступна по url: http://0.0.0.0:8000/api/docs#

## 🚀 Локальный запуск приложения:

## 📈 Создание БД:
```bash
sudo -u postgres psql

CREATE USER tmpauth WITH PASSWORD 'tmpauth';
ALTER USER tmpauth CREATEDB;
CREATE DATABASE tmpauth WITH OWNER tmpauth;
```


```bash
python store/web/main.py
```

```bash
./entrypoint.sh start_app
```

## 📈 Запуск миграций:
***создание миграций alembic:***
```bash
alembic revision --autogenerate -m "..."
```

***применить миграций alembic:***
```bash
alembic upgrade head
```

***откатить миграций alembic:***

*последнюю миграцию:*
**
```bash
alembic downgrade -1
```
*все миграции:*
**
```bash
alembic downgrade base
```

## Проверка ошибок:

### 1. 🆘 Help для entrypoint (просмотр команд для тестирования)

```bash
./entrypoint.sh help
```