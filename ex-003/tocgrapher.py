'''
Workflow for module for graphing TOCs.

2022.11.17 Matt Briggs
'''

import yaml
import datetime
import time
import mdbutilities.mdbutilities as MU

import tocharvestor as TH
import tocscanner as TS
import tocformats as TF


def create_csv_check(folder, graph, count):
    '''With a graph tuple and count create graph outputs.'''
    todaysDate = datetime.date.fromtimestamp(time.time());
    nodes = graph[0]
    edges = graph[1]
    nodefile = folder + "{}-{}-nodes.csv".format(todaysDate, count)
    edgefile = folder + "{}-{}-edges.csv".format(todaysDate, count)
    TF.create_csv(nodes, nodefile, edges, edgefile)

def main():

    with open (r"C:\git\feature\content-feature\ex-003\jobtoc.yml", "r") as stream:
        config = yaml.load(stream, Loader=yaml.CLoader)

    output = ""
    for i in config["folders"]:
        tocs = TH.get_tocs_from_repo(i["folder"])
        size = len(tocs)
        for count, t, in enumerate(tocs):
            print("{} of {} getting {}".format(size-count, size, t))
            graphed = TS.input_tocfile(t)
            output += TF.create_cypher_graph(graphed)
            create_csv_check("C:\\data\\tocgraphs\\", graphed, count)

    MU.write_text(output, config["output"])


if __name__ == "__main__":
    main()