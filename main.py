class Hero:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def fight(self, enemy):
        enemy.health -= self.power
print(5)
print(1)
print(2)
print(3)
print(4)
print(1)


knight = Hero('Вася', 100, 10)
print(knight.name)

knight2 = Hero('Петя', 120, 5)
knight.fight(knight2)
print(knight2.health)
