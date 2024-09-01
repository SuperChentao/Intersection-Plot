class Street:

    def __init__(self, name, roads):
        self.name = name
        self.roads = roads

    def update_roads(self, roads):
        self.roads = roads
    
    def get_name(self):
        return self.name
    

from point import Point
from road import Road
from regex_pattern import COORDINATE_PATTERN
from colorama import Fore
import re
import sys

def create_street(tokens):
    street_name = retrieve_street_name(tokens)
    if not street_name:
        return None
    
    roads = assign_coordinates(tokens)
    if not roads:
        return None
    
    print(f"street {street_name} has been created")
    return Street(street_name, roads)

def modify_street(streets, tokens):
    street_name = retrieve_street_name(tokens)
    if not street_name:
        return
    
    for street in streets:
        if street_name == street.get_name():
            roads = assign_coordinates(tokens)
            if roads:
                print(f"street {street_name} has been modified")
                street.update_roads(roads)
            return
            
    print(Fore.RED + f"the street {street_name} doesn't exist")
    return

def remove_street(streets, tokens):
    street_name = retrieve_street_name(tokens)
    if not street_name:
        return
    
    if len(tokens) > 0:
        print(Fore.RED + f"please only follow street name after rm")
        return
    
    for street in streets:
        if street_name == street.get_name():
            streets.remove(street)
            print(f"street {street_name} has been removed")
            return
    
    print(Fore.RED + f"the street {street_name} doesn't exist")
    sys.exit()
    return
    

def retrieve_street_name(tokens):
    try:
        street = tokens.pop(0)
        if(not str(street).startswith("\"")):
            print(Fore.RED + f"invalid Street name, wrap street name with \" \"")
            return None
        else:
            while(not str(street).endswith("\"")):
                street += " "+ tokens.pop(0)
    except IndexError:
        print(Fore.RED + f"invalid Street name, wrap street name with \" \"")
        return None
    
    return street

def assign_coordinates(tokens):
    roads = []

    start = None
    end = None

    while tokens:
        coordinate = tokens.pop(0)
        match = re.search(COORDINATE_PATTERN, coordinate)
        if match:
            try:
                x = float(match.group("x"))  # Captures the x-coordinate
                y = float(match.group("y"))  # Captures the y-coordinate
            except ValueError:
                print(Fore.RED + f"invalid coordiante format: {coordinate}, please enter (x,y)")
                return None
            point = Point(x,y)

            start = end
            end = point
            if(end and start):
                roads.append(Road(start, end))

        else:
            print(Fore.RED + f"invalid coordiante format: {coordinate}, please enter (x,y)")
            return None
    
    return roads