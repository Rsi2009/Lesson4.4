from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


#
class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"


class Bow(Weapon):
    def attack(self):
        return "наносит удар из лука"



# Классы Fighter и Monster
class Fighter:
    def __init__(self, weapon):
        self.weapon = weapon

    def attack(self):
        print(f"Боец {self.weapon.attack()}")

    def changeWeapon(self, weapon):
        self.weapon = weapon


class Monster:
    def __init__(self, health=10):
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print("Монстр побежден!")


def fight(fighter, monster):
    fighter.attack()
    monster.take_damage(5)


# Демонстрация боя
fighter = Fighter(Sword())
monster = Monster()

print("Боец выбирает меч.")
fight(fighter, monster)

fighter.changeWeapon(Bow())
print("Боец выбирает лук.")
fight(fighter, monster)