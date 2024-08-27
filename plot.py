from matplotlib import collections
import pylab as pl
import numpy as np

def plot_street(street):
    roads = street.roads
    print(f"Ploting:")
    print(street.name)
    print(roads)
    line = list()
    for road in roads:
        if not road.start in line:
            line.append(road.start)
        line.append(road.end)

    return line
    
    # print(f"line: {line}")
    # for point in line:
    #     print(id(point))

    # lines = list()
    # lines.append(line)
    # print(lines)



    # lc = collections.LineCollection(lines, linewidths=2)
    # lc2 = collections.LineCollection(lines, linewidths=6)
    # fig, ax = pl.subplots()
    # ax.add_collection(lc2)
    # ax.autoscale()
    # ax.margins(0.1)
    pl.show()

def plot_streets(streets):
    lines = list()
    for street in streets:
        lines.append(plot_street(street))

    lc = collections.LineCollection(lines, linewidths=2)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    pl.show()

def plot_streets_intersections(streets, intersections):
    lines = list()
    for street in streets:
        lines.append(plot_street(street))

    lc = collections.LineCollection(lines, linewidths=2)
    fig, ax = pl.subplots()
    ax.add_collection(lc)

    for point in intersections:
        ax.plot(point.x, point.y, 'ro')
    ax.autoscale()
    ax.margins(0.1)
    pl.show()


