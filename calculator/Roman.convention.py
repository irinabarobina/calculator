def int_to_roman(num: int) -> str:
    """Конвертирует обычное число в римское."""
    # Список соответствий: от больших значений к меньшим
    # Включаем сюда "составные" числа вроде 900 (CM), 400 (CD) и т.д.
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    roman_num = ""
    i = 0

    # Пока число не станет равным нулю
    while num > 0:
        # Сколько раз текущее значение помещается в числе?
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1

    return roman_num


def roman_to_int(s: str) -> int:
    """Конвертирует римское число в обычное."""
    # Словарь значений одиночных символов
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    # Проходим по строке справа налево (от конца к началу)
    # Это упрощает логику вычитания
    for char in reversed(s):
        value = roman_values[char]

        # Если текущий символ меньше предыдущего (который был правее),
        # значит это случай вычитания (например, I перед V)
        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value

    return total


# --- ПРОВЕРКА РАБОТЫ ---

# Тест 1: Из условия задачи (Римские -> Обычные)
print("--- Конвертация из Римских в Арабские ---")
roman_tests = ["IV", "IX", "XLII", "XCIX", "MMXXIII"]
for roman in roman_tests:
    result = roman_to_int(roman)
    print(f"{roman} -> {result}")

print("\n--- Конвертация из Арабских в Римские ---")
# Тест 2: Обратная проверка (Обычные -> Римские)
arabic_tests = [4, 9, 42, 99, 2023, 1994]
for arabic in arabic_tests:
    result = int_to_roman(arabic)
    print(f"{arabic} -> {result}")