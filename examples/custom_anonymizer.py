from anonymization import Anonymization

text = "This is a message to Marco"

class MarcoAnonymizer():
    '''
    Replace all occurences of Marco or marco with a star (*)
    '''
    def __init__(self, anonymization: Anonymization):
        self.anonymization = anonymization

    def anonymize(self, text: str) -> str:
        return text.replace(r'Marco', '*')

anon = Anonymization(None)
marcoAnonymizer = MarcoAnonymizer(anon)
print(marcoAnonymizer.anonymize(text))