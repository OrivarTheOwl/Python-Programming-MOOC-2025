class WeatherStation:
    def __init__(self, name: str):
        self.__name = name
        self.__list = []
        self.__counter = 0

    def add_observation(self, observation: str):
        self.__list.append(observation)
        self.__counter += 1

    def latest_observation(self):
        if len(self.__list) == 0:
            return ""
        else:
            return self.__list[-1]

    def number_of_observations(self):
        return self.__counter

    def __str__(self):
        return f"{self.__name}, {self.number_of_observations()} observations"



if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)