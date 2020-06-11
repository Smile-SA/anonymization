from anonymization import Anonymization, AnonymizerChain, EmailAnonymizer, NamedEntitiesAnonymizer

text = "Hi John,\nthanks for you for subscribing to Superprogram, feel free to ask me any question at secret.mail@Superprogram.com \n Superprogram the best program!"
anon = AnonymizerChain(Anonymization('en_US'))
anon.add_anonymizers(EmailAnonymizer, NamedEntitiesAnonymizer('en_core_web_lg'))
print(anon.anonymize(text))
