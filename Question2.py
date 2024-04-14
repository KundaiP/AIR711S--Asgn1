import random

# Define the city names
cities = ['Khomasdal', 'Eros', 'Katutura', 'Dorado', 'Klein Windhoek']


def generateRandomRoute():
    return random.sample(range(len(cities)), len(cities))


def routeLength(tsp, route):
    length = 0
    for i in range(len(route)):
        length += tsp[route[i - 1]][route[i]]
    return length


def totalDistance(tsp, route):
    distances = []
    total_length = 0
    for i in range(len(route)):
        from_city = route[i - 1]
        to_city = route[i]
        distance = tsp[from_city][to_city]
        distances.append((cities[from_city], cities[to_city], distance))
        total_length += distance
    return total_length, distances


def exploreNeighbours(current_route):
    neighbours = []
    for i in range(len(current_route)):
        for j in range(i + 1, len(current_route)):
            neighbour = current_route[:]
            neighbour[i], neighbour[j] = neighbour[j], neighbour[i]  # Swap two cities
            neighbours.append(neighbour)
    return neighbours


def hillClimbing(tsp):
    current_route = generateRandomRoute()
    current_route_length = routeLength(tsp, current_route)
    neighbours = exploreNeighbours(current_route)
    best_neighbour, best_neighbour_length = min((neighbour, routeLength(tsp, neighbour)) for neighbour in neighbours)

    while best_neighbour_length < current_route_length:
        current_route = best_neighbour
        current_route_length = best_neighbour_length
        neighbours = exploreNeighbours(current_route)
        best_neighbour, best_neighbour_length = min(
            (neighbour, routeLength(tsp, neighbour)) for neighbour in neighbours)

    return current_route


def visualizeRoutes(tsp, routes):
    print("City Map:")
    for city in cities:
        print(city, end=" ")
    print()
    print("-" * (len(cities) * 2 - 1))

    for i, route in enumerate(routes):
        print(f"Route {i + 1}: ", end="")
        for j in range(len(cities)):
            print("|", end="")
            if j in route:
                print("X", end="")
            else:
                print(" ", end="")
        print("|")


def main():
    tsp = [
        [0, 7, 20, 15, 12],
        [10, 0, 6, 14, 18],
        [20, 6, 0, 15, 30],
        [15, 14, 25, 0, 2],
        [12, 18, 30, 2, 0],
    ]

    routes = []
    for _ in range(4):  # Generate three routes
        routes.append(hillClimbing(tsp))

    visualizeRoutes(tsp, routes)

    print("\nRoute Details:")
    for i, route in enumerate(routes):
        print(f"Route {i + 1}: {' -> '.join(cities[city_index] for city_index in route)}")
        total_distance, distances = totalDistance(tsp, route)
        print("Total Distance Traveled:", total_distance)
        print("Individual Distances:")
        for distance in distances:
            print(f"{distance[0]} to {distance[1]}: {distance[2]}")


if __name__ == "__main__":
    main()
