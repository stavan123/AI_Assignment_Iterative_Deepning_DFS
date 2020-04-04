#This function specifies the cites and the coordinate 
#on the screen according to the map image
def getCityXY(): 
    city = [
        ["Arad", 61, 227],  
        ["Zerind", 91, 164],
        ["Oradea", 124, 98],
        ["Sibiu", 248, 284],
        ["Timisoara", 65, 362],
        ["Lugoj", 179, 413],
        ["Mehadia", 186, 476],
        ["Drobeta", 180, 540],
        ["Craiova", 320, 559],
        ["RimnicuVilcea", 288, 359],
        ["Fagaras", 410, 299],
        ["Pitesti", 432, 430],
        ["Bucharest", 561, 496],
        ["Giurgiu", 518, 587],
        ["Urziceni", 654, 457],
        ["Vaslui", 736, 302],
        ["Iasi", 679, 205],
        ["Neamt", 569, 153],
        ["Hirsova", 777, 457],
        ["Eforie", 822, 550]
    ]
    # print(city[0][1])
    return city


def getCityEdges():  #Specifying the edges on the image of romania graph
    edges = [
        ["Arad", "Zerind"],
        ["Zerind", "Oradea"],
        ["Oradea", "Sibiu"],
        ["Arad", "Timisoara"],
        ["Timisoara", "Lugoj"],
        ["Lugoj", "Mehadia"],
        ["Mehadia", "Drobeta"],
        ["Drobeta", "Craiova"],
        ["Craiova", "RimnicuVilcea"],
        ["RimnicuVilcea", "Sibiu"],
        ["Arad", "Sibiu"],
        ["Sibiu", "Fagaras"],
        ["Fagaras", "Bucharest"],
        ["Bucharest", "Giurgiu"],
        ["Bucharest", "Pitesti"],
        ["Pitesti", "Craiova"],
        ["Pitesti", "RimnicuVilcea"],
        ["Bucharest", "Urziceni"],
        ["Urziceni", "Hirsova"],
        ["Hirsova", "Eforie"],
        ["Urziceni", "Vaslui"],
        ["Vaslui", "Iasi"],
        ["Iasi", "Neamt"],
    ]
    return edges
