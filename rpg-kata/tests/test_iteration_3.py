
import pytest
import rpgchar
'''
## Iteration Three ##

1. Characters have an attack Max Range.

1. *Melee* fighters have a range of 2 meters.

1. *Ranged* fighters have a range of 20 meters.

1. Characters must be in range to deal damage to a target.
'''


@pytest.fixture
def rpg_char():
    return rpgchar.RpgChar()


def test_character_cannot_attack_itself(rpg_char):
    char = rpgchar.RpgChar()
    assert False

