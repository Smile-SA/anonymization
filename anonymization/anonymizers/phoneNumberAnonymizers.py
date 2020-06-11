import re
from types import SimpleNamespace

import faker

from ..Anonymization import Anonymization

class PhoneNumberAnonymizer():
    '''
    Replace phone numbers of the anonymization locale with fake ones
    see https://faker.readthedocs.io/en/stable/providers/faker.providers.phone_number.html
    '''

    def __init__(self, anonymization: Anonymization):
        self.anonymization = anonymization
    
    def anonymize(self, text: str) -> str:
        formats = getattr(
            faker.providers.phone_number, 
            self.anonymization.locale
            ).Provider.formats

        for phone_nb_format in formats:
            safeFormat = re.escape(phone_nb_format.replace('#', '_'))
            regex = re.compile('\\b' + safeFormat.replace('_', '\d') + '\\b')
            
            text = self.anonymization.regex_anonymizer(text, regex, 'phone_number')

        return text
    
    def evaluate(self, text: str) -> str:
        formats = getattr(
            faker.providers.phone_number, 
            self.anonymization.locale
            ).Provider.formats

        ents = []

        for phone_nb_format in formats:
            safeFormat = re.escape(phone_nb_format.replace('#', '_'))
            regex = re.compile('\\b' + safeFormat.replace('_', '\d') + '\\b')

            matchs = re.finditer(regex, text)
            ents += [SimpleNamespace(start=m.start(), end=m.end(), entity_type="PHONE_NUMBER", score=1) for m in matchs]

        return ents

class msisdnAnonymizer():
    '''
    Replace msisdn of the anonymization locale with fake ones
    see https://en.wikipedia.org/wiki/MSISDN
    see https://faker.readthedocs.io/en/stable/providers/faker.providers.phone_number.html
    '''

    def __init__(self, anonymization: Anonymization):
        self.anonymization = anonymization
    
    def anonymize(self, text: str) -> str:
        msisdn_formats = getattr(
            faker.providers.phone_number, 
            self.anonymization.locale
            ).Provider.msisdn_formats

        for phone_nb_format in msisdn_formats:
            safeFormat = re.escape(phone_nb_format.replace('#', '_'))
            regex = re.compile('\\b' + safeFormat.replace('_', '\d') + '\\b')
            
            text = self.anonymization.regex_anonymizer(text, regex, 'msisdn')

        return text