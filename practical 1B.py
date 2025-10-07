def iddfs(graph, start, target, max_depth): 
    for depth in range(max_depth + 1):  # Try each depth level 
        visited = set() 
        if dls(graph, start, target, depth, visited): 
            return True 
    return False 
def dls(graph, node, target, depth, visited): 
    if depth == 0 and node == target: 
        return True 
    if depth > 0: 
        visited.add(node) 
        for neighbor in graph[node]: 
            if neighbor not in visited: 
                if dls(graph, neighbor, target, depth - 1, visited): 
                    return True 
    return False 
# Tree as a graph 
graph = { 
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F'], 
    'D': [], 
    'E': [], 
    'F': [], 
} 
start_node = 'A' 
target_node = 'F' 
maximum_depth = 3 
if iddfs(graph, start_node, target_node, maximum_depth): 
    print("Target node", target_node, "found with maximum depth of", maximum_depth) 
else: 
    print("Target node", target_node, "NOT found with maximum depth of", maximum_depth)
