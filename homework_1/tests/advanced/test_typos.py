import pytest

from pages.typos_page import TyposPage


def _find_first_difference(expected: str, actual: str) -> str:
    min_len = min(len(expected), len(actual))
    for i in range(min_len):
        if expected[i] != actual[i]:
            return f"позиция {i}: ожидалось '{expected[i]}', получено '{actual[i]}'"
    if len(expected) != len(actual):
        return f"длина: ожидалось {len(expected)}, получено {len(actual)}"
    return "расхождений не найдено"


@pytest.mark.regression
def test_typos(browser):
    page = TyposPage(browser).open()

    typo_attempts = []
    correct_attempts = []

    for i in range(1, 11):
        text = page.get_second_paragraph_text()

        if text == page.CORRECT_TEXT:
            correct_attempts.append(i)
        else:
            typo_attempts.append({
                "attempt": i,
                "diff": _find_first_difference(page.CORRECT_TEXT, text),
            })

        page.refresh()
    # Базовые проверки корректности сценария
    assert len(correct_attempts) + len(typo_attempts) == 10
    assert page.get_second_paragraph_text() != "", "Текст не должен быть пустым"
    # Печатаем сводку (видно при запуске с -s)
    print(f"\nБез опечатки: {len(correct_attempts)}, с опечаткой: {len(typo_attempts)}")
    for item in typo_attempts:
        print(f"  Попытка {item['attempt']}: {item['diff']}")