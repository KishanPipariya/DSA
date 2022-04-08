def add_vertex(gr, v):
     pass

def add_edge(v1, v2):
    pass
graph=[]
while True:
    print("Enter 1 to create a vertex")
    print("ENter 2 to add a edge")
    in1 = input()
    if in1==1:
        in2 = input("Enter the vertex no:")
        add_vertex(graph, in2)