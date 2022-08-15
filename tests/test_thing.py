from app.thing import Thing


class Cell:
    def __init__(self):
        self.isAlive = False
        self.coordinate = (0, 0)


def test_create_cell_with_coordinated():
    cell = Cell()
    assert cell.coordinate is (0, 0)


def test_created_cell_is_death():
    cell = Cell()
    assert cell.isAlive is False
