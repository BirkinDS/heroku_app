"""Запуск только regression-тестов: `pytest -m regression -v`."""

from start_test._runner import main

if __name__ == "__main__":
    main("tests", "-m", "regression", "-v", "-s")