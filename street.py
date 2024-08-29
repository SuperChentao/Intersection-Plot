class Street:

    def __init__(self, name, roads):
        self.name = name
        self.roads = roads

    # def __str__(self):
    #     output = ""
    #     for road in self.roads:

    def update_roads(self, roads):
        self.roads = roads
    
    def get_name(self):
        return self.name
    

from point import Point
from road import Road
from regex_pattern import COORDINATE_PATTERN
import re

def create_street(tokens):
    coordinates = []
    roads = []
    street = tokens.pop(0)

    if(not str(street).startswith("\"")):
        return
    else:
        while(not str(street).endswith("\"")):
            street += " "+ tokens.pop(0)

    start = None
    end = None

    while tokens:
        match = re.search(COORDINATE_PATTERN, tokens.pop(0))
        if match:
            x = float(match.group("x"))  # Captures the x-coordinate
            y = float(match.group("y"))  # Captures the y-coordinate
            point = Point(x,y)
            coordinates.append(point)

            start = end
            end = point
            if(end and start):
                roads.append(Road(start, end))
                
        else:
            return # Error here
    
    return Street(street, roads)