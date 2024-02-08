import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(self.V)}
        
    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        
    def dijkstra(self, src):
        min_heap = [(0, src)]
        distances = {i: float('inf') for i in range(self.V)}
        distances[src] = 0
        
        while min_heap:
            dist, u = heapq.heappop(min_heap)
            
            # For each neighbor v of u, see if the path through u to v is a shorter path than previously known
            for v, weight in self.graph[u]:
                if distances[v] > dist + weight:
                    distances[v] = dist + weight
                    heapq.heappush(min_heap, (distances[v], v))
                    
        return distances

# Let's create a graph with 9 vertices (0 to 8)
g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

# Now let's calculate the shortest paths from vertex 0 to all other vertices
shortest_paths = g.dijkstra(0)
shortest_paths
