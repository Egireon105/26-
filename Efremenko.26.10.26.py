#==============================================================================
#                           Задание №1
#==============================================================================

def back_flash(base, bonus):
    result = base * bonus
    return result

print(back_flash(120, 2.5))

#==============================================================================
#                           Задание №2
#==============================================================================

def count_word(text, word):
    return text.lower().count(word.lower())
text = "Проклятие сидит в этом здании. Проклятие в каждом этаже. Это проклятие особое."
word = "проклятие"

print("Отчёт:", text)
print(f"Слово «{word}» встречается: {count_word(text, word)} раз(а)")
print("Слов в отчёте:", len(text.split()))

#==============================================================================
#                           Задание №3
#==============================================================================
items =[
    {"name": "Клык Пустого", "price":4200},
    {"name": "Зеркало ранга", "price":3600},
    {"name": "Печать Року", "price":2800}
]

sort = sorted(items, key=lambda item: item["price"], reverse=True)
print("Топ 3 артифакта Аукциона: ")
for i, item in enumerate(items[:3], start=1):
    print(f"{i}) {item['name']} — {item['price']}")
    
sum = sum([item["price"] for item in items])
print("Общая сумма", sum)

#==============================================================================
#                           Задание №4
#==============================================================================

weights = [15, 3, 8, 12, 5, 2]

def total_weight(weights):
    return sum(weights)

def light_items(weights, limit):
    return [w for w in weights if w <= limit]

# Вывод результатов
print("Общий вес рюкзака:", total_weight(weights))
print("Лёгкие предметы (до 10):", light_items(weights, 10))
print("Средний вес предмета:", round(total_weight(weights) / len(weights), 1))
