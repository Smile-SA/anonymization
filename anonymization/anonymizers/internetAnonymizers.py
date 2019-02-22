from ..Anonymization import Anonymization

class EmailAnonymizer():
    '''
    Replace email addresses with fake ones
    '''

    def __init__(self, anonymization: Anonymization):
        self.anonymization = anonymization
    
    def anonymize(self, text: str) -> str:
        return self.anonymization.regex_anonymizer(text, r'[\w\.-]+@[\w\.-]+\.\w+', 'email')

class UriAnonymizer():
    '''
    Replace uri addresses (ex: https://example.com/foo#bar) with fake ones
    '''

    def __init__(self, anonymization: Anonymization):
        self.anonymization = anonymization
    
    def anonymize(self, text: str) -> str:
        return self.anonymization.regex_anonymizer(text, r'(?:(?:[^:/?# ]+):)(?://(?:[^/?#]*))(?:[^?\s]*)', 'uri')

class MacAddressAnonymizer():
    '''
    Replace mac addresses with fake ones
    '''

    def __init__(self, anonymization: Anonymization):
        self.anonymization = anonymization
    
    def anonymize(self, text: str) -> str:
        return self.anonymization.regex_anonymizer(text, r'(?:[a-f0-9]{2}:){5}[a-f0-9]{2}', 'mac_address')

class Ipv4Anonymizer():
    '''
    Replace Ipv4 addresses with fake ones
    '''

    def __init__(self, anonymization: Anonymization):
        self.anonymization = anonymization
    
    def anonymize(self, text: str) -> str:
        return self.anonymization.regex_anonymizer(text, r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:\.)){3}(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))', 'ipv4')
        
class Ipv6Anonymizer():
    '''
    Replace Ipv6 addresses with fake ones
    '''

    def __init__(self, anonymization: Anonymization):
        self.anonymization = anonymization
    
    def anonymize(self, text: str) -> str:
        return self.anonymization.regex_anonymizer(text, r'(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9]))', 'ipv6')
        