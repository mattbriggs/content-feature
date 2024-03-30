import re
from textblob import TextBlob
import logging

def extract_entities_and_summary(md_file_path):
    """
    Extracts entities from a markdown file and generates a simple summary.

    Parameters:
    - md_file_path: The path to the markdown file.

    Returns:
    - A tuple (entities, summary) where:
        - entities is a list of unique entities found in the file.
        - summary is a brief summary of the file content.
    """
    try:
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            content = md_file.read()
            
        # Simple entity extraction: consider words starting with a capital letter as entities
        # This is a very basic approach and might include common nouns or even miss some entities.
        entities = list(set(re.findall(r'\b[A-Z][a-z]*\b', content)))
        
        # Generate a simple summary: use the first 3 sentences.
        # You might want to use more sophisticated NLP techniques for a production-level summary.
        blob = TextBlob(content)
        summary_sentences = blob.sentences[:3]
        summary = ' '.join(sentence.raw for sentence in summary_sentences)
        
        logging.info(f"Processed markdown file: {md_file_path}")
        return entities, summary
    except Exception as e:
        logging.error(f"Failed to process markdown file {md_file_path}: {e}")
        return [], ""

def process_markdown_files(markdown_files):
    """
    Processes each markdown file to extract entities and generate summaries.
    
    Parameters:
    - markdown_files: A list of paths to markdown files.
    
    Returns:
    - A dictionary with markdown file paths as keys and tuples of (entities, summary) as values.
    """
    results = {}
    for md_file in markdown_files:
        entities, summary = extract_entities_and_summary(md_file)
        results[md_file] = {"entities": entities, "summary": summary}
    return results
