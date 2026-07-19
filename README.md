# QA Python Portfolio

Этот репозиторий — моё портфолио учебных проектов по автоматизации тестирования на Python. Здесь собраны автотесты для API и UI, а также артефакты ручного тестирования (тест-кейсы, баг-репорты). Репозиторий демонстрирует мои навыки как Junior Manual QA Engineer с основами автоматизации.

## 🛠️ Стек технологий
- **Язык:** Python 3.x
- **Фреймворки для тестов:** PyTest, Unittest
- **UI-тестирование:** Playwright
- **API-тестирование:** Requests
- **Инструменты:** Git, GitHub, Docker (базовое знание), Jenkins (базовое знание)
- **Базы данных:** SQL (SELECT, JOIN)

## 📂 Структура проекта
- **`portfolio/`** — папка с основными проектами и артефактами
  - **`api_booking_tests/`** — API-автотесты для сервиса бронирования (PyTest, Requests)
  - **`pytest_bank_and_lib_app/`** — тесты для банковского и библиотечного приложений на PyTest
  - **`unittest_bank_and_lib_app/`** — аналогичные тесты на Unittest
  - **`ui_saucedemo_tests/`** — UI-автотесты для интернет-магазина (Playwright, POM)
  - **`test_cases/`** — примеры тест-кейсов (ручное тестирование)
  - **`bug_report/`** — примеры баг-репортов
  - **`flask_app_docker/`** — пример веб-приложения с Dockerfile
- **`src/`** — переиспользуемый код, общий для тестов (утилиты, конфигурация логирования)

## 🚀 Запуск всех тестов

Для запуска всех тестов из папки `portfolio` выполните команду из корня проекта:

```bash
pytest portfolio/
```

## 🚀 Запуск конкретных тестов
- Только PyTest-тесты:
```bash
pytest portfolio/pytest_bank_and_lib_app/tests/
```
- Только Unittest-тесты:
```bash
python -m unittest discover -s portfolio/unittest_bank_and_lib_app/tests -p "*.py"
```
- Только API-тесты:
```bash
pytest portfolio/api_booking_tests/tests/
```
- Только UI-тесты:
```bash
pytest portfolio/ui_saucedemo_tests/tests/
```

## 📦 Установка и настройка
1. Клонируйте репозиторий:
```bash
git clone https://github.com/Yuliya-Ausiannikava/automated_testing_on_python.git
```
2. Создайте виртуальное окружение и установите зависимости:
```bash
python -m venv venv
source venv/bin/activate  # для Windows: `venv\Scripts\activate`
pip install -r requirements.txt
```
3. Установите проект в режиме разработки (чтобы импорты работали корректно):
```bash
pip install -e .
```
