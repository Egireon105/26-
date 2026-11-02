# ============================================================
#  ГИЛЬДИЯ КОТОВ-ПРИКЛЮЧЕНЦЕВ
#  Лабораторная работа №6 — все шаги 1-8 + задания 1*-5*
# ============================================================

# ---------- ИМПОРТЫ ----------
import random   # для кубика
import json     # для сейва в JSON

# ============================================================
# ШАГ 1. СПРАВОЧНИКИ: герои и товары лавки
# ============================================================
heroes = {
    "Мурзик": {"вид": "кот-рыцарь",        "сила": 2, "hp": 20, "золото": 5},
    "Жужа":   {"вид": "сколопендра-бард",  "сила": 1, "hp": 15, "золото": 8},
    "Перо":   {"вид": "голубь-маг",        "сила": 3, "hp": 12, "золото": 3},
}

shop = [
    {"name": "Сарделька",      "price": 10, "heal": 5},
    {"name": "Молоко",         "price": 8,  "heal": 3},
    {"name": "Когтеточка +5",  "price": 25, "power": 2},
]

# ============================================================
# ШАГ 2. КУБИК — функция roll_dice
# ============================================================
def roll_dice(sides=6):
    """Бросает кубик и возвращает число от 1 до sides."""
    return random.randint(1, sides)

# ============================================================
# ШАГ 4. КЛАСС Character + ЗАДАНИЕ 4* (инвентарь)
# ============================================================
class Character:
    """Чертёж любого персонажа игры."""
    def __init__(self, name, view, power, hp, gold):
        self.name    = name
        self.view    = view
        self.power   = power
        self.hp      = hp
        self.max_hp  = hp
        self.gold    = gold
        self.inventory = []          # ★ ЗАДАНИЕ 4*: инвентарь

    def info(self):
        return (f"{self.name} ({self.view}) | Сила: {self.power} "
                f"| HP: {self.hp}/{self.max_hp} | Золото: {self.gold}")

    def heal(self, amount):
        self.hp = min(self.hp + amount, self.max_hp)

    def take_damage(self, dmg):
        self.hp = max(self.hp - dmg, 0)

    # ★ ЗАДАНИЕ 4*: методы инвентаря
    def add_item(self, item_name):
        self.inventory.append(item_name)

    def show_items(self):
        if len(self.inventory) == 0:
            print("Сумка пуста, как желудок у Жужи перед боем.")
        else:
            print("Инвентарь:")
            for item in self.inventory:
                print("-", item)

