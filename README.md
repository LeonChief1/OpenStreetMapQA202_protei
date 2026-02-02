# OpenStreetMapQA202_protei

### Шаги
1. Склонировать проект `https://github.com/LeonChief1/OpenStreetMapQA202_protei.git`
2. Установить все зависимости `pip install -r requirements.txt`
3. Запустить тесты `python -m pytest`
4. Сгенерировать отчет `allure generate allure-files -o allure-report`
5. Открыть отчет `allure open allure-report`

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
