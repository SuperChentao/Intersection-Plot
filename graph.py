def generate_graph(edges):
    intersections = set()
    registered_id = list()

    for i, edge in enumerate(edges):
        # print(f"edge:{i} start:{(edge.start)} end:{(edge.end)}")
        print(f"edge:{i} start:{edge.start} (address: {id(edge.start)}) start:{edge.end} (address: {id(edge.end)})")

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
                print(f"found id{id} in registration")
                idd += 1
            registered_id.append(idd)
            intersections[i].set_id(idd)
        else:
            print(f"intersection{intersections[i].id} has id")

    print("\nV = {")
    for i in intersections:
        print(" " + str(i))
    print("}\n")

    print("E = {")
    for e in edges:
        # assign id to to duplicated points
        if e.start.id == -1:
            e.start.id = intersections.index(e.start) + 1
        if e.end.id == -1:
            e.end.id = intersections.index(e.end) + 1
            
        print(" " + str(e.repr_id()))
    print("}\n")