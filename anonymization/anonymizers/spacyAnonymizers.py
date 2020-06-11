from types import SimpleNamespace

import spacy

from ..Anonymization import Anonymization

class _NamedEntitiesAnonymizer():
    '''
    Replace all named entities with fake ones

    This class requires spacy and a spacy model:
    $ pip install spacy
    $ python -m spacy download <model>

    Call NamedEntitiesAnonymizer if you want to pass an instance to an AnonymizerChain
    '''

    def __init__(self, anonymization: Anonymization, model: str):
        self.anonymization = anonymization
        self.processor = spacy.load(model)

    def anonymize(self, text: str) -> str:
        doc = self.processor(text)
        # remove whitespace entities and trim the entities
        ents = [ent.text.strip() for ent in doc.ents if not ent.text.isspace()]

        return self.anonymization.replace_all(text, ents, 'first_name')
    
    def evaluate(self, text: str) -> str:
        doc = self.processor(text)
        # remove whitespace entities and trim the entities
        ents = [SimpleNamespace(start=ent.start_char, end=ent.end_char, entity_type=ent.label_, score=1) for ent in doc.ents if not ent.text.isspace()]

        return ents

def NamedEntitiesAnonymizer(model: str) -> _NamedEntitiesAnonymizer:
    '''
    Context wrapper for _NamedEntitiesAnonymizer, takes a spacy model.
    '''

    return lambda anonymization: _NamedEntitiesAnonymizer(anonymization, model)