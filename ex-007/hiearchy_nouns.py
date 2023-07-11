import nltk
import json
from nltk.corpus import wordnet



def read_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    return lines

def get_hypernyms(entity):
    synsets = wordnet.synsets(entity)
    hypernyms = set()
    for synset in synsets:
        hypernyms.update(synset.hypernyms())
    return hypernyms


# entities = read_text_file(r"C:\git\feature\content-feature\ex-007\entities.txt")
entities = ['dog', 'cat', 'horse', 'puppy', 'kitten', 'animal']

hierarchy = {}
for entity in entities:
    hierarchy[entity] = get_hypernyms(entity)

for entity, hypernyms in hierarchy.items():
    print(entity, ':', hypernyms)
