# OpenStreetMapQA202_protei

### Шаги
1. Склонировать проект `https://github.com/LeonChief1/OpenStreetMapQA202_protei.git`
2. Установить все зависимости `pip install -r requirements.txt`
3. Запустить тесты `python -m pytest`
4. Сгенерировать отчет `allure generate allure-files -o allure-report`
5. Открыть отчет `allure open allure-report`

- Или перейти в директорию `cd allure-report`
- Запустить сервер http `python -m http.server 8080`
- Зайди на страницу с ответочм по ссылке: `http://localhost:8080`

### Стек:
- pytest
- selenium
- webdriver manager
- requests
- allure
- configparser
- json

### Структура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./configuration - провайдер настроек
    - test_config.ini - настройки для тестов
- ./testdata - провайдер тестовых данных
    - test_data.json

### Если не работает UI тесты
Я использую Chromium-ghost и тесты могут не запускаться на обычном chrome.
Для этого можно попробовать 
- Скачиваем драйвер для версии 127:
1. `cd /tmp`
2. `wget https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.72/linux64/chromedriver-linux64.zip`
3. `unzip chromedriver-linux64.zip`
4. `chmod +x chromedriver-linux64/chromedriver`
5. Копируем в системный путь `sudo mv chromedriver-linux64/chromedriver /usr/local/bin/chromedriver_127`
6. Проверяем: `chromedriver_127 --version`