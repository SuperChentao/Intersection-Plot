def generate_graph(edges):
    intersections = set()
    for e in edges:
        intersections.add(e.start)
        intersections.add(e.end)

    intersections = sorted(list(intersections))

    for i in range(len(intersections)):
        intersections[i].set_id(i+1)

    print("\nV = {")
    for i in intersections:
        print(" " + str(i))
    print("}\n")

    print("E = {")
    for e in edges:
        if e.start.id == -1:
            e.start.id = intersections.index(e.start) + 1
        if e.end.id == -1:
            e.end.id = intersections.index(e.end) + 1
        print(" " + str(e.repr_id()))
    print("}")