"""Общий запуск pytest для скриптов в start_test/.

Использование:
    from start_test._runner import run_pytest
    run_pytest("tests", "-m", "basic", "-v")
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def run_pytest(*args: str) -> int:
    """Запускает pytest из корня проекта тем же интерпретатором Python.

    :param args: аргументы, передаваемые pytest (например, "tests", "-v").
    :return: код выхода (0 = успех).
    """
    cmd = [sys.executable, "-m", "pytest", *args]
    print(f"▶ Запуск: {' '.join(cmd)}")
    print(f"  Рабочая директория: {PROJECT_ROOT}\n")

    result = subprocess.run(cmd, cwd=PROJECT_ROOT)
    return result.returncode


def main(*args: str) -> None:
    """Удобная обёртка для запуска из `if __name__ == "__main__"`."""
    sys.exit(run_pytest(*args))