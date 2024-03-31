# Import custom modules for each application component
from config_loader import load_config
from markdown_finder import find_markdown_files
from markdown_processor import process_markdown_files
from database_manager import setup_database, create_connection, save_data_to_database
from network_creator import create_semantic_network
from taxonomy_creator import create_taxonomy_opml  # Newly added import
from template_renderer import render_output_page
from logger_setup import setup_logging

# Constants for file paths and names
CONFIG_FILE = 'C:\\git\\feature\\content-feature\\ex-010\\config.yml'
DB_FILE = 'output\\markdown_entities.db'
LOG_FILE = 'output\\application_log.log'
TEMPLATE_FILE = 'entity_template.mustache'
OUTPUT_HTML = 'output\\output.html'
OUTPUT_GRAPHML = 'output\\semantic_network.graphml'
OUTPUT_OPML = 'output\\taxonomy.opml'


def main():
    # Set up loggingex-010\output\m
    setup_logging(LOG_FILE)

    # Load configuration
    directories = load_config(CONFIG_FILE)
    
    if directories:
        # Find markdown files
        markdown_files = find_markdown_files(directories)
        
        # Process markdown files
        entities_info = process_markdown_files(markdown_files)

        # Create and populate the database
        save_data_to_database(DB_FILE, entities_info)  # Save processed data to the database
        
        # Create a semantic network and export it
        create_semantic_network(DB_FILE, OUTPUT_GRAPHML)  # Adjusted to pass DB_FILE and OUTPUT_GRAPHML
        
        # Create and export taxonomy in OPML format
        create_taxonomy_opml(DB_FILE, OUTPUT_OPML)  # Newly added step
        
        # Render the output page
        render_output_page(entities_info, TEMPLATE_FILE, OUTPUT_HTML)  # Adjust parameters order to match definition
        
        print("Application finished successfully.")
    else:
        print("No directories specified in the configuration.")

if __name__ == "__main__":
    main()
