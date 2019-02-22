from ..Anonymization import Anonymization

class FilePathAnonymizer():
    '''
    Replace file paths such as 'some/file/path.ext' with a fake file path
    '''

    def __init__(self, anonymization: Anonymization):
        self.anonymization = anonymization
    
    def anonymize(self, text: str) -> str:
        return self.anonymization.regex_anonymizer(text, r'(?:\w+)(?:\/\w+)+\w+\.\w+', 'file_path')
