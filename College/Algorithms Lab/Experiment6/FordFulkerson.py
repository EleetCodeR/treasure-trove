from collections import defaultdict

# Represent Directed Graph as an Cost Adjacency Matrix


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def BFS(self, s, t, parent):
        visited = [False]*(self.ROW)
        queue = []

        # Mark Source node as visited.
        queue.append(s)
        visited[s] = True
        while queue:
            v_current = queue.pop(0)
            for indx, val in enumerate(self.graph[v_current]):
                if visited[indx] == False and val > 0:
                    queue.append(indx)
                    visited[indx] = True
                    parent[indx] = v_current

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False

    def FordFulkerson(self, source, sink):
        parent = [-1]*(self.ROW)
        max_flow = 0

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]


maxWaterFlow = [[0, 100, 0, 50, 0, 0],
                [0, 0, 55, 25, 0, 0],
                [0, 0, 0, 0, 25, 65],
                [0, 0, 20, 0, 35, 0],
                [0, 0, 0, 0, 0, 50],
                [0, 0, 0, 0, 0, 0]]

g = Graph(maxWaterFlow)

source = 0
sink = 5

print("The maximum possible flow is %d " % g.FordFulkerson(source, sink))
