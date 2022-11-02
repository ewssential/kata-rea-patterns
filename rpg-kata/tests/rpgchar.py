

class RpgChar:
    def __init__(self, level=1, health=1000, alive=True):
        self.Health = health
        self.Level = level
        self.Alive = alive

    def attack(self, enemy, damage):
        if enemy is self:
            return self
        return self.calculate_attack(damage, enemy)

    def calculate_attack(self, damage, enemy):
        if enemy.Level - self.Level >= 5:
            damage //= 2
        if self.Level - enemy.Level >= 5:
            damage = int(damage * 1.5)
        return enemy.get_attacked(damage)

    def get_attacked(self, damage):
        return self.__suffer_damage(damage)

    def __suffer_damage(self, damage):
        health = self.Health - damage
        alive = True
        if health <= 0:
            health = 0
            alive = False
        return RpgChar(self.Level, health, alive)

    def healed(self, healing):
        if not self.Alive:
            return self
        return self.__heal(healing)

    def __heal(self, healing):
        health = self.Health + healing
        if health > 1000:
            health = 1000
        return RpgChar(self.Level, health, self.Alive)

    def level_up(self):
        level = self.Level + 1
        return RpgChar(level, self.Health, self.Alive)
