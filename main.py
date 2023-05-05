import re
from termcolor import colored

def clean_text(text):
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\n\t]', ' ', text)
    return text

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(colored(f'Could not open file "{filename}".', 'red'))
        return None

def validate_filename(filename):
    if not filename.endswith('.txt'):
        print(colored('The file must have a .txt extension.', 'red'))
        return False
    return True

def get_search_word():
    search_word = input('Enter the word you want to search for: ')
    return search_word

def get_search_options():
    exact_match = input('Do you want to search for exact matches? (y/n): ').lower() == 'y'
    case_sensitive = input('Do you want the search to be case sensitive? (y/n): ').lower() == 'y'
    return exact_match, case_sensitive

def count_word_occurrences(text, search_word, exact_match=True, case_sensitive=False):
    if not case_sensitive:
        text = text.lower()
        search_word = search_word.lower()
    if exact_match:
        pattern = r'\b{}\b'.format(re.escape(search_word))
    else:
        pattern = re.escape(search_word)
    word_count = len(re.findall(pattern, text))
    return word_count

def search_word_in_file():
    filename = input('Enter the name of the text file: ')
    if not validate_filename(filename):
        return
    text = read_file(filename)
    if text is None:
        return
    search_word = get_search_word()
    exact_match, case_sensitive = get_search_options()
    text = clean_text(text)
    word_count = count_word_occurrences(text, search_word, exact_match, case_sensitive)
    if word_count > 0:
        print(colored(f'The word "{search_word}" appears {word_count} times in the file "{filename}".', 'green'))
    else:
        print(colored(f'The word "{search_word}" does not appear in the file "{filename}"', 'red'))

search_word_in_file()
