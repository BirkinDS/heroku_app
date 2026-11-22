"""Запуск пяти тестов homework_2 из любой рабочей директории."""
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if __name__ == "__main__":
    command = [sys.executable, "-m", "pytest", "tests", "-v", "-s"]
    print(f"▶ Запуск: {' '.join(command)}")
    print(f"  Рабочая директория: {PROJECT_ROOT}\n")
    raise SystemExit(subprocess.run(command, cwd=PROJECT_ROOT).returncode)
