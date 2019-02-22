# anonymization

Text anonymization in many languages for python3.6+ using [Faker](https://github.com/joke2k/faker).

## install

```bash
pip install anonymization
```

## example

### Replace a french phone number with a fake one

```python
>>> from anonymization import Anonymization, PhoneNumberAnonymizer
>>>
>>> text = "C'est bien le 0611223344 ton numéro ?"
>>> anon = Anonymization('fr_FR')
>>> phoneAnonymizer = PhoneNumberAnonymizer(anon)
>>> phoneAnonymizer.anonymize(text)
"C'est bien le 0144939332 ton numéro ?"
```

### Replace emails and named entities in english

This example use NamedEntitiesAnonymizer which require [spacy](https://spacy.io) and a spacy model.

```bash
pip install spacy
python -m spacy download en
```

```python
>>> from anonymization import Anonymization, AnonymizerChain, EmailAnonymizer, NamedEntitiesAnonymizer

>>> text = "Hi John,\nthanks for you for subscribing to Superprogram, feel free to ask me any question at secret.mail@Superprogram.com \n Superprogram the best program!"
>>> anon = AnonymizerChain(Anonymization('en_US'))
>>> anon.add_anonymizers(EmailAnonymizer, NamedEntitiesAnonymizer('en'))
>>> anon.anonymize(text)
'Hi Holly,\nthanks for you for subscribing to Ariel, feel free to ask me any question at shanestevenson@gmail.com \n Ariel the best program!'
```

## included anonymizers

### files

| name                                                                         | lang                        |
|------------------------------------------------------------------------------|-----------------------------|
| [FilePathAnonymizer](anonymization/anonymizers/fileAnonymizers.py)           | -                           |

### internet

| name                                                                         | lang                        |
|------------------------------------------------------------------------------|-----------------------------|
| [EmailAnonymizer](anonymization/anonymizers/internetAnonymizers.py)          | -                           |
| [UriAnonymizer](anonymization/anonymizers/internetAnonymizers.py)            | -                           |
| [MacAddressAnonymizer](anonymization/anonymizers/internetAnonymizers.py)     | -                           |
| [Ipv4Anonymizer](anonymization/anonymizers/internetAnonymizers.py)           | -                           |
| [Ipv6Anonymizer](anonymization/anonymizers/internetAnonymizers.py)           | -                           |

### phone numbers

| name                                                                         | lang                        |
|------------------------------------------------------------------------------|-----------------------------|
| [PhoneNumberAnonymizer](anonymization/anonymizers/phoneNumberAnonymizers.py) | [47+](https://github.com/joke2k/faker/tree/master/faker/providers/phone_number) |
| [msisdnAnonymizer](anonymization/anonymizers/fileAnonymizers.py)             | [47+](https://github.com/joke2k/faker/tree/master/faker/providers/phone_number) |

### spacy

| name                                                                         | lang                        |
|------------------------------------------------------------------------------|-----------------------------|
| [NamedEntitiesAnonymizer](anonymization/anonymizers/spacyAnonymizers.py)     | [7+](https://spacy.io/usage/models) |

## Contribution

Contributions are welcome both to improve the code base and add new anonymizers. Feel free to open PR & issues.

For new anonymizers, make sure:

- that they works in as many languages as possible
- to use type hinting
- to document them in table