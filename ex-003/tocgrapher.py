'''
Workflow for module for graphing TOCs.

2022.11.22 Matt Briggs
'''

import yaml
import datetime
import time
from neo4j import GraphDatabase
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

class GraphDB:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_element(self, cquery):
        with self.driver.session() as session:
            result = session.execute_write(self._create_and_return_greeting, cquery)
            print(result)

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
                    logging.info("Query: {}".format(cypher))
                    add_element = GraphDB("bolt://localhost:7687", "neo4j", "reb00REB")
                    add_element.create_element(str(cypher))
                    add_element.close()
                except Exception as e:
                    logging.error("Error neo4j for {} : {}".format(t, e))
            elif config["type"].lower() == "csv":
                try:
                    create_csv_check(config["output"], graphed, count, todaysDate)
                except Exception as e:
                    logging.error("Error csv for {} : {} Query: {}".format(t, e, cypher))
            else:
                print("You need a value for the output type.")
                exit()
    logging.info('Finished')

if __name__ == "__main__":
    main()