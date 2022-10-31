# Ex-002: Work on TOC scanner

Updated: 2022.10.31

This exercise is to unpack a table of contents so that it can be rendered as a set.

**toc-scanner.py**: This is an iterator that loops through a toc yaml to create a list of markdown files and document types.

My notes:

load the toc as a dictionary.

iterate over each level.
At each level that is a list/array,
unpack the dictionaries, grab the markdown file, get the content-type and add to the dictionary.

We may need a service that categories the content by possible content type based on the rules.