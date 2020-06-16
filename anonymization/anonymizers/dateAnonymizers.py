import re
from types import SimpleNamespace

from ..Anonymization import Anonymization

class DateAnonymizer():
    '''
    Replace the dates with fake ones

        Date Formats: DD/MM/YYYY or DD/MM/YY
    '''

    def __init__(self, anonymization: Anonymization):
        self.anonymization = anonymization
        self.date_regex= r'(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})|(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))|(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})'

    def anonymize(self, text: str) -> str:
        return  self.anonymization.regex_anonymizer(text,self.date_regex,'date')

    def evaluate(self, text: str) -> str:
        matchs = re.finditer(self.date_regex, text)
        ents = [SimpleNamespace(start=m.start(), end=m.end(), entity_type="DATE", score=1) for m in matchs]
        return ents

