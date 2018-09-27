'''
    dijkstra
'''

graph = {
    'start': { 'a': 6, 'b': 2 },
    'a': { 'fin': 1 },
    'b': { 'a': 3, 'fin': 5 },
    'fin': {}
}

infinity = float('inf')

costs = {
    'a': 6, 
    'b': 2,
    'fin': infinity
}

parents = {
    'a': 'start',
    'b': 'start',
    'fin': None
}

def find_lowest_cost_node(costs):
    lowest = infinity
    node = None
    for n in costs.keys():
        if (costs[n] < lowest) and (n not in processed):
            lowest = costs[n]
            node = n
    return node

processed = []

node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neibours = graph[node]
    for n in neibours.keys():
        new_cost = cost + neibours[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)


    
print(costs)
print(parents)