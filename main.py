import sys

from enum import Enum
from colorama import Fore, init
from regex_pattern import COORDINATE_PATTERN
import logging

from config import cmds
import config
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

def set_debug_mode():
    arguments = sys.argv
    if len(arguments) > 1:
        mode = arguments[1]
        if mode.lower() == "debug":
            config.debug_mode = True
            logging.basicConfig(level=logging.DEBUG)
            logging.debug(Fore.YELLOW + "running on debug mode")
            return
        
    logging.basicConfig(level=logging.INFO)
    logging.info(Fore.GREEN + f"running on standard mode\n")


def main():
        set_debug_mode()
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
                    if not street:
                        continue
                    streets.append(street)

                case Operation.MOD.value:
                    modify_street(streets, tokens)
  
                case Operation.RMV.value:
                    remove_street(streets, tokens)

                case Operation.GEN.value:
                    intersections, edges = find_intersections(streets)
                    generate_graph(edges)
                    plot_streets_intersections(streets, intersections)

                case _:
                    print(Fore.RED + f"command: {cmd} doesn't exist, please start with add, mod, rm, gg\n")

if __name__ == "__main__":
    main()


    # add "Weber Street" (2,-1) (2,2) (5,5) (5,6) (3,8)