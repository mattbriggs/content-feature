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
        meat += "{} : '{}', ".format(i, indict[i])
    return "{{ {} }}".format(meat[:-2])


# cypher
def create_cypher_graph(ingraph):
    '''With the path and file to a target directory and a mapper graph, create cypher files.'''
    nodes = create_cypher_nodes(ingraph)
    edges = create_cypher_edges(ingraph)
    output = nodes + edges
    return output

NODECOUNT = 1

def create_cypher_nodes(ingraph):
    '''Create a node:
    CREATE (TheMatrix:Movie {title:'The Matrix', released:1999, tagline:'Welcome to the Real World'})'''
    global NODECOUNT
    output = ""
    for serial, i in enumerate(ingraph[0]):
        NODECOUNT += serial
        try:
            create_node = "CREATE (n{}:content {});\n".format(NODECOUNT, make_attribute(i))
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
            create_edge = "MATCH (a:content), (b:content)\nWHERE a.node_id = '{}' AND b.node_id ='{}'\nCREATE (a)-[r:child]->(b);\n\n".format(i["source"], i["target"]) 
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


#CSV files
def make_table(in_array):
    '''Take an array of dictionaries and a make a table of tables'''
    out_table = []
    # header
    headers = in_array[0].keys()
    out_table.append(list(headers))
    for index, i in enumerate(in_array):
        # if index > 0:
        row = []
        for j in headers:
            row.append(i[j])
        out_table.append(row)
    return(out_table)


def create_csv(nodes, nodefile, edge, edgefile):
    '''With the the tuple of node/edges from tocgrapher produce:
    - graph[0] (nodes) and path to a node file
    - graph[1[ (edges) and a path a edge file
    '''

    csv_nodes = make_table(nodes)
    csv_edges = make_table(edge)
    MU.write_csv(csv_nodes, nodefile)
    MU.write_csv(csv_edges, edgefile)


def main():
    print("This is a module of functions for the toc mapper.")

if __name__ == "__main__":
    main()