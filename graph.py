import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        self.visa_required = set()

    def add_edge(self, src, dest, cost):
        if src not in self.edges:
            self.edges[src] = {}
        self.edges[src][dest] = cost

    def add_visa_required(self, airport):
        self.visa_required.add(airport)

    def find_route(self, src, dest, has_visa, minimize_cost=True):
        visited = set()
        queue = [(0, src, [])]

        while queue:
            (cost, current, path) = heapq.heappop(queue)
            if current not in visited:
                visited.add(current)
                path = path + [current]

                if current == dest:
                    return (cost, path)

                for neighbor, edge_cost in self.edges[current].items():
                    if not has_visa and neighbor in self.visa_required:
                        continue

                    new_cost = cost + (edge_cost if minimize_cost else 1)
                    heapq.heappush(queue, (new_cost, neighbor, path))

        return (None, [])


###
##decidí usar heapq porque es una biblioteca de Python que proporciona una implementación eficiente de una cola de prioridad. En el algoritmo de Dijkstra, necesitamos una estructura de datos que nos permita almacenar y recuperar los nodos con el menor costo acumulado de manera eficiente. La cola de prioridad es una estructura de datos adecuada para este propósito.
##La biblioteca heapq utiliza una estructura de montículo (heap) binario, que es una estructura de árbol binario en la que cada nodo es menor (o mayor, dependiendo de si es un montículo mínimo o máximo) que sus hijos. Esto permite encontrar y extraer el elemento mínimo (o máximo) en tiempo O(log n), donde n es el número de elementos en el montículo.
##En nuestro caso, utilizamos heapq.heappush() para agregar elementos a la cola de prioridad y heapq.heappop() para extraer el elemento con el menor costo acumulado. Estas operaciones tienen una complejidad de tiempo O(log n), lo que hace que el algoritmo de Dijkstra sea más eficiente en comparación con el uso de una lista simple, donde encontrar y extraer el elemento mínimo tendría una complejidad de tiempo O(n).
##En resumen, elegí heapq porque proporciona una implementación eficiente de una cola de prioridad, lo que mejora la eficiencia del algoritmo de Dijkstra
###