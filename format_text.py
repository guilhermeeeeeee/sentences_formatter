import re
import os
from number import written_number

def get_text_formatted(text):
    text = text.strip().lower()
    numbers = re.findall(r'\d+', text)
    text = re.sub(r'[$%&!?@|/()*]', '', text)
    for number in numbers:
        text = text.replace(number, written_number(int(number)))
    return text.split('. ')

def generate_sentences():
    sentences = []
    for article in os.listdir('articles'):
        if article.endswith('.txt'):
            with open('articles/{}'.format(article), 'r') as f:
                sentences = get_text_formatted(f.read())
    return sentences

with open('sentences.txt', 'w') as sentence_file:
    sentences = generate_sentences()
    for sentence in sentences:
        print(sentence)
        sentence_file.writelines('{}\n'.format(sentence))
