from app.thing import Thing


class Cell:
    def __init__(self, coordinate, is_alive=False):
        self.isAlive = is_alive
        self.coordinate = coordinate


def test_create_cell_with_coordinated():
    expected_coordinates = (1, 1)
    cell = create_cell(expected_coordinates)
    assert cell.coordinate is expected_coordinates


def test_created_cell_is_death():
    cell = create_cell()
    assert cell.isAlive is False


def test_alive_created_cell_is_alive():
    cell = create_cell(is_alive=True)
    assert cell.isAlive is True


def create_cell(coordinate=(0, 0), is_alive=False):
    cell = Cell(coordinate, is_alive)
    return cell
