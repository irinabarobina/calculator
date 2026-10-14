# 1. Создаем наши алфавиты (строки с буквами по порядку)
rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
eng = "abcdefghijklmnopqrstuvwxyz"


def caesar(text, shift, mode):
    result = ""  # Сюда будем собирать новый текст

    # Если мы хотим расшифровать, то сдвигаем буквы в обратную сторону
    # Для этого просто делаем сдвиг отрицательным
    if mode == 'decrypt':
        shift = -shift

    # 2. Запускаем цикл: проходим по каждой букве в тексте
    for letter in text:

        # Проверяем: может быть эта буква есть в русском алфавите?
        if letter.lower() in rus:
            alphabet = rus
        # А может в английском?
        elif letter.lower() in eng:
            alphabet = eng
        else:
            # Если это пробел, запятая или цифра — оставляем как есть
            # и переходим к следующей букве (continue)
            result += letter
            continue

        # Находим номер (индекс) нашей буквы в алфавите (с 0)
        index = alphabet.find(letter.lower())

        # Считаем новый номер буквы.
        # len(alphabet) нужно, чтобы когда мы доходим до конца алфавита,
        # мы возвращались в начало (как колесо).
        new_index = (index + shift) % len(alphabet)

        # Берем новую букву из алфавита по новому номеру
        new_letter = alphabet[new_index]

        # 3. Проверка регистра: если исходная буква была большой,
        # то и новую делаем большой (.upper())
        if letter.isupper():
            new_letter = new_letter.upper()

        # Добавляем новую букву в результат
        result += new_letter

    return result


secret_text = "Привет, World!"
key = 5  # Наш секретный ключ (сдвиг на 5 букв)

print("Оригинал:", secret_text)

# Шифруем
encrypted = caesar(secret_text, key, 'encrypt')
print("Зашифровано:", encrypted)

# Расшифровываем
decrypted = caesar(encrypted, key, 'decrypt')
print("Расшифровано:", decrypted)
