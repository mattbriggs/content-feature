'''
pip install --upgrade py2neo

https://py2neo.org/

'''

from py2neo import Graph

graph = Graph("bolt://localhost:7687", auth=("neo4j", "reb00REB"))
data = graph.run('MATCH (a {name: "Concepts"} ) --> (b) RETURN (a), (b)').data()

# print number of nodes
print("Number of nodes: {}".format(len(data)))

# print root node info
print("Root nodes: {} | {}".format(data[0]["a"]["name"], data[0]["a"]["filepath"]))

#print children
for count, i in enumerate(data):
    print("  - {} | {}".format(count, i["b"]["content_type"]))

#print detail
print("\nDetials\n")
for count, i in enumerate(data):
        print(count)
        try:
            print("Title: {}".format(i["b"]["name"]))
        except:
            pass
        try:
            print("Type: {}".format(i["b"]["content_type"]))
        except:
            pass
        try:
            print("Summary: {}".format(i["b"]["summary"]))
        except:
            pass
        try:
            print("Path: {}\n\n".format(i["b"]["filepath"]))
        except:
            pass