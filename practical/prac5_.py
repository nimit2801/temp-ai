class bestFirstSearch:
    def __init__(self,graph):
        self.graph = graph
        self.queue = []
        self.visited = []
        self.other_arr = []

    def search(self):
        self.searchElement = input("\nEnter the element you want to reach : ")
        self.visited.insert(0,list(self.graph.keys())[0])
        self.queue.insert(0,list(self.graph.keys())[0])
        
        if self.queue[0] == list(self.graph.keys())[0]:
            temp = self.queue.pop(0)
            self.queue.extend(self.graph[temp])
            self.queue.sort(key=lambda x: x[1])
            self.visited.append(self.queue[0][0])

        for i in self.visited:
            temp = self.queue.pop(0)

            if temp[0] == self.searchElement:
                return temp[0]

            self.queue.extend(self.graph[temp[0]])
            self.queue.sort(key=lambda x: x[1])
            self.visited.extend([self.queue[0][0]])
            print(self.visited)

            
graphTree = {
    'A': [['O', 146], ['S', 140], ['C', 494]],
    'O': [['S', 151]],
    'S': [['F', 99],['R',80]],
    'C': [['R', 146],['P',138]],
    'R': [['P', 97]],
    'F': [['B', 211]],
    'P': [['B', 101]]
}


bfs = bestFirstSearch(graphTree)
bfss = bfs.search()
print("\nElement found:",bfss)