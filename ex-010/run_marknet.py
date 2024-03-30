# Import custom modules for each application component
from config_loader import load_config
from markdown_finder import find_markdown_files
from markdown_processor import process_markdown_files
from database_manager import create_database
from network_creator import create_semantic_network
from template_renderer import render_output_page
from logger_setup import setup_logging

# Constants for file paths and names
CONFIG_FILE = 'config.yaml'
DB_FILE = 'markdown_entities.db'
LOG_FILE = 'application_log.log'
TEMPLATE_FILE = 'entity_template.mustache'
OUTPUT_HTML = 'output.html'

def main():
    # Set up logging
    setup_logging(LOG_FILE)

    # Load configuration
    directories = load_config(CONFIG_FILE)
    
    if directories:
        # Find markdown files
        markdown_files = find_markdown_files(directories)
        
        # Process markdown files
        entities_info = process_markdown_files(markdown_files)
        
        # Create and populate the database
        create_database(DB_FILE, entities_info)
        
        # Create a semantic network and export it
        create_semantic_network(entities_info)
        
        # Render the output page
        render_output_page(TEMPLATE_FILE, OUTPUT_HTML, entities_info)
        
        print("Application finished successfully.")
    else:
        print("No directories specified in the configuration.")

if __name__ == "__main__":
    main()
