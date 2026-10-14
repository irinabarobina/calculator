from main import add_numbers  # Импортируем функцию из твоего файла main.py


def test_add():
    """Тест для проверки сложения."""
    assert add_numbers(2, 3) == 5, "Ошибка: 2 + 3 должно быть равно 5"
    assert add_numbers(-1, 1) == 0, "Ошибка: -1 + 1 должно быть равно 0"
    print("Тесты пройдены успешно!")


if __name__ == "__main__":
    test_add()
