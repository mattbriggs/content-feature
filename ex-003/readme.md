# Ex-003: Work on pattern mining discovery using a graph

Updated: 2022.11.18

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