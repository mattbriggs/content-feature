'''This scripts work and unpacks a table of contents as two tables: nodes and edges
that can be consumed in yED.

2022.11.13 Matt Briggs
'''


from re import X
import sys
import yaml
import uuid
import mdbutilities.mdbutilities as MU
import markdownvalidator.mdhandler as MDH

# C:\git\ms\azure-docs-pr\articles\active-directory\app-provisioning\toc.yml
# https://learn.microsoft.com/en-us/azure/active-directory/app-provisioning/

def make_set(in_iter):
    '''with an iterable, convert to a set'''
    try:
        out_set = set(list(in_iter.keys()))
        return out_set
    except Exception as e:
        return print(e)
        exit()

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

def main():
    ''' '''
    try: 
        tocfile = sys.argv[1]
    except IndexError as e:
        tocfile = r"C:\git\ms\azure-docs-pr\articles\active-directory\app-provisioning\toc.yml"
        # print("Error: {}\nNeed a toc file.".format(e))
        # exit()

    print("Graphing ... {}".format(tocfile))

    with open (tocfile, "r") as stream:
        tocdict = yaml.load(stream, Loader=yaml.CLoader)

    spot = tocfile.lower().find("toc.yml")
    stem = tocfile[0:spot]

    # iterator to build a graph from the yaml TOC
    rootnode = {}
    rootnode["node_id"] = "root"
    rootnode["node_type"] = "toc-node"
    rootnode["toc_name"] = "root"
    rootnode["content_type"] = "None"
    rootnode["href"] = "None"

    nodes = []
    nodes.append(rootnode)
    rels = []

    def process_toc(intoc, parent_node):
        print("{}".format(parent_node))
        if type(intoc) == str:
            pass
        elif type(intoc) == list:
            for i in intoc:
                process_toc(i, parent_node)
        elif type(intoc) == dict:
            keys =  make_set(intoc)
            try:
                if "items" in keys:
                    try:
                        node = {}
                        edge = {}
                        node["node_id"] = str(uuid.uuid4())
                        node["node_type"] = "toc-node"
                        node["toc_name"] = intoc["name"]
                        node["content_type"] = "None"
                        node["href"] = "None"
                        edge["source"] = parent_node
                        edge["target"] = node["node_id"]
                        print(edge)
                        rels.append(edge)
                        nodes.append(node)
                        parent_node = node["node_id"]
                    except:
                        node = {}
                        edge = {}
                        node["node_id"] = str(uuid.uuid4())
                        node["node_type"] = "content-node"
                        node["toc_name"] = "no name"
                        node["content_type"] = "None"
                        node["href"] = ""
                        edge["source"] = parent_node
                        edge["target"] = node["node_id"]
                        print(edge)
                        rels.append(edge)
                        nodes.append(node)
                        parent_node = node["node_id"]
                    process_toc(intoc["items"], parent_node)
                elif "href" in keys:
                        node = {}
                        edge = {}
                        node["node_id"] = str(uuid.uuid4())
                        node["node_type"] = "content-node"
                        node["toc_name"] = intoc["name"]
                        node["content_type"] = "None"
                        node["href"] = ""
                        node["href"] = intoc["href"]
                        if intoc["href"].find(".md") > 0:
                            try:
                                handler = MDH.MDHandler()
                                md_page = handler.get_page(stem + str(intoc["href"]))
                                node["content_type"] = md_page.metadata["ms.topic"]
                            except:
                                pass
                        edge["source"] = parent_node
                        edge["target"] = node["node_id"]
                        print(edge)
                        rels.append(edge)
                        nodes.append(node)
            except Exception as e:
                print("Error: {}".format(e))
    process_toc(tocdict, "root")

    # output to tables
    csv_nodes = make_table(nodes)
    csv_edges = make_table(rels)
    MU.write_csv(csv_nodes, "c:\\data\\test-nodes.csv")
    MU.write_csv(csv_edges, "c:\\data\\test-edges.csv")

    print("Done")


if __name__ == "__main__":
    main()