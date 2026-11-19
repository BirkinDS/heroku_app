"""Запуск всех тестов: эквивалент `pytest -v` из корня проекта."""

from start_test._runner import main

if __name__ == "__main__":
    main("tests", "-v", "-s")