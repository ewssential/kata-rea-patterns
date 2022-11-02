
import pytest
import rpgchar
'''
## Iteration Two ##

1. A Character cannot Deal Damage to itself.

1. A Character can only Heal itself.

1. When dealing damage:
    - If the target is 5 or more Levels above the attacker, Damage is reduced by 50%
    - If the target is 5 or more Levels below the attacker, Damage is increased by 50%

'''


@pytest.fixture
def rpg_char():
    return rpgchar.RpgChar()


def test_character_cannot_attack_itself(rpg_char):
    rpg_char = rpg_char.attack(rpg_char, 50)
    assert rpg_char.Health == 1000


def test_character_can_increase_level(rpg_char):
    rpg_char = rpg_char.level_up()
    assert rpg_char.Level == 2

    rpg_char = rpg_char.level_up()
    assert rpg_char.Level == 3


def test_target_is_5_or_more_levels_above_the_attacker_damage_is_halved(rpg_char):
    target = rpgchar.RpgChar(level=6)
    target = rpg_char.attack(target, 100)
    assert target.Health == 1000 - 100 // 2


def test_target_is_5_or_more_levels_above_the_attacker_odd_damage_is_working(rpg_char):
    target = rpgchar.RpgChar(level=6)
    target = rpg_char.attack(target, 99)
    assert target.Health == 1000 - 99 // 2


def test_target_is_5_or_more_levels_below_the_attacker_then_damage_is_50_percent_increased(rpg_char):
    attacker = rpgchar.RpgChar(level=6)
    rpg_char = attacker.attack(rpg_char, 100)
    assert rpg_char.Health == 1000 - int(100 * 1.5)


def test_target_is_5_or_more_levels_below_the_attacker_then_odd_damage_is_working(rpg_char):
    attacker = rpgchar.RpgChar(level=6)
    rpg_char = attacker.attack(rpg_char, 99)
    assert rpg_char.Health == 1000 - int(99 * 1.5)
