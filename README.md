# WeatherApp
Сервис на Python для просмотра прогноза погоды.

🔍 Особенности

Прогноз погоды берется через API и выдается пользователю в читаемом формате.

🛠 Технологический стек

Python 3.13  
Django  
Docker  

⏬Установка

python -m venv venv source  
venv/bin/activate  
docker-compose up -d --build  

-Для запуска достаточно запустить docker-compose, он установит requirements.txt, примении миграции и запустит сервер(http://127.0.0.1:8000/).

Так же была попытка сделать регистрацию и возможность просматривать историю запросов, подсказки при вводе и возможность выбора проследнего запроса.
