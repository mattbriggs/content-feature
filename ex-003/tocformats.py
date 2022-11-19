'''
Input Nodes and Edges as a tuple of arrays that contains dictionaries 
describing the Node and Edge attributes.

Each function produces the target output. Currently supporting:
- cypher (Neo4j)
- gremlin (CosmoDB)
- graphml (Gelphi / yEd)
- dot (GraphViz)

2022.11.18 Matt Briggs

'''

import mdbutilities.mdbutilities as MU


def make_attribute(indict):
    keys = indict.keys()
    meat = ""
    for i in keys:
        meat += "{} : '{}'".format(i, indict[i])
    return "{{ {} }}".format(meat)


# cypher
def create_cypher_text(ingraph):
    '''With the path and file to a target directory and a mapper graph, create cypher files.'''
    nodes = create_cypher_nodes(ingraph)
    edges = create_cypher_edges(ingraph)
    output = nodes + edges
    return output


def create_cypher_nodes(ingraph):
    '''Create a node:
    CREATE (TheMatrix:Movie {title:'The Matrix', released:1999, tagline:'Welcome to the Real World'})'''
    output = ""
    for i in ingraph[0]:
        try:
            create_node = "CREATE (a:content {})".format(make_attribute(i))
            output += create_node
        except Exception as e:
            print("{} Error: {}".format(str(i), e))
    return output


def create_cypher_edges(ingraph):
    '''Create an edge:
    (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrix)'''
    output = ""
    for i in ingraph[1]:
        try: 
            create_edge = "CREATE (a:content {node_id: {}) -[r:{}] (b:content {node_id {})".format(i["source"], i["type"], i["target"]) 
            output += create_edge
        except Exception as e:
            print("{} Error: {}".format(str(i), e))
    return output

# gremlin
def create_gremlin_text(ingraph):
    '''With the path to a target directory and a mapper graph, create cypher files.'''
    ''' '''
    nodes = create_cypher_nodes(ingraph)
    edges = create_cypher_edges(ingraph)
    output = nodes + edges
    MU.write_text(output, target)


def create_gremlin_nodes(ingraph):
    ''' '''
    output = ""
    for i in ingraph:
        output += str(i[0])
    return output


def create_gremlin_edges(ingraph):
    ''' '''
    output = ""
    for i in ingraph:
        output += str(i[1])
    return output


# graphml
def create_graphml_text(ingraph):
    '''With the path to a target directory and a mapper graph, create cypher files.'''
    nodes = create_cypher_nodes(ingraph)
    edges = create_cypher_edges(ingraph)
    output = nodes + edges
    MU.write_text(output, target)


def create_graphml_nodes(ingraph):
    ''' '''
    output = ""
    for i in ingraph:
        output += str(i[0])
    return output



def create_graphmledges(ingraph):
    ''' '''
    output = ""
    for i in ingraph:
        output += str(i[1])
    return output


# dot (GraphViz)
def create_dot_text(ingraph):
    '''With the path to a target directory and a mapper graph, create cypher files.'''
    ''' '''
    nodes = create_dot_nodes(ingraph)
    edges = create_dot_edges(ingraph)
    output = nodes + edges
    MU.write_text(output, target)


def create_dot_nodes(ingraph):
    ''' '''
    output = ""
    for i in ingraph:
        output += str(i[0])
    return output

def create_dot_edges(ingraph):
    ''' '''
    output = ""
    for i in ingraph:
        output += str(i[1])
    return output