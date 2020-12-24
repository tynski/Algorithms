from collections import deque

class Vertex(object):
    def __init__(self, node):
        self.value = node
        self.distance = 0
        self.predecesor = None
        self.neighbours = {}
    
    def __str__(self):
        return str(self.value) + ' adjacent: ' + str([x for x in self.neighbours])

    def add_neighbour(self, node, weight):
        self.neighbours[node] = weight
    
class Graph(object):
    def __init__(self):
        self.vert_dict = {}

    def add_vertex(self, node):
        self.vert_dict[node] = Vertex(node)
    
    def add_edge(self, frm, to, weight):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
        
        self.vert_dict[frm].add_neighbour(to, weight)
        self.vert_dict[to].add_neighbour(frm, weight)
    
    def get_weight(self, frm, to):
        return self.vert_dict[frm].neighbours[to]


def breadth_first_search(graph, frm, to):
    queue = deque(frm)
    current_node = frm
    while queue:
        if current_node == to:
            break
        current_node = queue.pop()
        curr_vertex = g.vert_dict[current_node]
        for next_node, weight in curr_vertex.neighbours.items():            
            next_vertex = g.vert_dict[next_node]
            if next_vertex.predecesor is None:
                next_vertex.predecesor = curr_vertex.value
                next_vertex.distance = weight + curr_vertex.distance
                queue.append(next_node)
    
    return g.vert_dict[current_node].value + ',' + str(g.vert_dict[current_node].distance) + ',' + g.vert_dict[current_node].predecesor

g = Graph()

g.add_vertex('3')
g.add_vertex('5')
g.add_vertex('7')
g.add_vertex('9')
g.add_vertex('2')

g.add_edge('3', '5', 1)  
g.add_edge('3', '7', 1)
g.add_edge('5', '9', 1)
g.add_edge('5', '2', 1)
g.add_edge('7', '9', 1)

print(breadth_first_search(g, '3', '7'))