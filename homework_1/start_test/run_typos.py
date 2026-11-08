"""Запуск теста Typos."""

from start_test._runner import main

if __name__ == "__main__":
    main("tests/advanced/test_typos.py", "-v", "-s")