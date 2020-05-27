from anonymization import Anonymization, PhoneNumberAnonymizer

text = "C'est bien le 0611223344 ton numéro ?"
anon = Anonymization('fr_FR')
phoneAnonymizer = PhoneNumberAnonymizer(anon)
print(phoneAnonymizer.anonymize(text))
