import re
from number import written_number

def get_text_formatted(text):
    text = text.strip().lower()
    numbers = re.findall(r'\d+', text)
    text = re.sub(r'[.$%&!?@|/()*]', '', text)
    for number in numbers:
        text = text.replace(number, written_number(int(number)))
    return text.split('. ')
