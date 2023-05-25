# api_final_yatube
# Описание
Это DRF-проект. Здесь можно создать аккаунт, получив JWT-токен. После авторизации каждый пользователь имеет право на создание/изменение/удаление своего поста, добавление/изменение/удаление комментариев к другим постам пользователей, а также есть возможность подписаться на любимых или не очень любимых авторов. Устанавливай и пробуй!

# Установка
1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Ant0shich/api_final_yatube.git
```
2. Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```

```
source venv/bin/activate
```
3. Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
4. Выполнить миграции:
```
python manage.py migrate
```
5. Запустить проект:
```
python manage.py runserver
```

# Примеры
1. Получение JWT-токена (POST)
```
http://127.0.0.1:8000/api/v1/jwt/create/
```
![number1.png](number1.png)

2. Создание публикации (POST)
```
http://127.0.0.1:8000/api/v1/posts/
```
![number2.png](number2.png)

3. Получение публикаций (GET)
```
http://127.0.0.1:8000/api/v1/posts/
```
![number3.png](number3.png)

4. Добавление комментария (POST)
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
![number4.png](number4.png)
