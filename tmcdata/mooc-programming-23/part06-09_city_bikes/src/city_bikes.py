
import math

# ------------------------------------------------------------ GET STATION DATA ---------------------------------------

'''
First, write a function named get_station_data(filename: str). 
This function should read the names and locations of all the stations in the file, and return them in a dictionary with the following format:

{
  "Kaivopuisto: (24.950292890004903, 60.155444793742276),
  "Laivasillankatu: (24.956347471358754, 60.160959093887129),
  "Kapteeninpuistikko: (24.944927399779715, 60.158189199971673)
}

Dictionary keys are the names of the stations, and the value attached is a tuple containing the location coordinates of the station. 
The first element in the tuple is the Longitude field, and the second is the Latitude field.
'''

def get_station_data(filename: str):

    stations = {} # the dictionary to store the information 

    # open and read file, store the information in a list

    with open(filename) as new_file:
        for line in new_file:
            parts = line.split(";")

            if parts[0] == "Longitude": # to ignore the first line (titles)
                continue

            stations[str(parts[3])] = (float(parts[0]), float(parts[1]))
    
    return stations

# ---------------------------------------------------------------- DISTANCE ---------------------------------------
'''
Next, write a function named distance(stations: dict, station1: str, station2: str), which returns the distance between the two stations given as arguments.

The distance is calculated using the Pythagorean theorem. 
The multiplication factors below are approximate values for converting latitudes and longitudes to distances in kilometres in the Helsinki region.

x_km = (longitude1 - longitude2) * 55.26
y_km = (latitude1 - latitude2) * 111.2
distance_km = math.sqrt(x_km**2 + y_km**2)

'''
    

def distance(stations: dict, station1: str, station2: str):
    
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

# ---------------------------------------------------------------- GREATEST DISTANCE ---------------------------------------
'''
Please write a function named greatest_distance(stations: dict), which works out the two stations on the list with the greatest distance from each other. 
The function should return a tuple, where the first two elements are the names of the two stations, and the third element is the distance between the two.

stations = get_station_data('stations1.csv')
station1, station2, greatest = greatest_distance(stations)
print(station1, station2, greatest)

Sample output:
Laivasillankatu Hietalahdentori 1.478708873076181
'''

def greatest_distance(stations: dict):
    
    # To run all the possible combinations of stations

    import itertools
    possible_combinations = []

    for L in range(len(stations) + 1):
        for subset in itertools.combinations(stations, L):
            if len(subset) == 2:
                possible_combinations.append(subset)
    
    # store the distances between stations in a list of tuples

    distances_combinations = []
    for combination in possible_combinations:
        distances_combinations.append(distance(stations, combination[0], combination[1]))

    # find the max distance and index, to print
    
    index = distances_combinations.index(max(distances_combinations))
    
    return (possible_combinations[index][0], possible_combinations[index][1], distances_combinations[index])


if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
    
    
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)