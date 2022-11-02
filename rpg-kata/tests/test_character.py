
import pytest
import rpgchar
'''
Iteration Three
Characters have an attack Max Range.

Melee fighters have a range of 2 meters.

Ranged fighters have a range of 20 meters.

Characters must be in range to deal damage to a target.
'''


@pytest.fixture
def rpg_char():
    return rpgchar.RpgChar()


def test_new_char_have_1000_health(rpg_char):
    assert rpg_char.Health == 1000


def test_new_char_has_level_1(rpg_char):
    assert rpg_char.Level == 1


def test_new_char_is_born_alive(rpg_char):
    assert rpg_char.Alive is True


def test_char_can_deal_damage(rpg_char):
    enemy = rpgchar.RpgChar()
    enemy = rpg_char.attack(enemy, 100)
    assert enemy.Health == 1000 - 100


def test_damage_is_subtracted_from_health(rpg_char):
    rpg_char = rpg_char.get_attacked(100)
    assert rpg_char.Health == 1000 - 100


def test_character_health_reduced_to_zero_char_dies(rpg_char):
    rpg_char = rpg_char.get_attacked(1000)
    assert rpg_char.Health == 0
    assert rpg_char.Alive is False


def test_character_health_can_not_fall_beyond_zero(rpg_char):
    rpg_char = rpg_char.get_attacked(10000)
    assert rpg_char.Health == 0


def test_healing_improves_health(rpg_char):
    rpg_char = rpg_char.get_attacked(999)
    rpg_char = rpg_char.healed(100)
    assert rpg_char.Health == 1000 - 999 + 100


def test_dead_character_cannot_be_healed(rpg_char):
    rpg_char = rpg_char.get_attacked(9999)
    rpg_char = rpg_char.healed(100)
    assert rpg_char.Health == 0
    assert rpg_char.Alive is False


def test_character_cannot_be_healed_above_1000_with_full_health(rpg_char):
    rpg_char = rpg_char.healed(100)
    assert rpg_char.Health == 1000


def test_character_cannot_be_healed_above_1000(rpg_char):
    rpg_char = rpg_char.get_attacked(50)
    rpg_char = rpg_char.healed(100)
    assert rpg_char.Health == 1000

# iteration 2


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
