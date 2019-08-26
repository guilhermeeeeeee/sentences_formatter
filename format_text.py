import re

def get_text_formatted(text):
    text = text.strip().lower()
    return text.split('. ')

text = r'RegExr was created by gskinner.com, and is proudly hosted by Media Temple. 1Edit the Expression & Text to see matches. Roll over matches or the expression for details. PCRE & Javascript flavors of RegEx are supported. 11T1he side bar includes a Cheatsheet, full Reference, and Help. You can also Save & Share with the Community, and view patterns you create or favorite in My Patterns. 13Explore results with the Tools below. Replace & List output custom results. Details lists capture groups. Explain describes your expression in plain English.'

