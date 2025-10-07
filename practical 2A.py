import queue as Q 
 
dict_hn = { 
    'Arad': 336, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 
    'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 
    'Iasi': 226, 'Lugoj': 244, 'Mehdia': 241, 'Neamt': 234, 
    'Oradea': 380, 'Pitesti': 100, 'Rimnicu': 193, 'Siblu': 253, 
    'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374 
} 
 
dict_gn = { 
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Siblu': 140}, 
    'Bucharest': {'Urziceni': 85, 'Giurgiu': 90, 'Pitesti': 101, 'Fagaras': 211}, 
    'Craiova': {'Drobeta': 120, 'Pitesti': 138, 'Rimnicu': 146}, 
    'Drobeta': {'Mehdia': 75, 'Craiova': 120}, 
    'Eforie': {'Hirsova': 86}, 
    'Fagaras': {'Siblu': 99, 'Bucharest': 211}, 
    'Giurgiu': {'Bucharest': 90}, 
    'Hirsova': {'Eforie': 86, 'Urziceni': 98}, 
    'Iasi': {'Neamt': 87, 'Vaslui': 92}, 
    'Lugoj': {'Mehdia': 70, 'Timisoara': 111}, 
    'Mehdia': {'Drobeta': 75, 'Lugoj': 70}, 
    'Neamt': {'Iasi': 87}, 
    'Oradea': {'Zerind': 71, 'Siblu': 151}, 
    'Pitesti': {'Rimnicu': 97, 'Bucharest': 101, 'Craiova': 138}, 
    'Rimnicu': {'Siblu': 80, 'Pitesti': 97, 'Craiova': 146}, 
    'Siblu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu': 80}, 
    'Timisoara': {'Arad': 118, 'Lugoj': 111}, 
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142}, 
    'Vaslui': {'Iasi': 92, 'Urziceni': 142}, 
    'Zerind': {'Arad': 75, 'Oradea': 71}, 
} 
 
start = 'Arad' 
goal = 'Giurgiu' 
 
def a_star(start, goal): 
    cityq = Q.PriorityQueue() 
    cityq.put((dict_hn[start], 0, start, [start]))  # (f(n), g(n), city, path) 
    visited = set() 
 
    while not cityq.empty(): 
        fn, gn, current, path = cityq.get() 
        if current in visited: 
            continue 
        visited.add(current) 
 
        if current == goal: 
            print("The A* path with total cost is:") 
            print(" -> ".join(path), "::", gn) 
            return 
 
        for neighbor in dict_gn.get(current, {}).keys(): 
            if neighbor not in visited: 
                new_gn = gn + dict_gn[current][neighbor] 
                new_fn = new_gn + dict_hn[neighbor] 
                cityq.put((new_fn, new_gn, neighbor, path + [neighbor])) 
 
    print("No path found.") 
 
if __name__ == '__main__': 
    a_star(start, goal) 