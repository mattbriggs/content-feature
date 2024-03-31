# Semantic Mapper - Original sketch

I need an application that maps a corpus in markdown file to create a sentiment map. The sentiment map will be used to create a content inventory.  A semantic network is a conceptual framework used to represent knowledge in patterns of interconnected nodes and edges. In such networks, nodes represent concepts or entities, while edges represent the relationships or associations between these concepts. Semantic networks serve as a versatile tool in artificial intelligence, cognitive psychology, linguistics, and data analysis, offering a structured way to visualize and understand the complex interrelationships within a set of data or knowledge base.

To make this application, create a Python script that recursively identifies all of the markdown (.md) files by ingesting a `yaml` file that lists the folders that contain markdown files. The script will scan all of the markdown files in the list of directories. The yaml file also specifies the output from the script that includes:

 - a .`graphml` file that will display the semantic network
 - a sqlite database that will contain the tables describing the markdown files
 - A `toc.yml` file that is a hierarchy that represents each entity in a taxonomy. The `toc.yaml` uses the toc format in DocFX. Each entity in the taxonomy  is a title which is the entity, and the name of a markdown file that is the name of the entity containing a standard presentation of the entity as a single page.
 - Each entity will be a markdown page that has a standard presentation created using a mustache template. Each entity page will have a filename named for the unique entity in camel case. The file will have a title that is the entity, the definition, a list of links to 10 other entities files that are very similar, and then a table that lists the occurrences of the entity. Each column in the table will list the title of the file, the path to the file, the sentiment in the line, and  the line.

For each file it will produce a title, a short 150 word or less summary, and a file path in the database.

The script will collect a list of unique terms as entities that accounts for pluralization. For each entity the database will require the term, a definition of the term, and score for prominence in the corpus.

For each entity, it will have a relationship to the file that scores the prominence of the term in the article, the line number where the term appeared, the line where the term appeared, and the sentiment of the term in that line, and an average sentiment in the entire corpus.

In addition, each entity will have a relationship to another entities. The relationship will be determined by the similarity of occurrences in the articles for the two entities.

Notes on routines:
 - The summary routine will create a summary by scoring sentences for frequent entities and collect the 7 most prominent sentences.
 - The entity definition may use an external source of WordNet, the internet, and OpenAI to create a definition.
 - Sentiment will be calculated for each entity using natural language processing.

Notes on exported `.graphml`:
 - The exported .`graphml` file will be made of nodes and edges. Each term node is a term with the following properties: definition, sentiment, link to term detail. The edges is the semantic similarity of one term to another. All nodes in the graph will be linked to another node.
 - Nodes in the graph will be sized by their semantic centrality.
 - Nodes in the graph will be colored by sentiment: green positive, yellow negative.
 - The exported `.graphml` will defined groups for key terms.

Notes on taxonomy as `toc.yml`:
 - It will be an unsupervised term taxonomy will have levels based on similarity.  The unsupervised taxonomy of entities from a similarity graph involves several steps, leveraging both the structure of the similarity graph and clustering or hierarchical techniques to organize entities into a meaningful taxonomy. A similarity graph, where nodes represent entities and edges represent the degree of similarity between these entities, serves as the foundation for this process. The goal is to structure these entities into a hierarchical classification without predefined categories, relying on the data's inherent patterns. 

Including logging, for the output pages a mustache template, and include requirements.txt, and instructions to install the application.

## Related content

- [Python Application Module Documentation](application_docs.md)
- [MarkNet Analyzer](readme.md)