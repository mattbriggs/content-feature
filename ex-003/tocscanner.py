'''This scripts contains the function to convert a yaml to a touple that 
contains two arrays. [0] is an array of nodes. [1] is an array of edges.

2022.11.17 Matt Briggs
'''

from re import X
import yaml
import uuid
import mdbutilities.mdbutilities as MU
import markdownvalidator.mdhandler as MDH


def make_set(in_iter):
    '''With an iterable, convert to a set'''
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


def input_tocfile(intocyaml):
    '''With a toc yaml file return a touple of lists that contain node dicts and edge dicts'''
    with open (intocyaml, "r") as stream:
        tocdict = yaml.load(stream, Loader=yaml.CLoader)

    spot = intocyaml.lower().find("toc.yml")
    stem = intocyaml[0:spot]

    # iterator to build a graph from the yaml TOC
    rootID = str(uuid.uuid4())
    rnode = {}
    rnode["node_id"] = rootID
    rnode["node_type"] = "root"
    rnode["name"] = "root"
    rnode["content_type"] = "None"
    rnode["href"] = "None"

    nodes = []
    nodes.append(rnode)
    rels = []

    def process_toc(intoc, parent_node):
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
                        node["node_type"] = "toc"
                        node["name"] = intoc["name"]
                        node["content_type"] = "None"
                        node["href"] = "None"
                        edge["type"] = "child"
                        edge["source"] = parent_node
                        edge["target"] = node["node_id"]
                        rels.append(edge)
                        nodes.append(node)
                        parent_node = node["node_id"]
                    except:
                        node = {}
                        edge = {}
                        node["node_id"] = str(uuid.uuid4())
                        node["node_type"] = "content"
                        node["name"] = "no name"
                        node["content_type"] = "None"
                        node["href"] = ""
                        edge["type"] = "child"
                        edge["source"] = parent_node
                        edge["target"] = node["node_id"]
                        rels.append(edge)
                        nodes.append(node)
                        parent_node = node["node_id"]
                    process_toc(intoc["items"], parent_node)
                elif "href" in keys:
                        node = {}
                        edge = {}
                        node["node_id"] = str(uuid.uuid4())
                        node["node_type"] = "content"
                        node["name"] = intoc["name"]
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
                        edge["type"] = "child"
                        edge["source"] = parent_node
                        edge["target"] = node["node_id"]
                        rels.append(edge)
                        nodes.append(node)
            except Exception as e:
                print("Error: {}".format(e))
    process_toc(tocdict, rootID)

    return (nodes, rels)

def main():
    pass

if __name__ == "__main__":
    main()