# Best First Search

from collections import defaultdict
graph = defaultdict(list)

graph[0].append([1, 10])
graph[0].append([2, 9])
graph[1].append([3, 8])
graph[3].append([3, 0])
graph[1].append([4, 11])
graph[4].append([4, 0])
graph[2].append([5, 8])
graph[5].append([5, 0])

print(len(graph))
print()

visited = []
unvisited = []

def bfs(node, t):
    vis = []
    while vis[-1][0] != t:
        unvisited.extend(graph[node])
        print("unvisited: " + str(unvisited))
        unvisited.sort(key=lambda x: x[1])
        print("unvisited: " + str(unvisited))
        vis.append(unvisited.pop(0))
        print("vis: " + str(vis))
        print("unvisited: " + str(unvisited))
        unvisited.extend(graph[vis[0][0]])
        print("unvisited: " + str(unvisited))


bfs(0, 5)



