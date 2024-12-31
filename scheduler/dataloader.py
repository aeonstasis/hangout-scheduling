import networkx as nx
import sys
from pathlib import Path
import matplotlib.pyplot as plt
import csv


def load_dataset(filename: Path) -> nx.Graph:
    """
    Helper utility to parse a CSV file into a Graph.
    """
    nodes = []
    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in reader:
            name, gender = row
            nodes.append(name, gender=gender)

    return nx.complete_graph(nodes)


if __name__ == "__main__":
    filename = sys.argv[1]

    g = load_dataset(filename)
    ax = plt.plot()
    nx.draw(g, with_labels=True, font_weight="bold")
    plt.show()
