import warnings


class Graph(object):
    '''

        graph in the form
        {
            node = [[nodeA, weigh1], [nodeB, weigh2]],
            nodeA = [[nodeC, weigh3]]
        }
    '''

    def __init__(self, graph=None):
        '''
            sdfs
        '''
        if graph is None:
            graph = dict()
            self._graph = graph
        elif isinstance(graph, dict):
            self._graph = graph
        else:
            ValueError("Graph should be a dictionary")

        self._node_count = 0
        self._edge_count = 0

    @property
    def node_count(self):
        return self._node_count

    @property
    def edge_count(self):
        return self._edge_count

    def add_node(self, node):
        '''
            Adds node to the graph.
            If it already exists, raise an Error
        '''
        if node not in self._graph:
            self._graph[node] = []
            self._node_count += 1
        else:
            raise ValueError("Node " + str(node) + " already exists in graph")

    def add_node_from(self, nodes):
        '''
            add nodes from list of nodes
            #TODO
        '''
        pass

    def add_edge(self, start_node, end_node, weight=1):
        '''
            Adds edge from start_node to end_node
            If weight is not specified, defaults to one
            If the edge already exists, updates the weight to given in argument
        '''

        # check if start node already exists
        if start_node not in self._graph:
            warnings.warn("Node {} does not exist, adding it to graph".format(str(start_node)), Warning)
            self.add_node(start_node)
        edges = self._graph[start_node]

        # check if edge already exists)
        for edge in edges:
            if edge[0] == end_node:
                raise ValueError("Edge already exiists")

        # check if end node already exists
        if end_node not in self._graph:
            warnings.warn("Node {} does not exist, adding it to graph".format(str(end_node)), Warning)
            self.add_node(end_node)

        if not self._is_number(weight):
            raise ValueError("{} is not a valid Number".format(weight))

        edges = self._graph[start_node]
        for edge in edges:
            if edge[0] == end_node:
                warnings.warn("Edge already exists with weight {}, updating it to {}".format(str(edge[1]), str(weight)), Warning)
                edge[1] = weight
                return

        self._graph[start_node].append([end_node, weight])
        self._edge_count += 1

    def delete_node(self, node):
        '''
            Removoes all node dependecnies and then removes node
        '''
        if node not in self._graph:
            raise AttributeError("Node " + str(node) + " does not exist")

        for key, values in self._graph.items():
            if key == node:
                for edge in values:
                    self._edge_count -= 1
                continue
            else:
                for edge in values:
                    if edge[0] == node:
                        self.delete_edge(key, node)

        self._graph.pop(node, None)
        self._node_count -= 1

    def delete_edge(self, start_node, end_node):

        if start_node not in self._graph:
            raise AttributeError("Node " + str(start_node) + " does not exist")

        elif end_node not in self._graph:
            raise AttributeError("Node " + str(end_node) + " does not exist")

        edges = self._graph[start_node]
        for edge in edges:
            if edge[0] == end_node:
                self._graph[start_node].remove(edge)

        self._edge_count -= 1

    def delete_edge_from(self, start_node, end_node):
        # TODO
        pass

    def get_node_details(self, node):
        '''
            Returns all nodes connected to it in a dictionary
            dict = {
                node1: weigh1,
                node2: weigh2
            }
        '''
        if node in self._graph:
            temp_dict = {}
            edges = self._graph[node]

            for edge in edges:
                temp_dict[edge[0]] = edge[1]

            return temp_dict

        else:
            raise AttributeError("Node " + str(node) + " does not exist")

    def update_edge(self, start_node, end_node, weight=None):
        '''
            Updates the weight of the edge
            if the new weight is not specified, it deletes that edge
            if the edge is not found, it raise an error
        '''

        # check if nodes already exists
        if start_node not in self._graph:
            raise AttributeError("Node " + str(start_node) + " does not exist")

        elif end_node not in self._graph:
            raise AttributeError("Node " + str(end_node) + " does not exist")

        if weight is None:
            self.delete_edge(start_node, end_node)

        if not self._is_number(weight):
            raise ValueError("{} is not a valid Number".format(weight))

        edges = self._graph[start_node]
        for edge in edges:
            if edge[0] == end_node:
                edge[1] = weight
                return

        raise AttributeError("Edge from {} to {} does not exist".format(start_node, end_node))

    @property
    def nodes(self):
        '''
            returns a list of all nodes
        '''
        return [*self._graph]

    @property
    def graph(self):
        '''
            returns the graph
        '''
        return self._graph

    def return_edges(self, node):
        if node not in self._graph:
            raise AttributeError("Node " + str(node) + " does not exist")
        else:
            return self._graph[node]

    def get_edge(self, start_node, end_node):
        '''
            Returns the edge weight, raise AttributeError incase edge does not exist
        '''

        if start_node not in self._graph:
            raise AttributeError("Node " + str(start_node) + " does not exist")

        elif end_node not in self._graph:
            raise AttributeError("Node " + str(end_node) + " does not exist")

        edges = self._graph[start_node]
        for edge in edges:
            if edge[0] == end_node:
                return edge[1]

        raise AttributeError("Edge does not exist")

    def _is_number(self, number):
        try:
            float(number)
            return True
        except ValueError:
            return False
