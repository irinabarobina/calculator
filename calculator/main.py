import numpy as np

print(np.__version__)
import numpy as np

# Тестовый скрипт (Задача 1)
print(f"Версия NumPy: {np.__version__}")


def add_numbers(a: float, b: float) -> float:
    """
    Складывает два числа.

    Args:
        a (float): Первое число.
        b (float): Второе число.

    Returns:
        float: Сумма чисел.
    """
    return a + b


# Проверка, что функция работает
if __name__ == "__main__":
    result = add_numbers(10, 20)
    print(f"Результат сложения: {result}")
