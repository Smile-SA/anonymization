from anonymization import Anonymization, AnonymizerChain, NamedEntitiesAnonymizer, EmailAnonymizer, PhoneNumberAnonymizer, Ipv4Anonymizer, CreditCardAnonymizer, IbanAnonymizer
from presidio_evaluator.presidio_analyzer import PresidioAnalyzer, ModelEvaluator
from presidio_evaluator.data_generator import read_synth_dataset

anon = AnonymizerChain(Anonymization('en_US'))
anon.add_anonymizers(EmailAnonymizer, Ipv4Anonymizer, IbanAnonymizer,
    CreditCardAnonymizer, PhoneNumberAnonymizer, NamedEntitiesAnonymizer('en_core_web_lg'))

class AnonymizationAnalyzerEngine:
    def analyze(self, text, language, all_fields, entities=None, correlation_id=None,
                score_threshold=None, trace=False):
        """
        analyzes the requested text, searching for the given entities
         in the given language
        :param text: the text to analyze
        :param entities: the text to search
        :param language: the language of the text
        :param all_fields: a Flag to return all fields
        :param correlation_id: cross call ID for this request
        of the requested language
        :param score_threshold: A minimum value for which
        to return an identified entity
        :param trace: Should tracing of the response occur or not
        :return: an array of the found entities in the text
        """
        return anon.evaluate(text)

if __name__ == "__main__":
    print("Reading dataset")
    input_samples = read_synth_dataset("./data/synth_dataset.txt")

    print("Preparing dataset by aligning entity names to Presidio's entity names")

    # Mapping between dataset entities and Presidio entities. Key: Dataset entity, Value: Presidio entity
    entities_mapping = {
        "PERSON": "PERSON",
        "EMAIL": "EMAIL_ADDRESS",
        "CREDIT_CARD": "CREDIT_CARD",
        "FIRST_NAME": "PERSON",
        "PHONE_NUMBER": "PHONE_NUMBER",
        "BIRTHDAY": "DATE_TIME",
        "DATE": "DATE_TIME",
        "DOMAIN": "DOMAIN",
        "CITY": "LOCATION",
        "ADDRESS": "LOCATION",
        "IBAN": "IBAN_CODE",
        "URL": "DOMAIN_NAME",
        "US_SSN": "US_SSN",
        "IP_ADDRESS": "IP_ADDRESS",
        "ORGANIZATION": "ORG",
        "O": "O",
    }

    updated_samples = ModelEvaluator.align_input_samples_to_presidio_analyzer(
        input_samples, entities_mapping
    )

    flatten = lambda l: [item for sublist in l for item in sublist]
    from collections import Counter

    count_per_entity = Counter(
        [
            span.entity_type
            for span in flatten(
                [input_sample.spans for input_sample in updated_samples]
            )
        ]
    )

    print("Evaluating samples")
    analyzer = PresidioAnalyzer(analyzer=AnonymizationAnalyzerEngine(), entities_to_keep=count_per_entity.keys())
    evaluated_samples = analyzer.evaluate_all(updated_samples)
    #
    print("Estimating metrics")
    score = analyzer.calculate_score(evaluation_results=evaluated_samples, beta=2.5)
    precision = score.pii_precision
    recall = score.pii_recall
    entity_recall = score.entity_recall_dict
    entity_precision = score.entity_precision_dict
    f = score.pii_f
    errors = score.model_errors
    #
    print("precision: {}".format(precision))
    print("Recall: {}".format(recall))
    print("F 2.5: {}".format(f))
    print("Precision per entity: {}".format(entity_precision))
    print("Recall per entity: {}".format(entity_recall))
    #
    FN_mistakes = [str(mistake) for mistake in errors if mistake.error_type == "FN"]
    FP_mistakes = [str(mistake) for mistake in errors if mistake.error_type == "FP"]
    other_mistakes = [
        str(mistake) for mistake in errors if not mistake.error_type in ["FN", "FP"]
    ]
    print(other_mistakes)

    fn = open("./data/fn_30000.txt", "w+", encoding="utf-8")
    fn1 = "\n".join(FN_mistakes)
    fn.write(fn1)
    fn.close()

    fp = open("./data/fp_30000.txt", "w+", encoding="utf-8")
    fp1 = "\n".join(FP_mistakes)
    fp.write(fp1)
    fp.close()

    mistakes_file = open("./data/mistakes_30000.txt", "w+", encoding="utf-8")
    mistakes1 = "\n".join(other_mistakes)
    mistakes_file.write(mistakes1)
    mistakes_file.close()

    from pickle import dump

    dump(evaluated_samples, open("./data/evaluated_samples_30000.pickle", "wb"))
