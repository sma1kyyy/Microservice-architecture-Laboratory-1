# RestAPI-server
![Static Badge](https://img.shields.io/badge/Python-3.12-green?style=flat-square&logo=Python&logoColor=yellow&label=Python&labelColor=%23000000%09)
![Static Badge](https://img.shields.io/badge/Docker-blue?style=flat-square&logo=DOCKER&logoColor=white)
![Static Badge](https://img.shields.io/badge/Nginx-009639?logo=nginx&logoColor=white&style=flat-square)
![Static Badge](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=Flask&logoColor=white)

---
## Описание
Rest API сервер написанный на Python с использованием FastAPI. 
Проект был разработан в качестве лабораторной работы по дисциплине "Микросервисная архитектура" студентом 2 курса специальности 09.02.01 "Компьютерные системы и комплексы".

## Используемые технологии
* `python 3.12`
* `docker`
* `nginx`
* `fastapi`
* `uvicorn`
* `pydantic`

## Инструкция по запуску
### Запуск с использованием Docker
**Пересобираете и запускаете контейнеры с помощью команды:**
```bash
docker-compose up --build
```
**После у вас появится 5 контейнеров:**
* 4 экземляра сервиса
* Балансировщик nginx

**Сделайте запрос через Nginx или вставьте URL-адрес страницы**
```bash
curl http://localhost/api/v1/contact/
```

### Запуск без Docker-a
**Запустите главный скрипт "main.py" и перейдите по ссылке:** `http://127.0.0.1:6080`
В открывшейся странице выберите одну из предложенный ссылок:
![image](https://github.com/user-attachments/assets/9f4659dc-9027-48c0-ad29-b83b1f243418)

**Откройте один из файлов** `cmd/contact.py` **или** `cmd/group.py`
В самом конце кода будет написано основное тело запроса. Можете убрать коментарии и наблюдать за изменениями на странице или в консоли VS Code.

## Структура проекта
```
C:.
│   .env
│   compose.yaml
│   Dockerfile
│   README.md
│   requirements.txt
│   
├───app
│   │   models.py
│   │   __init__.py
│   │
│   └───__pycache__
│           __init__.cpython-312.pyc
│           __init__.cpython-313.pyc
│
├───cmd
│   │   main.py
│   │   __init__.py
│   │
│   ├───routers
│   │   │   contact.py
│   │   │   group.py
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           __init__.cpython-313.pyc
│   │
│   └───__pycache__
│           main.cpython-313.pyc
│           __init__.cpython-313.pyc
│
├───nginx
│       Dockerfile
│       nginx.conf
│
└───templates
        index.html
```
