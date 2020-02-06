from BellmanFord import Graph


def routingInfo_protocol():
    # define the network first
    V = int(input("Define the number of devices(vertices) in network:"))
    E = int(input("Define the number of links(routes) in network:"))
    g = Graph(V)

    for i in range(E):
        u = int(input("from vertex:"))
        v = int(input(f"from {u} to vertex:"))
        w = int(input(f"from {u} to {v} cost:"))
        g.addEdge(u, v, w)

    routing_Table = [[]]*V

    for src in range(V):
        routing_Table[src] = g.BellmanFord(src)

    print("\n \tROUTING TABLE: \t\t \n"+"\n from \t\t\t To \n")
    for i in range(V):
        print(f" {i} \t\t\t  {routing_Table[i]}")


routingInfo_protocol()
# V=4 ,E=5
# g.addEdge(0, 1, 2)
# g.addEdge(1, 2, 3)
# g.addEdge(2, 3, 11)
# g.addEdge(3, 0, 1)
# g.addEdge(1, 3, 7)

# Neagtive Edges
# V=5 , E=8
# g.addEdge(0, 1, -1)
# g.addEdge(0, 2, 4)
# g.addEdge(1, 2, 3)
# g.addEdge(1, 3, 2)
# g.addEdge(1, 4, 2)
# g.addEdge(3, 2, 5)
# g.addEdge(3, 1, 1)
# g.addEdge(4, 3, -3)


# Negative weight cycle:
# V=8 ,E=13
# g.addEdge(0, 1, 4)
# g.addEdge(0, 2, 4)
# g.addEdge(3, 0, 3)
# g.addEdge(3, 2, 2)
# g.addEdge(2, 4, 4)
# g.addEdge(4, 3, 1)
# g.addEdge(5,1,3)
# g.addEdge(2,5 ,-2 )
# g.addEdge(5, 4,-3 )
# g.addEdge(6,5 ,2 )
# g.addEdge(4, 6,-2 )
# g.addEdge(6,7 ,2 )
# g.addEdge(7,4 ,-2)
