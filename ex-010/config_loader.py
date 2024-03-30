import yaml
import logging

def load_config(config_file):
    """
    Load directories from a YAML config file.
    
    Parameters:
    - config_file: Path to the YAML configuration file.
    
    Returns:
    - A list of directories specified in the config file, or an empty list if there's an error.
    """
    try:
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
            logging.info("Config file loaded successfully.")
            return config.get('directories', [])
    except FileNotFoundError:
        logging.error(f"Config file not found: {config_file}")
    except yaml.YAMLError as e:
        logging.error(f"Error parsing YAML file: {e}")
    except Exception as e:
        logging.error(f"Failed to load config file: {e}")
    
    return []

