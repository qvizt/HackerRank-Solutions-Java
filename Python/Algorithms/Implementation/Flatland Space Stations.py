# Solution for Flatland Space Stations


def maximum_distance(cities, stations):
    stations.sort()
    # covering the left- / rightmost city - important especially if
    # there is only one station because the max distance is then either
    # the leftmost city or the rightmost city.
    max_distance = max(abs(0 - stations[0]),
                       abs(cities - 1 - stations[len(stations) - 1]))

    for i in range(0, len(stations) - 1):
        left_station, right_station = stations[i], stations[i + 1]
        distance_station_to_station = right_station - left_station
        max_distance_to_a_city = distance_station_to_station // 2
        max_distance = max(max_distance, max_distance_to_a_city)

    return max_distance


if __name__ == '__main__':
    cities, m = map(int, input().split())  # m is not required
    space_stations = list(map(int, input().split()))
    result = maximum_distance(cities, space_stations)
    print(result)
