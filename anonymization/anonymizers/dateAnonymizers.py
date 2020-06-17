import re
from types import SimpleNamespace

from ..Anonymization import Anonymization

class DateAnonymizer():
    '''
    Replace the dates with fake ones

        Date Formats: DD/MMM/YYYY or DD.MMM.YYYY  or DD-MMM-YYYY or DD MMM YYYY
    '''

    def __init__(self, anonymization: Anonymization):
        self.anonymization = anonymization
        self.date_regex= r'\d\d(?:\/|-|\.|\s)(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(?:\/|-|\.|\s)\d{4}'

    def anonymize(self, text: str) -> str:
        return  self.anonymization.regex_anonymizer(text,self.date_regex,'date')

    def evaluate(self, text: str) -> str:
        matchs = re.finditer(self.date_regex, text)
        ents = [SimpleNamespace(start=m.start(), end=m.end(), entity_type="DATE", score=1) for m in matchs]
        return ents

