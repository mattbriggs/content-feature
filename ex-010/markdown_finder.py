import os
from pathlib import Path
import logging

def find_markdown_files(directories):
    """
    Recursively search for markdown files in the specified directories.
    
    Parameters:
    - directories: A list of directories to search for markdown files.
    
    Returns:
    - A list of paths to the found markdown files.
    """
    markdown_files = []
    for directory in directories:
        # Ensure the directory path is absolute
        directory = os.path.abspath(directory)
        # Use Path.rglob from pathlib to find all .md files recursively
        for md_file in Path(directory).rglob('*.md'):
            markdown_files.append(str(md_file))
            logging.info(f"Markdown file found: {md_file}")

    return markdown_files
