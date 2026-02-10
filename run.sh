#!/bin/bash

echo "Запуск тестов..."
python3 -m pytest

echo "Запуск Allure отчета..."
allure open allure-files