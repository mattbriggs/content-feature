'''Extract features from markdown files. '''

import sys
import yaml
import nltk
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
from nltk.parse import DependencyGraph
from textstat import textstat
import markdown
from bs4 import BeautifulSoup
import mod_utilities as MU

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')

def get_soup(file):
    '''Get soup from markdown file.'''
    with open(file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    html = markdown.markdown(markdown_text)
    return BeautifulSoup(html, 'html.parser')

def get_text_only_from_md(file):
    '''Get text only from markdown file.'''
    soup = get_soup(file)
    paragraphs = soup.find_all('p')
    text = '\n'.join([p.text for p in paragraphs])
    return text

def feature_1(file):
    '''Count the number of words in a text file.'''
    text = get_text_only_from_md(file)
    words = text.split()
    return len(words)

def feature_2(file):
    '''Get sentences from a markdown file.'''
    text = get_text_only_from_md(file)
    sentences = nltk.sent_tokenize(text)
    return len(sentences)

def feature_3(file):
    '''Get paragraphs from a markdown file.'''
    soup = get_soup(file)
    return len(soup.find_all('p'))

def feature_4(file):
    """
    Calculate the average number of characters per word in a text.

    Args:
        text (str): The text string to analyze.

    Returns:
        float: The average number of characters per word.
    """
    # Get the text from the markdown file
    text = get_text_only_from_md(file)
    # Split the text into words
    words = text.split()
    # Calculate the total number of characters in all words
    total_chars = sum(len(word) for word in words)
    # Calculate the average number of characters per word
    avg_chars = total_chars / len(words) if len(words) > 0 else 0

    return avg_chars

def feature_5(file):
    '''Get the Avg Words/Sentence from a text file.'''
        # Get the text from the markdown file
    text = get_text_only_from_md(file)
    sentences = text.split('.')
    sentence_count = len(sentences)
    total_words = sum(len(sentence.split()) for sentence in sentences)
    avg_words_per_sentence = total_words / sentence_count if sentence_count > 0 else 0

    return avg_words_per_sentence


def feature_6(file):
    '''Get the Avg Sentences/Paragraph from a text file.'''
        # Get the text from the markdown file
    text = get_text_only_from_md(file)
    paragraphs = text.split('\n\n')
    paragraph_count = len(paragraphs)
    total_sentences = sum(len(paragraph.split('.')) for paragraph in paragraphs)
    avg_sentences_per_paragraph = total_sentences / paragraph_count if paragraph_count > 0 else 0

    return avg_sentences_per_paragraph


def feature_7(file):
    """
    Scores a text string for the average number of passive sentences.

    Args:
        text (str): The text string to analyze.

    Returns:
        float: The average number of passive sentences per sentence in the text.
    """
    text = get_text_only_from_md(file)
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


def feature_8(file):
    '''Get the flesh kinkaid score from a text file.'''
        # Get the text from the markdown file
    text = get_text_only_from_md(file)
    # Tokenize the text into sentences and words
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)

    # Calculate the number of sentences, words, and syllables
    num_sentences = len(sentences)
    num_words = len(words)
    num_syllables = sum(textstat.syllable_count(word) for word in words)

    # Calculate the Flesch-Kincaid readability score
    score = 0.39 * (num_words / num_sentences) \
        + 11.8 * (num_syllables / num_words) - 15.59

    return score


def feature_9(file):
    '''Count H2s from a markdown file.'''
    soup = get_soup(file)
    return len(soup.find_all('h2'))


def feature_10(file):
    '''Count links from a markdown file.'''
    soup = get_soup(file)
    return len(soup.find_all('a'))


def feature_11(file):
    '''Count code blocks from a markdown file.'''
    soup = get_soup(file)
    code_blocks = soup.find_all(['pre', 'code'])
    return len(code_blocks)


def feature_12(file):
    '''Count tables  from a markdown file.'''
    soup = get_soup(file)
    tables = soup.find_all('table')
    return len(tables)


def feature_13(file):
    '''Count img from a markdown file.'''
    soup = get_soup(file)
    img = soup.find_all('img')
    return len(img)


def feature_14(file):
    '''Count videos  from a markdown file.'''
    soup = get_soup(file)
    video = soup.find_all('video')
    return len(video)


def main():
    '''Main function.'''

    if sys.argv[1]:
        jobfile = sys.argv[1]
    else:
        print("Need a rules files.")
        sys.exit()

    with open (jobfile, "r") as stream:
        config = yaml.load(stream, Loader=yaml.CLoader)

    files = MU.get_files(config["repo"])

    report = [["ID", "Path", "# Words", "# Sentences", "# Paragraphs", \
                "Avg Chars/Word", "Avg Words/Sentence", \
                "Avg Sentences/Paragraph", "Passive Sentences", "Flesch", \
                "# H2s", "# Links", "# Code Blocks", "# Tables", \
                "# Images", "Videos"]]

    count = 0

    for f in files:
        print(f)
        try:
            row = []
            count += 1
            row.append(count)
            row.append(f)
            try:
                row.append(feature_1(f))
            except Exception as e:
                row.append(str(e))
            try:
                row.append(feature_2(f))
            except Exception as e:
                row.append(str(e))
            try:
                row.append(feature_3(f))
            except Exception as e:
                row.append(str(e))
            try:
                row.append(feature_4(f))
            except Exception as e:
                row.append(str(e))
            try:
                row.append(feature_5(f))
            except Exception as e:
                row.append(str(e))
            try:
                row.append(feature_6(f))
            except Exception as e:
                row.append(str(e))
            try:
                row.append(feature_7(f))
            except Exception as e:
                row.append(str(e))
            try:
                row.append(feature_8(f))
            except Exception as e:
                row.append(str(e))
            try:
                row.append(feature_9(f))
            except Exception as e:
                row.append(str(e))
            try:
                row.append(feature_10(f))
            except Exception as e:
                row.append(str(e))
            try:
                row.append(feature_11(f))
            except Exception as e:
                row.append(str(e))
            try:
                row.append(feature_12(f))
            except Exception as e:
                row.append(str(e))
            try:
                row.append(feature_13(f))
            except Exception as e:
                row.append(str(e))
            try:
                row.append(feature_14(f))
            except Exception as e:
                row.append(str(e))
            report.append(row)
        except Exception as e:
            print("Error: {}".format(e))

    csvout = config["outputfolder"] + "\\report.csv"
    MU.write_csv(report, csvout)
    input("Done. Hit a key.")


if __name__ == "__main__":
    main()
