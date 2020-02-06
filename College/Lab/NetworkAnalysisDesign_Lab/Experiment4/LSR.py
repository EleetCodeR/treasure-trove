import sys
from collections import deque


class Graph():
    def __init__(self, no_of_verti):
        self.no_of_verti = no_of_verti
        self.graph = [[0 for i in range(no_of_verti)]
                      for i in range(no_of_verti)]

    def shortest_dist(self, dist, spt_set):
        min = sys.maxsize
        for v in range(self.no_of_verti):
            if dist[v] < min and spt_set[v] == False:
                min = dist[v]
                index_vtx = v

        return index_vtx

    def dijkstra_mcst(self, src):
        # maintaining distance array
        parent = [None]*self.no_of_verti
        parent[src] = -1
        dist = [sys.maxsize]*self.no_of_verti
        dist[src] = 0
        # an array to check if vertex is included in tree.
        spt_set = [False]*self.no_of_verti

        for i in range(self.no_of_verti):
            u = self.shortest_dist(dist, spt_set)
            spt_set[u] = True
            for v in range(self.no_of_verti):
                if self.graph[u][v] > 0 and spt_set[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    # update distance
                    dist[v] = dist[u] + self.graph[u][v]
                    # record parent:
                    parent[v] = u

        return (dist, parent)


def generate_LSR_DB(g, routing_Table, parent_Table):
    for i_src in range(g.no_of_verti):
        info_tuple = g.dijkstra_mcst(i_src)
        routing_Table.append(info_tuple[0])
        parent_Table.append(info_tuple[1])

    # show Routing table and Parent Tables:
    print("\n\t \t\t\t  LINK STATE DATABASE: \n")
    print("\t SRC \t\t  route    \t\t\t\t\t  parent \n")
    for i_src in range(g.no_of_verti):
        print(
            f"\t {i_src} \t\t {routing_Table[i_src]}  \t\t  {parent_Table[i_src]} \n")


def print_Shortest_Path(parent_Table, stack_p):
    # print the shortest path
    try:
        src = int(input("Enter source vertex:"))
        child = int(input("Enter destination vertex to print path :"))
        while True:
                # parent = info_tuple[1][child]
            parent = parent_Table[src][child]
            stack_p.append(child)
            if parent != -1:
                child = parent
            else:
                break

    except ValueError as ex:
        print(
            "===================[ Please Enter a valid vertex ]=================== \n")
        print(ex, type(ex))
    else:
        print("\n PATH from Source to Destination : \n")

        while stack_p:
            print(f"{stack_p.pop()}", end="")
            if stack_p:
                print(" ---> ", end="")
    print("\n\n")


def link_state_routing():
    # input graph
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    routing_Table = []
    parent_Table = []
    stack_p = deque()
    # Create LSR Database.
    generate_LSR_DB(g, routing_Table, parent_Table)
    # Show shortest path to reach a destination.
    print_Shortest_Path(parent_Table, stack_p)


link_state_routing()
