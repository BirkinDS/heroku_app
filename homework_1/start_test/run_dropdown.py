"""Запуск теста Dropdown."""

from start_test._runner import main

if __name__ == "__main__":
    main("tests/basic/test_dropdown.py", "-v", "-s")