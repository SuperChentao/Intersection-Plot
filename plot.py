from matplotlib import collections
import pylab as pl
import logging

logging.getLogger("PIL").setLevel(logging.WARNING)
logging.getLogger("matplotlib").setLevel(logging.WARNING)


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


def plot_street(street):
    roads = street.roads
    # logging.debug(f"Ploting:")
    # logging.debug(street.name)
    # logging.debug(roads)
    line = list()
    for road in roads:
        if not road.start in line:
            line.append(road.start)
        line.append(road.end)

    return line