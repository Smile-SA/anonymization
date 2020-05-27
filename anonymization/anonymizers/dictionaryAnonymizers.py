import re

from ..Anonymization import Anonymization

class _DictionaryAnonymizer():
    '''
    Delete all words that are not part of the dictionary (keep numbers and ponctuation)
    '''

    def __init__(self, anonymization: Anonymization, dictionary: list):
        self.anonymization = anonymization
        self.dictionary = dictionary
    
    def anonymize(self, text: str) -> str:
        return "".join(w for w in re.findall(r"[\w]+|[^\w]", text) if w.lower() in self.dictionary or not w.isalpha())

def DictionaryAnonymizer(dictionary: list) -> _DictionaryAnonymizer:
    '''
    Context wrapper for _DictionaryAnonymizer, takes list of valid words.
    '''
    return lambda anonymization: _DictionaryAnonymizer(anonymization, dictionary)