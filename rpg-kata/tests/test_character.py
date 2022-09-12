import pytest

from app.thing import Thing

'''
x. A Character cannot Deal Damage to itself.

0. A Character can Heal a Character.
1. A Character can only Heal itself.

1. When dealing damage:
    - If the target is 5 or more Levels above the attacker, Damage is reduced by 50%
    - If the target is 5 or more Levels below the attacker, Damage is increased by 50%

'''


class RpgChar:
    def __init__(self):
        self.Health = 1000
        self.Level = 1
        self.Alive = True

    def attack(self, enemy, damage):
        if enemy is self:
            return
        enemy.get_attacked(damage)
        return enemy

    def get_attacked(self, damage):
        self.__suffer_damage(damage)

    def __suffer_damage(self, damage):
        self.Health -= damage
        if self.Health <= 0:
            self.Health = 0
            self.Alive = False

    def get_healed(self, healing):
        if not self.Alive:
            return
        self.__heal(healing)

    def __heal(self, healing):
        self.Health += healing
        if self.Health > 1000:
            self.Health = 1000


@pytest.fixture
def rpg_char():
    return RpgChar()


def test_new_char_have_1000_health(rpg_char):
    assert rpg_char.Health == 1000


def test_new_char_has_level_1(rpg_char):
    assert rpg_char.Level == 1


def test_new_char_is_born_alive(rpg_char):
    assert rpg_char.Alive is True


def test_char_can_deal_damage(rpg_char):
    enemy = RpgChar()
    enemy = rpg_char.attack(enemy, 100)
    assert enemy.Health == 1000 - 100


def test_damage_is_subtracted_from_health(rpg_char):
    rpg_char.get_attacked(100)
    assert rpg_char.Health == 1000 - 100


def test_character_health_reduced_to_zero_char_dies(rpg_char):
    rpg_char.get_attacked(1000)
    assert rpg_char.Health == 0
    assert rpg_char.Alive is False


def test_character_health_can_not_fall_beyond_zero(rpg_char):
    rpg_char.get_attacked(10000)
    assert rpg_char.Health == 0


def test_healing_improves_health(rpg_char):
    rpg_char.get_attacked(999)
    rpg_char.get_healed(100)
    assert rpg_char.Health == 1000 - 999 + 100


def test_dead_character_cannot_be_healed(rpg_char):
    rpg_char.get_attacked(9999)
    rpg_char.get_healed(100)
    assert rpg_char.Health == 0
    assert rpg_char.Alive is False


def test_character_cannot_be_healed_above_1000(rpg_char):
    rpg_char.get_healed(100)
    assert rpg_char.Health == 1000


def test_character_cannot_be_healed_above_1000(rpg_char):
    rpg_char.get_attacked(50)
    rpg_char.get_healed(100)
    assert rpg_char.Health == 1000


def test_character_cannot_attack_itself(rpg_char):
    rpg_char.attack(rpg_char, 50)
    assert rpg_char.Health == 1000
