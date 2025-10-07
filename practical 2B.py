import queue as Q 
# Heuristic values (h(n)) 
dict_hn = { 
'Arad': 336, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 
'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 
'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234, 
'Oradea': 380, 'Pitesti': 100, 'Rimnicu': 193, 'Sibiu': 253, 
'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374 
} 
# Graph with costs (g(n)) 
dict_gn = dict( 
Arad=dict(Zerind=75, Timisoara=118, Sibiu=140), 
Bucharest=dict(Urziceni=85, Giurgiu=90, Pitesti=101, Fagaras=211), 
Craiova=dict(Drobeta=120, Pitesti=138, Rimnicu=146), 
Drobeta=dict(Mehadia=75, Craiova=120), 
Eforie=dict(Hirsova=86), 
Fagaras=dict(Sibiu=99, Bucharest=211), 
Giurgiu=dict(Bucharest=90), 
Hirsova=dict(Eforie=86, Urziceni=98), 
Iasi=dict(Neamt=87, Vaslui=92), 
Lugoj=dict(Mehadia=70, Timisoara=111), 
Mehadia=dict(Lugoj=70, Drobeta=75), 
Neamt=dict(Iasi=87), 
Oradea=dict(Zerind=71, Sibiu=151), 
Pitesti=dict(Rimnicu=97, Bucharest=101, Craiova=138), 
Rimnicu=dict(Sibiu=80, Pitesti=97, Craiova=146), 
Sibiu=dict(Rimnicu=80, Fagaras=99, Arad=140, Oradea=151), 
Timisoara=dict(Lugoj=111, Arad=118), 
Urziceni=dict(Bucharest=85, Hirsova=98, Vaslui=142), 
Vaslui=dict(Iasi=92, Urziceni=142), 
Zerind=dict(Oradea=71, Arad=75) 
) 
start = 'Arad' 
goal = 'Bucharest' 
result = '' 
# Function to calculate f(n) = g(n) + h(n) 
def get_fn(citystr): 
    cities = citystr.split(',') 
    gn = 0 
    for i in range(len(cities) - 1): 
        gn += dict_gn[cities[i]][cities[i + 1]] 
    hn = dict_hn[cities[-1]] 
    return hn + gn 
# Print the current queue 
def printout(cityq): 
    for i in range(cityq.qsize()): 
        print(cityq.queue[i]) 
 
# Expand a node 
def expand(cityq): 
    global result 
    tot, citystr, thiscity = cityq.get() 
    nexttot = 999 
    if not cityq.empty(): 
        nexttot, _, _ = cityq.queue[0] 
     
    if thiscity == goal and tot < nexttot: 
        result = citystr + '::' + str(tot) 
        return 
 
    print("Expanded city ------------------------------", thiscity) 
    print("Second best f(n) ---------------------------", nexttot) 
 
    tempq = Q.PriorityQueue() 
 
    for cty in dict_gn[thiscity]: 
        tempq.put((get_fn(citystr + ',' + cty), citystr + ',' + cty, cty)) 
 
    for _ in range(1, 3):  # Take top 2 best children 
        if not tempq.empty(): 
            ctrtot, ctrcitystr, ctrthiscity = tempq.get() 
            if ctrtot < nexttot: 
                cityq.put((ctrtot, ctrcitystr, ctrthiscity)) 
            else: 
                cityq.put((ctrtot, citystr, thiscity)) 
                break 
 
    printout(cityq) 
    expand(cityq) 
 
# Main function 
def main(): 
    cityq = Q.PriorityQueue() 
    cityq.put((999, "NA", "NA")) 
    cityq.put((get_fn(start), start, start)) 
    expand(cityq) 
    print("Result:", result) 
 
main()