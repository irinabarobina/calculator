import random
import string


def generate_password(length, use_lower, use_upper, use_digits, use_special):
    """Генерирует пароль на основе выбранных настроек."""
    characters = ""

    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"

    if not characters:
        return "Ошибка: выберите хотя бы один тип символов."

    # Генерация пароля
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=" * 40)
    print("   ГЕНЕРАТОР ПАРОЛЕЙ")
    print("=" * 40)

    # Ввод длины пароля с проверкой
    try:
        length_input = input("\nВведите длину пароля (минимум 4): ")
        length = int(length_input)
        if length < 4:
            print("Длина слишком мала. Установлено значение: 4")
            length = 4
    except ValueError:
        print("Некорректный ввод. Установлена длина по умолчанию: 12")
        length = 12

    # Настройки состава пароля
    print("\nНастройки состава пароля (y - да, n - нет):")
    use_lower = input("Строчные буквы (a-z)? [y/n]: ").lower() == 'y'
    use_upper = input("Заглавные буквы (A-Z)? [y/n]: ").lower() == 'y'
    use_digits = input("Цифры (0-9)? [y/n]: ").lower() == 'y'
    use_special = input("Спецсимволы (!@#...)? [y/n]: ").lower() == 'y'

    # Если ничего не выбрано, включаем всё для безопасности
    if not any([use_lower, use_upper, use_digits, use_special]):
        print("\nВнимание: ни один тип символов не выбран.")
        print("Для генерации включены все типы символов.")
        use_lower = use_upper = use_digits = use_special = True

    # Генерация и вывод результата
    result = generate_password(length, use_lower, use_upper, use_digits, use_special)

    print("\n" + "-" * 40)
    print("ВАШ ПАРОЛЬ:")
    print(f">>> {result}")
    print("-" * 40)


if __name__ == "__main__":
    main()