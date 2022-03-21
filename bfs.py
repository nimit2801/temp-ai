graph = {
    'Vadodara': [['Godra', 9], ['Kevadia', 10], ['Chota Udaipur', 12]],
    'Godra': [['Dahod', 6], ['Jhambusar', 5]],
    'Kevadia': [['Baruch', 8]],
    'Chota Udaipur': [['Karjan', 9]],
    'Dahod': [['Ujjain', 4]],
    'Jhambusar': [['Dhar', 3]],
    'Bharuch': [['Indore', 0]],
    'Karjan': [['Indore', 0]],
    'Ujjain': [['Indore', 0]],
    'Dhar': [['Indore', 0]],
}

def bfs(start, end):
    visited = []
    unvisited = []
    visited.append(start)
    for node in graph[visited[-1]]:
        unvisited.append(node)
    unvisited.sort(key = lambda x: x[1])
    visited.append(unvisited[0][0])
    for node in graph[visited[-1]]:
        unvisited.append(node)
    unvisited.sort(key = lambda x: x[1])
    visited.append(unvisited[0][0])
    for node in graph[visited[-1]]:
        unvisited.append(node)
    unvisited.sort(key = lambda x: x[1])
    visited.append(unvisited[0][0])
    for node in graph[visited[-1]]:
        unvisited.append(node)
    unvisited.sort(key = lambda x: x[1])
    visited.append(unvisited[0][0])
    # unvisited.append(graph[visited[-1]])
    # unvisited.sort(key = lambda x: x[1])
    # visited.append(unvisited[0][0][0])
    print('visited: '+ str(visited))
    print('unvisited: '+ str(unvisited))

bfs('Vadodara', 'Indore')



