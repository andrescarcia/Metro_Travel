class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = [[float('inf')] * vertices for _ in range(vertices)]
        self.visa_required = set()

    def add_edge(self, src, dest, cost):
        self.edges[src][dest] = cost
        self.edges[dest][src] = cost

    def add_visa_required(self, airport):
        self.visa_required.add(airport)

    def find_route(self, src, dest, has_visa, minimize_cost=True):
        visited = [False] * self.vertices
        dist = [float('inf')] * self.vertices
        dist[src] = 0
        prev = [None] * self.vertices

        for _ in range(self.vertices):
            u = self.min_distance(dist, visited)
            visited[u] = True

            for v, edge_cost in enumerate(self.edges[u]):
                if not visited[v] and edge_cost != float('inf'):
                    if not has_visa and v in self.visa_required:
                        continue

                    new_cost = dist[u] + (edge_cost if minimize_cost else 1)
                    if new_cost < dist[v]:
                        dist[v] = new_cost
                        prev[v] = u

        return (dist[dest], self.build_path(prev, dest))

    def min_distance(self, dist, visited):
        min_dist = float('inf')
        min_index = -1

        for i, d in enumerate(dist):
            if not visited[i] and d < min_dist:
                min_dist = d
                min_index = i

        return min_index

    def build_path(self, prev, dest):
        path = []
        current = dest

        while current is not None:
            path.append(current)
            current = prev[current]

        return path[::-1]

