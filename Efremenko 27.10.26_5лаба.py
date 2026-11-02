import random

# ================= ЗАДАНИЕ 1 =================
print("--- Задание 1: Техника Чёрной вспышки ---")

def black_flash(damage):
    return damage * 1.5

first = black_flash(100)
second = black_flash(first)

print(f"Урон после первой вспышки: {first}")
print(f"После второй вспышки: {second}")

print("\n")


# ================= ЗАДАНИЕ 2 =================
print("--- Задание 2: Проверка ранга мага ---")

def is_rank_ok(rank):
    ranks = ["S", "A", "B", "C", "D"]
    return rank in ranks

rank_input = input("Ранг? ")
result = is_rank_ok(rank_input)
print(f"Ранг допустим: {result}")
print(f"Тип результата: {type(result)}")

print("\n")


# ================= ЗАДАНИЕ 3 =================
print("--- Задание 3: Приветствие с запасным значением ---")

def greet(name, greeting="Привет"):
    return f"{greeting}, {name}!"

user_name = input("Имя? ")
print(greet(user_name))
print(greet(user_name, "Салют"))

print("\n")


# ================= ЗАДАНИЕ 4 =================
print("--- Задание 4: Функция-статистик ---")

def stats(numbers):
    lo = min(numbers)
    hi = max(numbers)
    avg = round(sum(numbers) / len(numbers), 1)
    return lo, hi, avg

nums = [5, 20, 12, 13]
lo, hi, avg = stats(nums)

print(f"Список: {nums}")
print(f"Минимум: {lo}")
print(f"Максимум: {hi}")
print(f"Среднее: {avg}")

print("\n")


# ================= ЗАДАНИЕ 5 =================
print("--- Задание 5: Класс Player ---")

class Player:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp
    
    def info(self):
        print(f"{self.name}: {self.level} уровень, {self.hp} HP")

p1 = Player("Итадори", 1, 100)
p2 = Player("Мегуми", 2, 85)

p1.info()
p2.info()

print("\n")


# ================= ЗАДАНИЕ 6 =================
print("--- Задание 6: Класс Potion ---")

class Potion:
    def __init__(self, power):
        self.power = power
    
    def apply(self, player):
        player.hp = min(100, player.hp + self.power)

hero = Player("Итадори", 1, 70)
potion = Potion(50)

print(f"HP до лечения: {hero.hp}")
print("Применяем зелье (+50)...")
potion.apply(hero)
print(f"HP после лечения: {hero.hp}")

print("\n")


# ================= ЗАДАНИЕ 7 =================
print("--- Задание 7: Класс Enemy ---")

class Enemy:
    def __init__(self, hp):
        self.hp = hp
    
    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)
    
    def is_defeated(self):
        return self.hp == 0

enemy = Enemy(50)
print(f"HP врага: {enemy.hp}")

print("Удар на 30!", end=" ")
enemy.take_damage(30)
print(f"HP врага: {enemy.hp}. Побеждён: {enemy.is_defeated()}")

print("Удар на 25!", end=" ")
enemy.take_damage(25)
print(f"HP врага: {enemy.hp}. Побеждён: {enemy.is_defeated()}")

print("\n")


# ================= ЗАДАНИЕ 8 =================
print("--- Задание 8: BlackFlashCounter ---")

class BlackFlashCounter:
    def __init__(self):
        self.count = 0
    
    def hit(self):
        self.count += 1
    
    def reset(self):
        self.count = 0
    
    def show(self):
        print(f"Чёрных вспышек: {self.count}")

counter = BlackFlashCounter()
counter.hit()
counter.hit()
counter.hit()
counter.show()

print("Сброс...")
counter.reset()
counter.show()

print("\n")


# ================= ЗАДАНИЕ 1* =================
print("--- Задание 1*: Класс Boss ---")

class Boss(Enemy):
    def __init__(self, name, hp):
        super().__init__(hp)
        self.name = name
    
    def take_damage(self, damage):
        real_damage = damage // 2
        self.hp = max(0, self.hp - real_damage)
        print(f"Босс получил {real_damage}.", end=" ")

boss = Boss("Пустой", 200)
print(f"Босс «{boss.name}»: {boss.hp} HP")

print("Удар на 75!", end=" ")
boss.take_damage(75)
print(f"HP: {boss.hp}")

print("Удар на 65!", end=" ")
boss.take_damage(65)
print(f"HP: {boss.hp}")

print("\n")


# ================= ЗАДАНИЕ 2* =================
print("--- Задание 2*: Класс Shop ---")

class Shop:
    def __init__(self):
        self.money = 1000
        self.items = [
            {"name": "Зелье лечения", "price": 250},
            {"name": "Меч тени", "price": 500},
            {"name": "Свиток", "price": 100}
        ]
    
    def buy(self, name):
        for item in self.items:
            if item["name"] == name:
                if self.money >= item["price"]:
                    self.money -= item["price"]
                    print(f"Купили «{name}» за {item['price']}. Осталось денег: {self.money}")
                else:
                    print("Недостаточно денег")
                return
        print("Такого товара нет")

shop = Shop()
shop.buy("Зелье лечения")
shop.buy("Броня")
shop.buy("Меч тени")

print("\n")


# ================= ЗАДАНИЕ 3* =================
print("--- Задание 3*: Арена ---")

class Fighter:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

fighter1 = Fighter("Итадори", 100)
fighter2 = Fighter("Годжо", 100)

round_num = 1
turn = 1

while fighter1.hp > 0 and fighter2.hp > 0:
    damage = random.randint(10, 30)
    if turn == 1:
        fighter2.hp = max(0, fighter2.hp - damage)
        print(f"Раунд {round_num}: {fighter1.name} бьёт на {damage} → у {fighter2.name} {fighter2.hp} HP")
        turn = 2
    else:
        fighter1.hp = max(0, fighter1.hp - damage)
        print(f"Раунд {round_num}: {fighter2.name} бьёт на {damage} → у {fighter1.name} {fighter1.hp} HP")
        turn = 1
        round_num += 1

if fighter1.hp > 0:
    print(f"Победитель: {fighter1.name}!")
else:
    print(f"Победитель: {fighter2.name}!")

print("\n")


# ================= ЗАДАНИЕ 4* =================
print("--- Задание 4*: Кошелёк игрока ---")

class Wallet:
    def __init__(self, money):
        self.money = money
    
    def add(self, amount):
        self.money += amount
    
    def spend(self, amount):
        if self.money >= amount:
            self.money -= amount
            return True
        return False

wallet = Wallet(500)
print(f"Кошелёк: {wallet.money}")

if wallet.spend(300):
    print(f"Купили за 300. Осталось: {wallet.money}")

result = wallet.spend(999)
print(f"Покупка на 999? Недостаточно денег: {result}")

print("\n")


# ================= ЗАДАНИЕ 5* =================
print("--- Задание 5*: Экзамен Пустого ---")

def double(x):
    return x * 2
y = double(5) + 1
print(f"Фрагмент 1: {y}")

class Enemy2:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

e = Enemy2("Слабый враг", 50)
print(f"Фрагмент 2: {e.name}, {e.hp} HP")

class Player2:
    def __init__(self, name):
        self.name = name
    
    def info(self):
        print(self.name)

p = Player2("Мегуми")
print("Фрагмент 3:", end=" ")
p.info()

card = {"hp": 100}
card["hp"] = 90
print(f"Фрагмент 4: {card['hp']}")

class Counter:
    def __init__(self):
        self.count = 0
    
    def hit(self):
        self.count = self.count + 1

c = Counter()
c.hit()
c.hit()
print(f"Фрагмент 5: {c.count}")