# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def getRequiredRepresentation(tour):
    print ("tour", tour)
    result = []
    firstEdge = tour[0]
    result.append(firstEdge[0])
    result.append(firstEdge[1])
    tour.remove(firstEdge)
    for edge in tour:
        result.append(edge[1])
    return result

def getUnexploredEdge(endNode, graph):
    unexploredEdges = (unexploredEdge for unexploredEdge in graph
                       if endNode == unexploredEdge[0] or endNode == unexploredEdge[1])
    result = list(unexploredEdges)
    print ("result:", result)
    print ("graph:", graph)
    if len(graph) == 1:
        return tuple(graph[0])
    if len(result) == 0:
        return ()
    else:
        return result.pop()

def find_eulerian_tour_internal(beginNode, tour, graph):
    print ("beginNode:", beginNode)
    unexploredEdge = getUnexploredEdge(beginNode, graph)
    print ("internal, edge:", unexploredEdge)
    if unexploredEdge == ():
        return tour
    graph.remove(unexploredEdge)
    # reverse the edge
    if unexploredEdge[1] == beginNode:
        unexploredEdge = (unexploredEdge[1], unexploredEdge[0])
        print ("new unexploredEdge:",unexploredEdge )
    find_eulerian_tour_internal(unexploredEdge[1], tour, graph)
    #tour.append(unexploredEdge)
    tour.insert(0, unexploredEdge)

def find_eulerian_tour(graph):
    tour = []
    edge = graph[0]
    beginNode = edge[0]
    find_eulerian_tour_internal(beginNode, tour, graph)
    return getRequiredRepresentation(tour)

if __name__ == "__main__":
    tour = find_eulerian_tour( [(1, 2), (2, 3), (3, 1)])
    print ("tour1:", tour)
    print ("===========================================")
    #tour = find_eulerian_tour( [(1, 2), (1, 3), (1, 5), (1, 6), (2, 6), (2, 4), (2, 5), (3, 4)])
    tour = find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)])
    print ("tour2:", tour)