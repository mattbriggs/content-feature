import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.parse import DependencyGraph
from nltk.corpus import stopwords

def score_average_passive_sentences(text):
    """
    Scores a text string for the average number of passive sentences.

    Args:
        text (str): The text string to analyze.

    Returns:
        float: The average number of passive sentences per sentence in the text.
    """
    # Tokenize the text into sentences
    sentences = nltk.sent_tokenize(text)

    # Define a function to check if a word is a passive verb
    def is_passive_verb(word):
        return word == 'VBG' or word == 'VBN'

    # Count the number of passive sentences and the total number of sentences
    num_passive_sentences = 0
    num_sentences = len(sentences)

    # Loop through each sentence
    for sentence in sentences:
        # Tokenize the sentence into words
        words = word_tokenize(sentence)
        # Remove stop words
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word.casefold() not in stop_words]
        # Perform part-of-speech (POS) tagging
        tagged = pos_tag(words)
        # Loop through each word in the tagged sentence
        for i, (word, pos) in enumerate(tagged):
            # Check if the word is a passive verb and if the next word is a subject
            if (pos == 'VBG' or pos == 'VBN') and (i + 1 < len(tagged)) and (tagged[i + 1][1] == 'NN'):
                num_passive_sentences += 1
                break

    # Calculate the average number of passive sentences per sentence
    avg_passive_sentences = num_passive_sentences / num_sentences if num_sentences > 0 else 0

    return avg_passive_sentences


text = "The book was written by the author. The cake was baked by her mom. The room was cleaned by the maid."
avg_passive_sentences = score_average_passive_sentences(text)
print("Average number of passive sentences per sentence: ", avg_passive_sentences)
