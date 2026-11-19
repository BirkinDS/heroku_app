"""Запуск теста Checkboxes."""

from start_test._runner import main

if __name__ == "__main__":
    main("tests/basic/test_checkboxes.py", "-v", "-s")