# ============================================================
# ★ ЗАДАНИЕ 2*: КЛАСС BOSS (наследник Character)
# ============================================================
class Boss(Character):
    """Босс получает только ПОЛОВИНУ урона."""
    def take_damage(self, dmg):
        super().take_damage(dmg // 2)

# ============================================================
# ШАГ 3. СОЗДАНИЕ ГЕРОЯ — функция create_hero
# ============================================================
def create_hero():
    """Спрашивает имя и роль, возвращает готового героя."""
    while True:
        name = input("Как зовут героя? (Мурзик, Жужа, Перо): ").strip()
        if name in heroes:
            break
        print("Такого героя нет в приюте. Попробуйте ещё раз.")

    role = input("Кем будешь: рыцарь, маг или вор? ").strip().lower()
    base = heroes[name]
    power = base["сила"]

    if role == "рыцарь":
        power = power + 4
    elif role == "маг":
        power = power + 3
    else:
        power = power + 2

    hp = base["hp"] + power
    hero = Character(name, base["вид"], power, hp, base["золото"])
    return hero

# ============================================================
# ★ ЗАДАНИЕ 1*: ФУНКЦИЯ STEAL (воровство Жужи)
# ============================================================
def steal(victim):
    """Крадёт у жертвы от 1 до 5 золота, но не больше, чем есть."""
    k = roll_dice(5)
    stolen = min(k, victim.gold)
    victim.gold = victim.gold - stolen
    return stolen

# ============================================================
# ШАГ 5. БОЙ — функция battle (+ вызов steal для Жужи)
# ============================================================
def battle(hero, enemy):
    """Бой по очереди ударов до нулевого HP."""
    print(f"\nБОЙ: {hero.name} против {enemy.name}!")

    # ★ ЗАДАНИЕ 1*: Жужа ворует золото ДО боя
    if hero.name == "Жужа":
        stolen = steal(enemy)
        if stolen > 0:
            print(f"Жужа украла {stolen} золота перед боем!")
            hero.gold += stolen
        else:
            print("У врага не оказалось золота для кражи.")

    while hero.hp > 0 and enemy.hp > 0:
        k = roll_dice()
        dmg = hero.power + k
        enemy.take_damage(dmg)
        print(f"{hero.name} бьёт на {dmg}! У врага {enemy.hp} HP")

        if enemy.hp == 0:
            print(f"{enemy.name} повержен! Добыча: {enemy.gold} золота")
            hero.gold = hero.gold + enemy.gold
            return True

        k = roll_dice()
        dmg = enemy.power + k
        hero.take_damage(dmg)
        print(f"{enemy.name} бьёт в ответ на {dmg}! У тебя {hero.hp} HP")

        if hero.hp == 0:
            print("Ты повержен... Возвращайся в приют и лечись.")
            return False

# ============================================================
# ШАГ 6. ЛАВКА — функция buy_item (+ инвентарь из 4*)
# ============================================================
def buy_item(hero):
    """Показывает лавку и продаёт выбранный товар."""
    print("\n--- Лавка приюта ---")
    for i, item in enumerate(shop):
        print(f"{i + 1}. {item['name']} — {item['price']} золота")

    while True:
        try:
            choice = int(input("Что покупаем? Введи номер (0 — отмена): "))
            if choice == 0:
                return
            item = shop[choice - 1]
            break
        except (ValueError, IndexError):
            print("Неверный номер товара. Попробуйте ещё раз.")

    if hero.gold < item["price"]:
        print("Не хватает золота, приятель!")
        return

    hero.gold = hero.gold - item["price"]
    if "heal" in item:
        hero.heal(item["heal"])
    if "power" in item:
        hero.power = hero.power + item["power"]

    # ★ ЗАДАНИЕ 4*: купленный предмет попадает в инвентарь
    hero.add_item(item["name"])
    print(f"Куплено: {item['name']}! Золота осталось: {hero.gold}")

# ============================================================
# ★ ЗАДАНИЕ 3*:
# ============================================================
def report():
    """Печатает таблицу героев и среднюю силу."""
    print(f"\n{'Имя':<10}{'Сила':>6}{'Золото':>8}")
    total = 0
    for name, card in heroes.items():
        print(f"{name:<10}{card['сила']:>6}{card['золото']:>8}")
        total = total + card["сила"]
    average = round(total / len(heroes), 1)
    print(f"Средняя сила: {average}")
def save_game(hero):
    """Записывает свойства героя в файл save.json."""
    save = {
        "name":      hero.name,
        "вид":       hero.view,
        "hp":        hero.hp,
        "max_hp":    hero.max_hp,
        "power":     hero.power,
        "gold":      hero.gold,
        "inventory": hero.inventory,
    }
    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(save, f, ensure_ascii=False)

def load_game():
    """Читает save.json и возвращает героя из сейва."""
    try:
        with open("save.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        hero = Character(data["name"], data["вид"], data["power"],
                         data["max_hp"], data["gold"])
        hero.hp = data["hp"]
        hero.inventory = data.get("inventory", [])
        print(f"Прогресс загружен: {hero.name}")
        return hero
    except FileNotFoundError:
        print("Сейв не найден. Создаём нового героя.")
        return create_hero()
    except Exception as e:
        print(f"Ошибка загрузки сейва: {e}. Создаём нового героя.")
        return create_hero()
def menu_loop(hero):
    while True:
        print("\n===== ГИЛЬДИЯ КОТОВ =====")
        print("1 — Карточка героя")
        print("2 — В подземелье (бой)")
        print("3 — Лавка приюта")
        print("4 — Бой с боссом ★")
        print("5 — Инвентарь ★")
        print("6 — Сводка по приюту ★")
        print("0 — Выйти из игры")
        choice = input("Твой выбор: ").strip()

        if choice == "1":
            print(hero.info())
        elif choice == "2":
            golem = Character("Пыльный голем", "пыльный голем", 4, 20, 12)
            battle(hero, golem)
        elif choice == "3":
            buy_item(hero)
        elif choice == "4":
            boss = Boss("Сколопендриха-матриарх", "сколопендриха", 5, 30, 25)
            battle(hero, boss)
        elif choice == "5":
            hero.show_items()
        elif choice == "6":
            report()
        elif choice == "0":
            save_game(hero)
            print("Прогресс сохранён. До встречи в приюте!")
            break
        else:
            print("Нет такого пункта, попробуй ещё раз!")

if __name__ == "__main__":
    hero = load_game()
    menu_loop(hero)