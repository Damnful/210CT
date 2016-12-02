class Node(object):
    def __init__(self, nodeName):
        self.nodeName = nodeName
        self.adj = list()
        # adjacent nodes stored in a list

    def add_adjacent(self, a):
        if a not in self.adj:
            # makes sure no duplicate neighbours are made
            self.adj.append(a)

class Graph(object):
    nodes = {}
    # store nodes
    searchGraph = {}
    # this dictionary is only for the searches
    
    def add_node(self, node):
        if isinstance(node, Node) and node.nodeName not in self.nodes:
            # check to make sure duplicate nodes aren't made
            self.nodes[node.nodeName] = node
            return True
        else:
            return False

    def add_edge(self, x, y):
        if x in self.nodes and y in self.nodes:
            # ensure both nodes exist
            for key, value in self.nodes.items():
                # this loop makes sure that the opposing node is set as a neighbour
                if key == x:
                    value.add_adjacent(y)
                if key == y:
                    value.add_adjacent(x)
            return True
        else:
            return False

    def display_graph(self):
        for key in sorted(list(self.nodes.keys())):
            print(key + str(self.nodes[key].adj))
            # prints the graph using the node dictionary and keys
            self.searchGraph[key] = self.nodes[key].adj
            # creates the searchGraph dictionary for use in DFS and BFS for easier traversal

    def depth_first_search(self):
        stack = ['E',]
        # initialising stack with root node
        visited = []
        while stack:
            current = stack.pop()
            # iterates through the traversal using first value in stack, this case the root node
            if current not in visited:
                visited.append(current)
                # appends the node used, once finished, to the visited list, which is the order of traversal 
                stack.extend([x for x in self.searchGraph[current] if x not in visited])
                # this line appends every item in a list to the stack whilst also making sure to not use values from the visited list
        print("Depth first search results: " + str(visited))
        file = open("depthfirstsearch.txt", "w")
        file.write(str(visited))

    def breadth_first_search(self):
        queue = ['E',]
        # initialising stack with root node
        visited = []
        while queue:
            current = queue.pop(0)
            # iterates through the traversal using first value in stack, this case the root node
            if current not in visited:
                visited.append(current)
                # appends the node used, once finished, to the visited list, which is the order of traversal 
                queue.extend([x for x in self.searchGraph[current] if x not in visited])
                # this line appends every item in a list to the stack whilst also making sure to not use values from the visited list
        print("Breadth first search results: " + str(visited))
        file = open("breadthfirstsearch.txt", "w")
        file.write(str(visited))
        
g = Graph()
g.add_node(Node('A'))
g.add_node(Node('B'))
g.add_node(Node('C'))
g.add_node(Node('D'))
g.add_node(Node('E'))
g.add_node(Node('F'))
g.add_node(Node('G'))
g.add_node(Node('H'))
edges = ['AB', 'BD', 'DC', 'BE', 'GF', 'FH', 'EH']
for edge in edges:
    g.add_edge(edge[1:], edge[:1])
    # 1: is the first letter of the edge and :1 is the second letter of the edge
g.display_graph()
g.depth_first_search()
g.breadth_first_search()


