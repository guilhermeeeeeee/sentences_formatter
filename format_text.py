import re
import os
from number import written_number

def get_text_formatted(text):
    text = text.strip().lower()
    numbers = re.findall(r'\d+', text+' ')
    text = re.sub(r'[$%&@|/()*\n]', ' ', text)
    text = re.sub(r'[.!?]', '.', text)
    for number in numbers:
        text = text.replace(number, written_number(int(number)))
    return text.split('. ')

def generate_sentences():
    sentences = []
    for article in os.listdir('articles'):
        if article.endswith('.txt'):
            print(article)
            with open('articles/{}'.format(article), 'r', encoding="utf8") as f:
                sentences.append(get_text_formatted(f.read()))
                print(sentences)
    return sentences

def write_sentences(files_sentences):
    count_sentences = 0
    with open('sentences.txt', 'w', encoding="utf8") as sentence_file:
        for sentences in files_sentences:
            count_sentences = count_sentences + sentences.__len__()
            for sentence in sentences:
                sentence_file.writelines('{}\n'.format(sentence))
    return count_sentences

def sentences_formatter():
    sentences = generate_sentences()
    print(write_sentences(sentences))

sentences_formatter()
