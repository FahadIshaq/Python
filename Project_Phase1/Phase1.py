import time #importing time for calculating time used by the algorithm 
import random #importing random

class GraphHead: #class 
    def __init__(self): #constructor
        self.count = 0 
        self.first = None

class GraphVertex: #class
    def __init__(self, data):#constructor
        self.nextVertex = None
        self.data = data
        self.inDegree = 0
        self.outDegree = 0
        self.processed = 0
        self.arc = None

class GraphArc: #class
    def __init__(self, destination, weight):#constructor
        self.destination = destination
        self.nextArc = None
        self.weight = weight

def create_graph():
    return GraphHead() #returning the graph head

def insert_vertex(graph, dataIn): #insert vertex method
    newVertex = GraphVertex(dataIn) 
    if graph.first is None: #checking the condition
        graph.first = newVertex 
    else: #ele conditon
        locPtr = graph.first
        predPtr = None
        while locPtr is not None and locPtr.data < dataIn: #checking the condition while is true
            predPtr = locPtr
            locPtr = locPtr.nextVertex
        if predPtr is None: #checking the condition
            newVertex.nextVertex = graph.first
            graph.first = newVertex
        else: #else condition
            newVertex.nextVertex = predPtr.nextVertex
            predPtr.nextVertex = newVertex
    graph.count += 1
    return 1 

def find_vertex(graph, data): #find vertex method
    locPtr = graph.first
    while locPtr is not None and locPtr.data != data: #checking the condition while is satisfying
        locPtr = locPtr.nextVertex
    return locPtr

def insert_arc(graph, fromData, toData, weight): #insert arc method
    fromVertex = find_vertex(graph, fromData)
    toVertex = find_vertex(graph, toData)
    if fromVertex is None or toVertex is None: #checking the condition
        return -2 if fromVertex is None else -3
    newArc = GraphArc(toVertex, weight)
    arcPtr = fromVertex.arc
    arcPredPtr = None
    while arcPtr is not None and arcPtr.destination.data < toVertex.data:#checking the condition while is satisfying
        arcPredPtr = arcPtr
        arcPtr = arcPtr.nextArc
    if arcPredPtr is None: #checking the condition
        fromVertex.arc = newArc
    else:#else condition
        arcPredPtr.nextArc = newArc
    newArc.nextArc = arcPtr
    fromVertex.outDegree += 1
    toVertex.inDegree += 1
    return 1

def construct_graph(v, e): #constructin the graph
    if e < v - 1 or e > v * (v - 1) // 2: #checking the condition
        raise ValueError("Invalid number of edges. Must satisfy v-1 ≤ e ≤ v(v-1)/2.")

    graph = create_graph()
    for i in range(v):#checking the condition while is valid
        insert_vertex(graph, i)
    
    
    for i in range(1, v):# To ensure the graph is connected, first create a spanning tree
        weight = random.randint(1, 20)
        insert_arc(graph, i-1, i, weight)
    
    added_edges = v - 1  # We already added v-1 edges in the spanning tree
    while added_edges < e:#checking the condition while is valid
        fromVertex = random.randint(0, v - 1)
        toVertex = random.randint(0, v - 1)
        if fromVertex != toVertex:  # Avoid self-loops 
            weight = random.randint(1, 20)
            if insert_arc(graph, fromVertex, toVertex, weight) == 1:
                added_edges += 1

    return graph

def print_graph(graph): #printing the graph
    vertex = graph.first
    while vertex is not None:#checking the condition while is valid
        print(f"Vertex {vertex.data}: ", end="")
        arc = vertex.arc
        while arc is not None:#checking the condition while is valid
            print(f"-> {arc.destination.data} (weight {arc.weight}) ", end="")
            arc = arc.nextArc
        print()
        vertex = vertex.nextVertex

#cases

start_time = time.time()
g = construct_graph(5, 5)
print_graph(g)
print(f"Running time for the algorithm: {time.time() - start_time:.5f} seconds\n")

start_time = time.time()
g = construct_graph(7, 9)
print_graph(g)
print(f"Running time for the algorithm: {time.time() - start_time:.5f} seconds\n")

start_time = time.time()
g = construct_graph(10, 15)
print_graph(g)
print(f"Running time for the algorithm: {time.time() - start_time:.5f} seconds\n")

# Custom values from the user

v = int(input("Enter the number of vertices: "))
e = int(input("Enter the number of edges: "))
start_time = time.time()
custom_graph = construct_graph(v, e)
print_graph(custom_graph)
print(f"Running time for the algorithm: {time.time() - start_time:.5f} seconds\n")
