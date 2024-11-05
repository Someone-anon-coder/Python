class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_vertex(self, vertex: any):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
    
    def add_edge(self, vertex1: any, vertex2: any):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
    
    def display(self):
        for vertex, edges in self.adj_list.items():
            print(f"{vertex} -> {', '.join(map(str, edges))}")
    
    def bfs(self, start_vertex: any):
        visited = set()
        queue = [start_vertex]
        
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                queue.extend(neighbor for neighbor in self.adj_list[vertex] if neighbor not in visited)
    
    def dfs(self, start_vertex: any):
        visited = set()
        self._dfs_recursive(start_vertex, visited)

    def _dfs_recursive(self, start_vertex: any, visited: set):
        if start_vertex not in visited:
            print(start_vertex, end=" ")
            
            visited.add(start_vertex)
            for neighbor in self.adj_list[start_vertex]:
                self._dfs_recursive(neighbor, visited)

graph = Graph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "E")
graph.add_edge("D", "E")

print("Graph Adjacency List:")
graph.display()

print("\nBFS Traversal:")
graph.bfs("A")

print("\nDFS Traversal:")
graph.dfs("A")