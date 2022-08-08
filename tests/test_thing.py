import random


class EventSample(object):
    def __init__(self):
        self.__eventhandlersample = []

    def __iadd__(self, Ehandler):
        self.__eventhandlersample.append(Ehandler)
        return self

    def __isub__(self, Ehandler):
        self.__eventhandlersample.remove(Ehandler)
        return self

    def __call__(self, *args, **keywargs):
        for eventhandlersample in self.__eventhandlersample:
            eventhandlersample(*args, **keywargs)


class WeatherStation:
    def __init__(self, station_type=None):
        self.station_type = station_type
        self.station_type.register(WeatherStation.update(self))

    def update(self):
        print(self.station_type.value)


class TempType:
    def __init__(self):
        self.OnEH = EventSample()
        self.type_name = "temp"
        self.value = 0

    def register(self, method):
        self.OnEH += method

    def new_measurement(self):
        self.value = random.randint(10, 20)
        self.OnEH()


def test_correct_greeting():
    weather_station = WeatherStation(TempType())
    exp = TempType().type_name
    actual = weather_station.station_type.type_name
    assert exp == actual


def test_other():
    temp_type = TempType()
    weather_station = WeatherStation(temp_type)
    temp_type.new_measurement()
    assert 1 == 2
