# Задание 1

a = int(input("Уровень энергии? "))

if a >= 1000:
    print("Специальный уровень! Годжо впечатлён")
elif a >= 100:
    print("Маг-новичок")
else:
    print("Мугл... то есть обычный человек")
    
# Задание 2

damage = int(input("Урон? "))
hp = int(input("HP врага? "))

if damage >= hp:
    print("СМЕРТЕЛЬНЫЙ УДАР! Враг повержен")
else:
    print(f"Враг выжил, у него осталось {hp - damage} HP")

# Задание 3

score = int(input("Очки? "))

if score >= 90:
    print("Ранг: S")
elif score >= 75:
    print("Ранг: A")
elif score >= 60:
    print("Ранг: B")
elif score >= 40:
    print("Ранг: C")
else:
    print("Ранг: D")
    
# Задание 4

n = 10
while n > 0:
    print(f"Обратный отсчёт: {n}")
    n = n - 1
print("ПУСК! ПРОКЛЯТАЯ ТЕХНИКА ГОТОВА!")

print("---")

# Задание 5

secret = 42
attempts = 0
guess = 0

while guess != secret:
    guess = int(input("Твоя догадка? "))
    attempts = attempts + 1
    
    if guess < secret:
        print("Больше!")
    elif guess > secret:
        print("Меньше!")
    else:
        print("Годжо аплодирует стоя!")

print(f"Попыток потрачено: {attempts}")

# Задание 6

n = int(input("Сколько повторений? "))

if n == 0:
    print("Лентяй! Ни одного повторения")
else:
    for i in range(1, n + 1):
        print(f"Отжимание № {i}")
    print(f"Готово! Сделано повторений: {n}")
    
# Задание 7

loot = ["меч", "зелье", "шлем", "зелье", "карта", "зелье"]
count = 0
i = 0
long_items = []

for item in loot:
    i = i + 1
    print(f"{i}) {item}")
    
    if item == "зелье":
        count = count + 1
        
    if len(item) > 4:
        long_items.append(item)

print(f"Зелий в луте: {count}")
print("Длинные предметы:", ", ".join(long_items))

# Задание 8

password = "gojo123"
tries = 0

while tries < 3:
    text = input("Пароль? ")
    
    if text == password:
        print("Добро пожаловать в Магический техникум!")
        break
    else:
        tries = tries + 1
        print(f"Неверный пароль. Осталось попыток: {3 - tries}")

if tries == 3:
    print("Аккаунт заблокирован. Годжо огорчён")

# Задание 1 *

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("мега-база")
    elif i % 3 == 0:
        print("кринж")
    elif i % 5 == 0:
        print("база")
    else:
        print(i)

# Задание 2 *

height = int(input("Высота? "))

print("Обычная пирамида:")
for i in range(1, height + 1):
    print("*" * i)

print("Пирамида-ёлочка:")
for i in range(1, height + 1):
    spaces = " " * (height - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
    
# Задание 3 *

code = int(input("Код? "))
n = code
sum_digits = 0
even_count = 0

while n > 0:
    digit = n % 10
    sum_digits = sum_digits + digit
    
    if digit % 2 == 0:
        even_count = even_count + 1
        
    n = n // 10

print(f"Сумма цифр: {sum_digits}")
print(f"Чётных цифр: {even_count}")

# Задание 4 *

print(f"{'Уровень':>8}{'XP':>10}")
total_xp = 0

for level in range(1, 11):
    xp = 100 * level
    total_xp = total_xp + xp
    print(f"{level:>8}{xp:>10}")

print(f"Суммарный XP: {total_xp}")

# Задание 5 *

hp = 100
energy = 50

while True:
    command = input("Команда? ")
    
    if command == "статус":
        print(f"HP: {hp}, Энергия: {energy}")
        
    elif command == "тренировка":
        n = int(input("Сколько отжиманий? "))
        bonus = 0
        
        for i in range(n // 10):
            bonus = bonus + 5
            
        energy = energy + bonus
        print(f"+{bonus} к энергии!")
        
    elif command == "выход":
        print("Сессия завершена")
        break
        
    else:
        print("Неизвестная команда")
