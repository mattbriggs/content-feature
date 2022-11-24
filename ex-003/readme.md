# Ex-003: Work on pattern mining discovery using a graph

Updated: 2022.11.23

This exercises will load a list of repositories and crawl the repo to find 'toc.yml' objects. It then feeds each toc.yml file to a function that graphs the function. A routine then produces cypher files that can be loaded into Neo4j.

## Some notes

The output of the graphing section is format agnostic, and could accommodate different graph formats.

## Working notes

My notes:

load the toc as a dictionary.

iterate over each level.
At each level that is a list/array,
unpack the dictionaries, grab the markdown file, get the content-type and add to the dictionary.

We may need a service that categories the content by possible content type based on the rules.

https://neo4j.com/docs/python-manual/current/get-started/

http://localhost:7474/browser/


## Rough how to use instructions

The system starts with: `tocgrapher.py`
Update `jobtoc.yml` with the repos.

Here is the following example of the jobtoc.yml.

```yml
output: "C:\\data\\tocgraphs\\"
type: "neo4j"
folders:
  - folder: "C:\\git\\ms\\azure-docs-pr\\articles\\"
```

| Property | Value | Description |
| --- | --- | --- |
| output | file path (escaped virgule) | Output directory where the logs will be stored or with formats with an output, where the outputs will be placed. |
| type | Enum | `neo4j` : will connect to a Neo4J graph database and load the graph.<br>`csv`: Qill drop each toc graph as a node/edge pair of files into the output folder. |
| folders | array | a list of file path (escaped virgule)s to repositories to scan for` toc.ymls`. |