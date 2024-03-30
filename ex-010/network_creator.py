import networkx as nx
import sqlite3
import logging

def create_semantic_network(db_file, output_graphml='semantic_network.graphml'):
    """
    Creates a semantic network from entities in the database and saves it as a .graphml file.

    Parameters:
    - db_file: The SQLite database file path.
    - output_graphml: The output path for the .graphml file.
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Initialize a new directed graph
        G = nx.DiGraph()

        # Query to select all entities and the files they're associated with
        query = """
        SELECT e.entity_name, mf.file_path
        FROM entities e
        JOIN markdown_files mf ON e.file_id = mf.id
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        # Add nodes and edges based on entities and their co-occurrence in files
        for entity_name, file_path in rows:
            # Ensure nodes for each entity and file exist
            if not G.has_node(entity_name):
                G.add_node(entity_name, type='entity')
            if not G.has_node(file_path):
                G.add_node(file_path, type='file')

            # Add edge between entity and file (if not already exists)
            if not G.has_edge(entity_name, file_path):
                G.add_edge(entity_name, file_path)
        
        # Save the graph to a .graphml file
        nx.write_graphml(G, output_graphml)
        logging.info(f"Semantic network saved to {output_graphml}")

    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
    except Exception as e:
        logging.error(f"Error creating semantic network: {e}")
    finally:
        conn.close()
