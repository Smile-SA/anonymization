# Anonymization

Text anonymization in many languages for python3.6+ using [Faker](https://github.com/joke2k/faker).

## Install

```bash
pip install anonymization
```

## Example

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
>>> anon.add_anonymizers(EmailAnonymizer, NamedEntitiesAnonymizer('en_core_web_lg'))
>>> anon.anonymize(text)
'Hi Holly,\nthanks for you for subscribing to Ariel, feel free to ask me any question at shanestevenson@gmail.com \n Ariel the best program!'
```

Or make it reversible with pseudonymize:

```python
>>> from anonymization import Anonymization, AnonymizerChain, EmailAnonymizer, NamedEntitiesAnonymizer

>>> text = "Hi John,\nthanks for you for subscribing to Superprogram, feel free to ask me any question at secret.mail@Superprogram.com \n Superprogram the best program!"
>>> anon = AnonymizerChain(Anonymization('en_US'))
>>> anon.add_anonymizers(EmailAnonymizer, NamedEntitiesAnonymizer('en_core_web_lg'))
>>> clean_text, patch = anon.pseudonymize(text)

>>> print(clean_text)
'Christopher, \nthanks for you for subscribing to Audrey, feel free to ask me any question at colemanwesley@hotmail.com \n Audrey the best program!'

revert_text = anon.revert(clean_text, patch)

>>> print(text == revert_text)
true
```

### Replace a french phone number with a fake one

Our solution supports many languages along with their specific information formats.

For example, we can generate a french phone number:

```python
>>> from anonymization import Anonymization, PhoneNumberAnonymizer
>>>
>>> text = "C'est bien le 0611223344 ton numéro ?"
>>> anon = Anonymization('fr_FR')
>>> phoneAnonymizer = PhoneNumberAnonymizer(anon)
>>> phoneAnonymizer.anonymize(text)
"C'est bien le 0144939332 ton numéro ?"
```

More examples in [/examples](/examples)

## Included anonymizers

### Files

| name                                                                         | lang                        |
|------------------------------------------------------------------------------|-----------------------------|
| [FilePathAnonymizer](https://github.com/alterway/anonymization/blob/master/anonymization/anonymizers/fileAnonymizers.py)           | -                           |

### Internet

| name                                                                         | lang                        |
|------------------------------------------------------------------------------|-----------------------------|
| [EmailAnonymizer](https://github.com/alterway/anonymization/blob/master/anonymization/anonymizers/internetAnonymizers.py)          | -                           |
| [UriAnonymizer](https://github.com/alterway/anonymization/blob/master/anonymization/anonymizers/internetAnonymizers.py)            | -                           |
| [MacAddressAnonymizer](https://github.com/alterway/anonymization/blob/master/anonymization/anonymizers/internetAnonymizers.py)     | -                           |
| [Ipv4Anonymizer](https://github.com/alterway/anonymization/blob/master/anonymization/anonymizers/internetAnonymizers.py)           | -                           |
| [Ipv6Anonymizer](https://github.com/alterway/anonymization/blob/master/anonymization/anonymizers/internetAnonymizers.py)           | -                           |

### Phone numbers

| name                                                                         | lang                        |
|------------------------------------------------------------------------------|-----------------------------|
| [PhoneNumberAnonymizer](https://github.com/alterway/anonymization/blob/master/anonymization/anonymizers/phoneNumberAnonymizers.py) | [47+](https://github.com/joke2k/faker/tree/master/faker/providers/phone_number) |
| [msisdnAnonymizer](https://github.com/alterway/anonymization/blob/master/anonymization/anonymizers/fileAnonymizers.py)             | [47+](https://github.com/joke2k/faker/tree/master/faker/providers/phone_number) |

## Date

| name                                                                         | lang                        |
|------------------------------------------------------------------------------|-----------------------------|
| [DateAnonymizer](https://github.com/alterway/anonymization/blob/master/anonymization/anonymizers/dateAnonymizers.py)               | -                           |

### Other

| name                                                                         | lang                        |
|------------------------------------------------------------------------------|-----------------------------|
| [NamedEntitiesAnonymizer](https://github.com/alterway/anonymization/blob/master/anonymization/anonymizers/spacyAnonymizers.py)     | [7+](https://spacy.io/usage/models) |
| [DictionaryAnonymizer](https://github.com/alterway/anonymization/blob/master/anonymization/anonymizers/dictionaryAnonymizers.py)   | -                           |

## Custom anonymizers

Custom anonymizers can be easily created to fit your needs:

```python
class CustomAnonymizer():
    def __init__(self, anonymization: Anonymization):
        self.anonymization = anonymization

    def anonymize(self, text: str) -> str:
        return modified_text
        # or replace by regex patterns in text using a faker provider
        return self.anonymization.regex_anonymizer(text, pattern, provider)
        # or replace all occurences using a faker provider
        return self.anonymization.replace_all(text, matchs, provider)
```

You may also add new faker provider with the helper `Anonymization.add_provider(FakerProvider)` or access the faker instance directly `Anonymization.faker`.

## Benchmark

This module is benchmarked on [synth_dataset](benchmark/data/synth_dataset.txt) from [presidio-research](https://github.com/microsoft/presidio-research) and returns accuracy result(**0.79**) better than Microsoft's solution(**0.75**)

You can run the benchmark using docker:

```bash
docker build . -f ./benchmark/dockerfile -t anonbench
docker run -it --rm --name anonbench anonbench
```

## License

MIT
