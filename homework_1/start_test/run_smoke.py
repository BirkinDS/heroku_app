"""Запуск только smoke-тестов: `pytest -m smoke -v`."""

from start_test._runner import main

if __name__ == "__main__":
    main("tests", "-m", "smoke", "-v", "-s")