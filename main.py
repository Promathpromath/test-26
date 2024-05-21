class Hero:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def fight(self, enemy):
        enemy.health -= self.power
print(1)
print(2)


knight = Hero('Вася', 100, 10)
print(knight.name)

knight2 = Hero('Петя', 120, 5)
knight.fight(knight2)
print(knight2.health)