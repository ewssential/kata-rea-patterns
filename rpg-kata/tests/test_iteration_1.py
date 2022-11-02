
import pytest
import rpgchar
'''
## Iteration One ##

1. All Characters, when created, have:
    - Health, starting at 1000
    - Level, starting at 1
    - May be Alive or Dead, starting Alive (Alive may be a true/false)

1. Characters can Deal Damage to Characters.
    - Damage is subtracted from Health
    - When damage received exceeds current Health, Health becomes 0 and the character dies

1. A Character can Heal a Character.
    - Dead characters cannot be healed
    - Healing cannot raise health above 1000
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

