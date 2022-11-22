'''
Workflow for module for graphing TOCs.

2022.11.17 Matt Briggs
'''

import yaml
import datetime
import time
from neo4j import GraphDatabase
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

class GraphDB:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_element(self, query):
        with self.driver.session() as session:
            result = session.execute_write(self._create_and_return_greeting, query)
            print(result)

    @staticmethod
    def _create_and_return_greeting(tx, query):
        result = tx.run(query)
        return result

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
            if config["type"].lower() == "neo4j":
                try:
                    create_csv_check("C:\\data\\tocgraphs\\", graphed, count)
                except Exception as e:
                    print("    Error CSV for {} : {}".format(t, e))
            elif config["type"].lower() == "csv":
                try:
                    cypher = TF.create_cypher_graph(graphed)
                    add_element = GraphDB("bolt://localhost:7687", "neo4j", "reb00REB")
                    add_element.create_element(cypher)
                    add_element.close()
                except Exception as e:
                    print("    Error neo4j for {} : {} Query: {}".format(t, e, cypher))

if __name__ == "__main__":
    main()