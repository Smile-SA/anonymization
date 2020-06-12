import re
from types import SimpleNamespace

from ..Anonymization import Anonymization

class CreditCardAnonymizer():
    '''
    Replace all credit card numbers
    '''

    def __init__(self, anonymization: Anonymization):
        self.anonymization = anonymization
        # matches Visa, MasterCard, American Express, Diners Club, Discover, and JCB cards
        self.credit_card_regex = r'(?:4[0-9]{12}(?:[0-9]{3})?|[25][1-7][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})'
    
    def anonymize(self, text: str) -> str:
        return self.anonymization.regex_anonymizer(text, self.credit_card_regex, 'credit_card_number')

    def evaluate(self, text: str) -> str:
        matchs = re.finditer(self.credit_card_regex, text)
        ents = [SimpleNamespace(start=m.start(), end=m.end(), entity_type="CREDIT_CARD", score=1) for m in matchs]

        return ents

class IbanAnonymizer():
    '''
    Replace all credit card numbers
    '''

    def __init__(self, anonymization: Anonymization):
        self.anonymization = anonymization
        # matches an IBAN with optional spaces
        self.iban_regex = r'([A-Z]{2}[ \-]?[0-9]{2})(?=(?:[ \-]?[A-Z0-9]){9,30}$)((?:[ \-]?[A-Z0-9]{3,5}){2,7})([ \-]?[A-Z0-9]{1,3})?'
    
    def anonymize(self, text: str) -> str:
        return self.anonymization.regex_anonymizer(text, self.iban_regex, 'iban')

    def evaluate(self, text: str) -> str:
        matchs = re.finditer(self.iban_regex, text)
        ents = [SimpleNamespace(start=m.start(), end=m.end(), entity_type="IBAN_CODE", score=1) for m in matchs]

        return ents