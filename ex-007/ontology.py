from nltk.corpus import wordnet as wn

# noun_phrases = ['car', 'tree', 'dog', 'computer'] # example
noun_phrases = ["makes sense", "standardization score", "topic value", "clean right", "data science", "health score", "date metadata"]

ontology = {}

for phrase in noun_phrases:
    words = phrase.split()
    hypernyms = []
    for word in words:
        if wn.synsets(word):
            synsets = wn.synsets(word)
            for synset in synsets:
                hypernyms.extend(synset.hypernyms())
    ontology[phrase] = hypernyms

for i in ontology["makes sense"]:
    print(i.hypernyms()[0].hyponyms())