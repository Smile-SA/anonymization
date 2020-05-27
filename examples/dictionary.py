from anonymization import Anonymization, DictionaryAnonymizer

dic = ['this', 'a', 'with', 'secret', 'is', 'to', 'a', 'message']
text = "This is a message to Marco with a secret: zedsdml"

anon = Anonymization(None)
dictionaryAnonymizer = DictionaryAnonymizer(dic)(anon)
print(dictionaryAnonymizer.anonymize(text))
