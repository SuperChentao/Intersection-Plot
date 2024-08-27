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
    MOD = "modify"
    RMV = "remove"
    GEN = "generate"

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
                    print(f"cmd : {cmd}")
                case Operation.RMV.value:
                    print(f"cmd : {cmd}")
                case Operation.GEN.value:
                    print(f"cmd : {cmd}")
                case _:
                    print("cmd : Error")

        intersections, edges = find_intersections(streets)
        
        generate_graph(edges)
        # plot_streets_intersections(streets, intersections)

if __name__ == "__main__":
    main()


    # add "Weber Street" (2,-1) (2,2) (5,5) (5,6) (3,8)