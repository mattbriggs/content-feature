import nltk
import json
from nltk.corpus import wordnet as wn


def read_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    return lines

def categorize_noun_phrases(noun_phrases):
    categorized_phrases = {}

    for noun_phrase in noun_phrases:
        category = {}

        tokens = nltk.word_tokenize(noun_phrase)
        for token in tokens:
            synsets = wn.synsets(token)

            for synset in synsets:
                hypernym_paths = synset.hypernym_paths()

                for path in hypernym_paths:
                    if len(path) >= 4:
                        level1 = path[0].lemmas()[0].name()
                        level2 = path[1].lemmas()[0].name()
                        level3 = path[3].lemmas()[0].name()

                        if level1 not in category:
                            category[level1] = {}
                        if level2 not in category[level1]:
                            category[level1][level2] = []
                        category[level1][level2].append(level3)

        categorized_phrases[noun_phrase] = category

    return categorized_phrases


noun_phrases = [

]

file_path = r"C:\git\feature\content-feature\ex-007\entities.txt"
out_path = "C:\\git\\feature\\content-feature\\ex-007\\categories.json"
noun_phrases = read_text_file(file_path)
categorized_phrases = categorize_noun_phrases(noun_phrases)
json_data = json.dumps(categorized_phrases, indent=4)
with open(out_path, 'w') as file:
    file.write(json_data)
