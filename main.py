import sys
import re

from enum import Enum
from colorama import Fore, init
from regex_pattern import COORDINATE_PATTERN
from commands import cmds
# from point import Point
# from road import Road
from street import *
from plot import *
from intersection import *
from graph import generate_graph

init(autoreset=True)

class Operation(Enum):
    ADD = "add"
    MOD = "mod"
    RMV = "rm"
    GEN = "gg"

def promote(i):
    print("(1) add a street, (2) modify a street, (3) remove a street, and, (4) generate a graph")
    # line = sys.stdin.readline()
    line = cmds[i]
    tokens = line.split()
    return tokens



def main():
    # while True:
        streets = []
        intersections = list()
        edges = list()

        for i in range(len(cmds)):
            tokens = promote(i)
            cmd = tokens.pop(0)

            match cmd:
                case Operation.ADD.value:
                    street = create_street(tokens)
                    streets.append(street)

                case Operation.MOD.value:
                    print(Fore.CYAN + f"cmd : {cmd}")
                    # Assume the street exists
                    mod_street = create_street(tokens)
                    print(f"mod street name: |{mod_street.get_name()}|")
                    for s in streets:
                        print(f"gay name: |{s.get_name()}|")
                        if(s.get_name() == mod_street.get_name()):
                            print("find mod street name")
                            s.update_roads(mod_street.roads)
                            break

                case Operation.RMV.value:
                    street_name = " ".join(map(str, tokens))
                    print(f"street_name001: {street_name}")
                    for s in streets:
                        if(s.get_name() == street_name):
                            streets.remove(s)
                            break

                case Operation.GEN.value:
                    print(f"cmd : {cmd}")
                    intersections, edges = find_intersections(streets)
                    generate_graph(edges)
                    plot_streets_intersections(streets, intersections)
                case _:
                    print("cmd : Error")

if __name__ == "__main__":
    main()


    # add "Weber Street" (2,-1) (2,2) (5,5) (5,6) (3,8)