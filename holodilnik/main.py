import datetime
from decimal import Decimal

goods = {
    'Пельмени Универсальные': [
        {'amount': Decimal('0.5'), 'expiration_date':
            datetime.date(2023, 7, 15)},
        {'amount': Decimal('2'), 'expiration_date':
            datetime.date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date':
            None}
    ],
}


def add(items, title, amount, expiration_date=None):
    # Если такого продукта еще нет, создаем для него пустой список
    if title not in items:
        items[title] = []

    real_date = None
    if expiration_date is not None:
        real_date = datetime.datetime.strptime(expiration_date, '%Y-%m-%d').date()

    # Создаем словарь партии и добавляем его в список
    new_batch = {
        'amount': amount,
        'expiration_date': real_date
    }
    items[title].append(new_batch)




def add_by_note(items, note):
    # Разделяем строку справа налево, максимум на 3 части
    parts = note.rsplit(maxsplit=2)

    # Проверяем, есть ли дата в конце строки (в формате ГГГГ-ММ-ДД)
    # Если дата есть, длина списка будет 3
    if len(parts) == 3 and '-' in parts[-1]:
        title = parts[0]
        amount = Decimal(parts[1])
        # Превращаем строку даты в объект date
        expiration_date = datetime.datetime.strptime(parts[2], '%Y-%m-%d').date()
    else:
        # Если даты нет, длина списка будет 2
        title = parts[0]
        amount = Decimal(parts[1])
        expiration_date = None

    # Если такого продукта еще нет, создаем для него пустой список
    if title not in items:
        items[title] = []

    # Создаем словарь партии и добавляем его в список
    new_batch = {
        'amount': amount,
        'expiration_date': expiration_date
    }
    items[title].append(new_batch)


def amount(items, needle):
    needle_lower = needle.lower()
    total_amount = Decimal('0')

    # Проходим по всем продуктам в словаре
    for title, batches in items.items():
        if needle_lower in title.lower():
            # Проходим по всем партиям этого продукта и суммируем количество
            for batch in batches:
                total_amount += batch['amount']

    # Возвращаем итоговую сумму
    return total_amount


def find(items, needle):
    # 1. Готовим пустой список, куда будем складывать найденные названия
    found_titles = []

    # 2. Переводим поисковый запрос в нижний регистр (маленькие буквы)
    needle_lower = needle.lower()

    # 3. Перебираем все названия (title) в нашем словаре-холодильнике
    for title in items:
        # 4. Если запрос есть в названии (тоже переведенном в нижний регистр)...
        if needle_lower in title.lower():
            # 5. ...то добавляем это название в наш список
            found_titles.append(title)

    # 6. Возвращаем собранный список
    return found_titles

# 1. Проверяем функцию add
add(goods, 'Молоко', Decimal('1.5'))
add(goods, 'Яйца', Decimal('10'), '2023-10-15')
print("В холодильнике:", goods)

#2. Проверяем функцию add_by_note
add_by_note(goods, 'Яйца гусиные 4 2023-07-15')
add_by_note(goods, 'Хлеб Бородинский 1 2023-10-20')
add_by_note(goods, 'Вода 2')
print("В холодильнике:", goods)

#3. Проверяем функцию amount (вес)
print(f"Сколько всего яиц (яйца + гусиные)? {amount(goods, 'яйца')} шт.")
print(f"Сколько воды? {amount(goods, 'вода')} л.")
print(f"Сколько мяса (его нет)? {amount(goods, 'мясо')}")

# 4. Проверяем функцию find (поиск названий)
print(f"Ищем 'яйца': {find(goods, 'яйца')}")
print(f"Ищем 'хлеб': {find(goods, 'хлеб')}")
print(f"Ищем 'сыр': {find(goods, 'сыр')}")