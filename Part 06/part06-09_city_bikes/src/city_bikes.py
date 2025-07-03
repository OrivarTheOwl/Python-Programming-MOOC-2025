import math


def get_station_data(filename: str):
    station_info = {}
    with open(filename) as new_file:
        for line in new_file:
            parts = line.split(";")
            if parts[0] == "Longitude":
                continue
            station_info[parts[3]] = (float(parts[0]), float(parts[1]))

    return station_info

def distance(stations: dict, station1: str, station2: str):
    longitude1 = stations[station1][0]
    longitude2 = stations[station2][0]
    latitude1 = stations[station1][1]
    latitude2 = stations[station2][1]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km



def greatest_distance(stations: dict):
    station_names = []
    comparison_stations = []

    for station in stations:
        station_names.append(station)
    for station in station_names:
        comparison_stations.append(station)


    greatest_station1 = ""
    greatest_station2 = ""
    greatest_num = 0

    for station in station_names:
        for compare in comparison_stations:
            temp_num = distance(stations, station, compare)

            if temp_num > greatest_num:
                greatest_num = temp_num
                greatest_station1 = station
                greatest_station2 = compare

    return greatest_station1, greatest_station2, greatest_num



if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)