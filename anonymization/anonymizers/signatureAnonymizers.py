import spacy
from typing import Iterable, List
from spacy.matcher import Matcher
from ..Anonymization import Anonymization

class SignatureAnonymizer():
    '''
    Identify all signature pattern and list them

    This class requires spacy and a spacy model:
    $ pip install spacy
    $ python -m spacy download <model>

    Call SignatureAnonymizer to detect signature patterns in the text
    '''

    def __init__(self, anonymization: Anonymization, model: str):
        self.anonymization = anonymization
        self.processor = spacy.load(model)

   
    def anonymize(self,text: str,patterns: List[str]) -> Iterable[str]:
        doc = self.processor(text)
        matcher = Matcher(self.processor.vocab)
        [matcher.add("Matcherextracter", [pattern]) for pattern in patterns]
        matches= matcher(doc)
        return [doc[start:end].text.strip() for match_id,start, end in matches]
       
