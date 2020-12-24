class Vertex(object):
    def __init__(self, node):
        self.value = node
        self.distance = 0
        self.predecesor = None
        self.neighbours = {}
    
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

def depth_first_search(graph, frm, to):
    visited, stack = set(), [frm]
    while stack:
        node = stack.pop()
        if node == to:
            return node

        if node not in visited:
            visited.add(node)
            curr_vertex = graph.vert_dict[node]
            for next_node, weight in curr_vertex.neighbours.items():
                if next_node not in visited:
                    next_vertex = graph.vert_dict[next_node]
                    if not next_vertex.predecesor:
                        next_vertex.predecesor = curr_vertex.value
                        next_vertex.distance = weight + curr_vertex.distance
                    stack.append(next_node)
    
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

print(g.vert_dict[depth_first_search(g, '3', '2')].distance)
            
