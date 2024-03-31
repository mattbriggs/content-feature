from sklearn.metrics.pairwise import cosine_similarity
from scipy.cluster.hierarchy import linkage, fcluster
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString
import pandas as pd
import numpy as np

def linkage_to_opml(linkage_matrix, labels, max_distance=0.7, output_file='taxonomy.opml'):
    """
    Converts a hierarchical clustering linkage matrix into an OPML file.
    """
    # Determine cluster assignments for each item
    cluster_assignments = fcluster(linkage_matrix, max_distance, criterion='distance')
    unique_clusters = np.unique(cluster_assignments)

    # Create the OPML structure
    opml = Element('opml')
    opml.set('version', '2.0')
    body = SubElement(opml, 'body')
    outline = SubElement(body, 'outline')
    outline.set('text', 'Entities Taxonomy')

    # Build a dictionary to hold cluster entities
    clusters = {cluster: [] for cluster in unique_clusters}
    for i, cluster_id in enumerate(cluster_assignments):
        clusters[cluster_id].append(labels[i])

    # Populate the OPML structure
    for cluster_id, entities in clusters.items():
        cluster_outline = SubElement(outline, 'outline')
        cluster_outline.set('text', f'Cluster {cluster_id}')
        for entity in entities:
            entity_outline = SubElement(cluster_outline, 'outline')
            entity_outline.set('text', entity)

    # Convert to a pretty XML string
    rough_string = tostring(opml, 'utf-8')
    reparsed = parseString(rough_string)
    pretty_xml_as_string = reparsed.toprettyxml(indent="  ")

    # Save to a file
    with open(output_file, 'w') as f:
        f.write(pretty_xml_as_string)

def create_taxonomy_opml(matrix, output_file='taxonomy.opml'):
    """
    Uses hierarchical clustering to create a taxonomy of entities based on their similarity
    and saves an OPML representation.
    """
    # Calculate the cosine similarity between entities
    similarity_matrix = cosine_similarity(matrix)
    
    # Perform hierarchical clustering
    Z = linkage(similarity_matrix, 'ward')
    
    # Generate and save the taxonomy as OPML
    linkage_to_opml(Z, matrix.index.tolist(), output_file=output_file)

# Example usage
# Assuming `matrix` is your entity-file matrix as a pandas DataFrame
# create_taxonomy_opml(matrix)
