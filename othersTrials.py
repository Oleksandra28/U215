def find_eulerian_tour(graph):
        tour=[]
        first = graph.pop()
        tour.append(first[1])
        find_tour(first[1],graph,tour)
        return tour


def find_tour(u,E,tour): 
    for (a,b) in E:
        if a==u:
            E.remove((a,b))
            find_tour(b,E,tour)
        elif b==u:
            E.remove((a,b))
            find_tour(a,E,tour)
    tour.insert(0,u)

if __name__ == "__main__":
    tour = find_eulerian_tour( [(1, 2), (2, 3), (3, 1)])
    print (tour)
    #tour = find_eulerian_tour( [(1, 2), (1, 3), (1, 5), (1, 6), (2, 6), (2, 4), (2, 5), (3, 4)])
    tour = find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)])
    print (tour)