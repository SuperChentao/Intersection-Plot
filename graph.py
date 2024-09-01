import logging
from colorama import Fore

def generate_graph(edges):
    intersections = set()
    registered_id = list()

    for i, edge in enumerate(edges):
        logging.debug(Fore.YELLOW + f"edge:{i} start:{edge.start} (address: {id(edge.start)}) start:{edge.end} (address: {id(edge.end)})")

    for e in edges:
        intersections.add(e.start)
        intersections.add(e.end)

    intersections = sorted(list(intersections))

    for i in intersections:
        if i.id != -1:
            registered_id.append(i.id)

    for i in range(len(intersections)):
        if(intersections[i].id == -1):
            idd = i + 1
            while idd in registered_id:
                idd += 1
            registered_id.append(idd)
            intersections[i].set_id(idd)

    print("\nV = {")
    for i in intersections:
        print(" " + str(i))
    print("}\n")

    print("E = {")
    for e in edges:
        # eliminate duplicated points
        if e.start.id == -1:
            start_id = intersections.index(e.start)
            e.start = intersections[start_id]
        if e.end.id == -1:
            end_id =  intersections.index(e.end)
            e.end = intersections[end_id]
            
        print(" " + str(e.repr_id()))
    print("}\n")