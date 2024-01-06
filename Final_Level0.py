import json
import math

def get_distance_matrix(data):
    #"""populate distance matrix"""
    length_cities = data["n_neighbourhoods"] + data["n_restaurants"]
    num_cities = length_cities
    distances = [[0] * num_cities for _ in range(num_cities)]
    
    for i in range(length_cities-1):
        distances[0][i+1] = data["restaurants"]["r0"]["neighbourhood_distance"][i]
        distances[i+1][0] = data["restaurants"]["r0"]["neighbourhood_distance"][i]
    for i in range(length_cities-1):
        for j in range(i + 1, num_cities-1):
            dist = data["neighbourhoods"]["n"+ str(i)]["distances"][j]
            distances[i+1][j+1] = int(dist)
            distances[j+1][i+1] = int(dist)
    return distances




def solve_tsp_nearest(distances):
    num_cities = len(distances)
    visited = [False] * num_cities
    tour = []
    total_distance = 0
    
    # Start at the first city
    current_city = 0
    tour.append(current_city)
    visited[current_city] = True
    
    
    
    
    # Repeat until all cities have been visited
    while len(tour) < num_cities:
        nearest_city = None
        nearest_distance = math.inf

        # Find the nearest unvisited city
        for city in range(num_cities):
            if not visited[city]:
                distance = distances[current_city][city]
                if distance < nearest_distance:
                    nearest_city = city
                    nearest_distance = distance

        # Move to the nearest city
        current_city = nearest_city
        tour.append(current_city)
        visited[current_city] = True
        total_distance += nearest_distance

    # Complete the tour by returning to the starting city
    tour.append(0)
    total_distance += distances[current_city][0]

    return tour, total_distance

with open("Z:\KLA Hackathon\input data\level0.json", 'r') as file:
      data = json.load(file)
      distances = get_distance_matrix(data)
      
tour, total_distance = solve_tsp_nearest(distances)

# output = {"v0": {"path": []}}
# for i in range(len(tour)):
#     if i==0 or i==len(tour)-1:
#         "r"+tour[i]


print("Tour:", tour)
print("Total distance:", total_distance)

"""
Tour: [0, 1, 3, 4, 2, 0]
Total distance: 1571
"""