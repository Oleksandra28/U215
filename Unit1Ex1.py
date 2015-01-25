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
    result = []
    firstEdge = tour.pop()
    result.append(firstEdge[0])
    result.append(firstEdge[1])
    for edge in tour:
        result.append(edge[1])
    return result

def getUnexploredEdges(endNode, graph):
    unexploredEdges = (unexploredEdge for unexploredEdge in graph
                       if endNode == unexploredEdge[0] or endNode == unexploredEdge[1])
    result = list(unexploredEdges)
    print ("unexplored edges: ", result)
    return result

def find_eulerian_tour_internal(beginNode, tour, graph):
    unexploredEdges = getUnexploredEdges(beginNode, graph)
    if len(unexploredEdges) == 0:
        return tour
    edge = unexploredEdges[0]
    print ("edge:", edge)
    beginN = edge[0]
    endN = edge[1]
    tour.append(edge)
    graph.remove(edge)
    find_eulerian_tour_internal(endN, tour, graph)

def find_eulerian_tour(graph):
    tour = []
    edge = graph.pop()
    beginNode = edge[0]
    endNode = edge[1]
    print ("edge:", edge)
    tour.append(edge)
    find_eulerian_tour_internal(endNode, tour, graph)
    if tour[len(tour)-1][0] == beginNode or tour[len(tour)-1][1] == beginNode:
        return getRequiredRepresentation(tour)
    else:
        return []

if __name__ == "__main__":
    tour = find_eulerian_tour( [(1, 2), (2, 3), (3, 1)])
    print (tour)
    print ("===========================================")
    tour = find_eulerian_tour( [(1, 2), (1, 3), (1, 5), (1, 6), (2, 6), (2, 4), (2, 5), (3, 4)])
    tour = find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)])
    print (tour)