# -*- coding: utf-8 -*-

from .priorityQueue import PriorityQueue
from .graph import Graph


def best_first_search(start_node, end_node, graph_input={}):
    path = []
    myQueue = PriorityQueue()
    graph = Graph(graph_input)

    start_node = start_node
    end_node = end_node

    # print(start_node, end='')
    # start = graph.get_node_details(start_node)
    current_node = [start_node]

    while current_node[0] != end_node:
        current_node = graph.return_edges(current_node[0])
        myQueue.makeEmpty()

        for item in current_node:
            myQueue.insert(item)

        current_node = myQueue.delete()
        path.append(current_node[0])
        # print("-> " + str(current_node[0]) , end = '')
    return path
