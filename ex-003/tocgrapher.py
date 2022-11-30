'''
Workflow for module for graphing TOCs.

2022.11.22 Matt Briggs
'''

import yaml
import datetime
import time
import logging

import tocharvestor as TH
import tocscanner as TS
import tocformats as TF
import mdbutilities.mdbutilities as MU


def create_csv_check(folder, graph, count, indate):
    '''With a graph tuple and count create graph outputs.'''
    nodes = TF.make_table(graph[0])
    edges = TF.make_table(graph[1])
    nodefile = folder + "{}-{}-nodes.csv".format(indate, count)
    edgefile = folder + "{}-{}-edges.csv".format(indate, count)
    TF.create_csv(nodes, nodefile, edges, edgefile)


def main():
    '''Builds the graph by the specified output type from a list of github 
    repositories that use the DocFX/Learn.microsoft.com content type.
    Operation: Loads a config file, counts the yml files, and parses each toc 
    file and the content associated with it. Writes to a cypher database,
    or outputs graph formats to the specified file.
    
    '''

    with open (r"C:\git\feature\content-feature\ex-003\jobtoc.yml", "r") as stream:
        config = yaml.load(stream, Loader=yaml.CLoader)

    todaysDate = datetime.date.fromtimestamp(time.time());
    logging.basicConfig(filename="{}{}-logs.log".format(config["output"], todaysDate), level=logging.INFO)
    logging.info("Job run at: {}".format(time.localtime(time.time())))

    for i in config["folders"]:
        tocs = TH.get_tocs_from_repo(i["folder"])
        size = len(tocs)
        if config["limit"] == "0":
            limit = size
        else:
            limit = config["limit"]
        for count, t, in enumerate(tocs):
            if count < limit:
                print("{} of {} getting {}".format(size-count, size, t))
                graphed = TS.input_tocfile(t)
                if config["type"].lower() == "neo4j":
                    try:
                        output = TF.create_cypher_graph(graphed)
                        filename = config["output"] + "{}-graph-{}.cypher".format(todaysDate, count)
                        MU.write_text(output, filename)
                    except Exception as e:
                        logging.error("Error neo4j for {} : {}\n".format(t, e))
                elif config["type"].lower() == "csv":
                    try:
                        create_csv_check(config["output"], graphed, count, todaysDate)
                    except Exception as e:
                        logging.error("Error csv for {} : {} : {}".format(t, e, graphed))
                else:
                    print("You need a value for the output type.")
                    exit()
    logging.info("Finished: {}".format(time.localtime(time.time())))


if __name__ == "__main__":
    main()