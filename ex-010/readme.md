# MarkNet Analyzer

## Application Overview

This Python application is designed to analyze and visualize the structure of knowledge within markdown (.md) files. It performs several key functions:

1. **Markdown File Ingestion**: Recursively identifies and reads markdown files from specified directories.
2. **Data Processing**: Extracts entities from the markdown files, considering plural forms.
3. **Database Management**: Stores and manages extracted data using SQLite.
4. **Taxonomy Creation**: Organizes entities into a hierarchy based on similarity.
5. **Summary Generation**: Produces summaries for each markdown file.
6. **Sentiment Analysis**: Evaluates the sentiment of each entity.
7. **Semantic Network Representation**: Visualizes the relationships between entities in a .graphml file.
8. **External Data Integration**: Fetches definitions for entities from external sources.
9. **Logging**: Tracks operations and outputs for debugging and record-keeping.
10. **Template Rendering**: Formats output pages using mustache templates.

## Requirements

- Python 3.x
- Pip (Python package installer)

## Installation

1. Clone the repository or download the source code to your local machine.
2. Navigate to the application directory.
3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Perform post-installation setup for NLTK:
   ```python
   import nltk
   nltk.download('wordnet')
   nltk.download('omw-1.4')
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('movie_reviews')
   ```

## Usage

1. **Configuration**: Create a YAML file named `config.yaml` specifying the directories containing your markdown files, following this structure:
   ```yaml
   directories:
     - path/to/markdowns/dir1
     - path/to/markdowns/dir2
   ```

2. **Logging**. To use this setup in your application, simply import and call setup_logging at the beginning of your main_script.py or before any other modules attempt to log messages:

    ```python
    from logger_setup import setup_logging
    
    # Call this at the start of your script
    setup_logging()
    ```

4. **Running the Application**: Execute the main script from the command line:
   ```bash
   python main_script.py
   ```
   Replace `main_script.py` with the name of your main application script. This script will perform all the operations outlined in the application overview.

5. **Viewing Results**: Check the generated outputs:
   - A `.graphml` file for the semantic network visualization.
   - A SQLite database `markdown_entities.db` containing extracted entities and their information.
   - Summarized markdown files and sentiment analysis results as specified in your application logic.
   - Templated output pages for viewing in a web browser.

## Development

- The application is modular, allowing for individual components to be updated or replaced as needed.
- Contributions to the application should follow standard coding practices and include updates to documentation for any changes made.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments

- NLTK Project
- NetworkX Contributors
- And all other libraries and data sources utilized in this application.

## Related content

- [Semantic Mapper - Original sketch](appplication_orginal.md)
- [Python Application Module Documentation](application_docs.md)