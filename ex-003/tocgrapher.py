'''
Workflow for module for graphing TOCs.

2022.11.22 Matt Briggs
'''

import yaml
import datetime
import time
import logging
import mdbutilities.mdbutilities as MU

import tocharvestor as TH
import tocscanner as TS
import tocformats as TF


def create_csv_check(folder, graph, count, date):
    '''With a graph tuple and count create graph outputs.'''
    nodes = graph[0]
    edges = graph[1]
    nodefile = folder + "{}-{}-nodes.csv".format(date, count)
    edgefile = folder + "{}-{}-edges.csv".format(date, count)
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
        for count, t, in enumerate(tocs):
            print("{} of {} getting {}".format(size-count, size, t))
            graphed = TS.input_tocfile(t)
            if config["type"].lower() == "neo4j":
                try:
                    cypher = TF.create_cypher_graph(graphed)
                    logging.info("\Success neo4j: {} \n".format(cypher))
                except Exception as e:
                    logging.error("Error neo4j for {} : {}\n".format(t, e))
            elif config["type"].lower() == "csv":
                try:
                    create_csv_check(config["output"], graphed, count, todaysDate)
                except Exception as e:
                    logging.error("Error csv for {} : {} Query: {}".format(t, e, cypher))
            else:
                print("You need a value for the output type.")
                exit()
    logging.info("Finished: {}".format(time.localtime(time.time())))


if __name__ == "__main__":
    main()