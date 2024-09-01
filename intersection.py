from colorama import Fore
import logging

from point import Point, Intersection
from road import Road

def find_intersections(streets):
    """find intersections for all streets"""
    roads = list()
    intersections = set()
    intersection_roads = set()

    for street in streets:
        roads.append(street.roads)
    
    all_roads = [road for sublist in roads for road in sublist]
    logging.debug(f"all roads:\n{roads}\n")
    
    # Find intersections for all roads, and add them into sets
    while all_roads:
        road1 = all_roads.pop(0)
        for road2 in all_roads:
            logging.debug(f"Checking intersection between:{road1} and {road2}")
            if(road1.end != road2.start and road1.start != road2.end and determine_intersection_existence(road1, road2)):
                intersection = calculate_intersection(road1, road2)
                intersections.add(intersection)
                logging.debug(Fore.YELLOW + f"Intersection found on {intersection}, crossed by {road1} and {road2}")

                if intersection != road1.start:
                    intersection_roads.add(Road(road1.start, intersection))
                if intersection != road1.end:                    
                    intersection_roads.add(Road(road1.end, intersection))
                if intersection != road2.start:
                    intersection_roads.add(Road(road2.start, intersection))
                if intersection != road2.end:                    
                    intersection_roads.add(Road(road2.end, intersection))
    
    # Loop until no intersection found on segments
    count = 0
    while True:
        intersection_roads, found_segment_intersection = break_segments(intersection_roads, intersections)
        count += 1
        logging.debug(Fore.YELLOW + f"count: {count}")

        if not found_segment_intersection:
            break

    edges = list(filter(lambda road : road.start is not road.end, intersection_roads))

    for edge in edges:
            intersections.add(edge.start)
            intersections.add(edge.end)

    logging.debug(Fore.YELLOW + f"intersection_roads {len(edges)} edges:\n{edges}")
    return list(intersections), edges


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


def break_segments(intersection_roads, intersections):
    intersection_roads2 = set()
    found_segment_intersection = False

    for road in intersection_roads:
        seperate = False    # if the segment is seperated
        for intersection in intersections:
            # If intersection is on the segment
            if on_segment(road.start, road.end, intersection) and not orientation(road.start, road.end, intersection):
                if not intersection == road.start and not intersection == road.end:
                    logging.debug(Fore.YELLOW + f"found {intersection} on segment {road}, breaking the segment")
                    seperate = True
                    found_segment_intersection = True
                    
                    road1 = Road(intersection, road.start)
                    road2 = Road(intersection, road.end)

                    if not road1 in intersection_roads:
                        intersection_roads2.add(road1)
                        
                        logging.debug(Fore.YELLOW + f"{road1} added to set")
                        
                    if not road2 in intersection_roads:
                        intersection_roads2.add(road2)
                        found_segment_intersection = True
                        logging.debug(Fore.YELLOW + f"{road2} added to set")
                        
        if not seperate:
            intersection_roads2.add(road)
    
    return intersection_roads2, found_segment_intersection