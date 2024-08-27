from colorama import Fore, init
init(autoreset=True)

from point import Point, Intersection
from road import Road

def find_intersections(streets):
    """find intersections for all streets"""
    roads = list()
    intersections = set()

    for street in streets:
        roads.append(street.roads)
    
    print(f"roads:\n{roads}")
    all_roads = [road for sublist in roads for road in sublist]
    print(f"All roads:\n{all_roads}")
    
    while all_roads:
        road1 = all_roads.pop(0)
        print(Fore.GREEN + f"road1 is {road1}")
        for road2 in all_roads:
            print(f"Checking intersection between:{road1} and {road2}")
            if(road1.end is not road2.start and determine_intersection_existence(road1, road2)):
                intersection = calculate_intersection(road1, road2)
                print(Fore.BLUE + f"adding {intersection}, id: {id(intersection)}")
                intersections.add(intersection)
                print(Fore.RED + f"Intersection found on {intersection}, crossed by {road1} and {road2}")
    
    all_roads = [road for sublist in roads for road in sublist]
    for road in all_roads:
        if road.intersected:
            intersections.add(road.start)
            intersections.add(road.end)

    print(f"{len(intersections)} intersections:\n{intersections}")
    return intersections

def on_segment(p, q, r):
    return min(p.x, q.x) <= r.x <= max(p.x, q.x) and min(p.y, q.y) <= r.y <= max(p.y, q.y)

def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0  # Collinear
    elif val > 0:
        return 1  # Clockwise
    else:
        return 2  # Counterclockwise

def determine_intersection_existence(road1, road2):
    a = road1.start
    b = road1.end
    c = road2.start
    d = road2.end

    o1 = orientation(a, b, c)
    o2 = orientation(a, b, d)
    o3 = orientation(c, d, a)
    o4 = orientation(c, d, b)

    # General case
    if o1 != o2 and o3 != o4:
        return True

    # Special cases
    # a, b, c are collinear and c lies on segment ab
    if o1 == 0 and on_segment(a, b, c):
        return True

    # a, b, d are collinear and d lies on segment ab
    if o2 == 0 and on_segment(a, b, d):
        return True

    # c, d, a are collinear and a lies on segment cd
    if o3 == 0 and on_segment(c, d, a):
        return True

    # c, d, b are collinear and b lies on segment cd
    if o4 == 0 and on_segment(c, d, b):
        return True

    # If none of the cases hold, they do not intersect
    return False

def calculate_intersection(road1, road2):
    p1 = road1.start
    q1 = road1.end
    p2 = road2.start
    q2 = road2.end

    A1 = q1.y - p1.y
    B1 = p1.x - q1.x
    C1 = A1 * p1.x + B1 * p1.y

    A2 = q2.y - p2.y
    B2 = p2.x - q2.x
    C2 = A2 * p2.x + B2 * p2.y

    determinant = A1 * B2 - A2 * B1

    x = (B2 * C1 - B1 * C2) / determinant
    y = (A1 * C2 - A2 * C1) / determinant

    intersection = Point(x, y)
    road1.set_intersected()
    road2.set_intersected()
    return intersection