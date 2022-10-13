from configparser import ConfigParser
from servier.io.dataHandler import read_output_json_file


def get_journal_with_most_drug_mentions(config_file: ConfigParser):
    """
        # ad-hoc process

        Read the output json file and extract the journal(s) that
        mention drugs the most.
        The output is a list of journals that have the most
        mentions of drugs.
    """

    drug_mapping = read_output_json_file(config_file)[['drug', 'journal']]
    drug_journal = drug_mapping.explode('journal')

    drug_journal['journal_name'] = drug_journal.journal.apply(lambda x: x['journal'])
    drug_journal['nb_drugs_mentioned'] = drug_journal.groupby('journal_name')['drug'].transform('nunique')
    most_mention = drug_journal['nb_drugs_mentioned'].max()
    most_mentioning_journals = drug_journal[drug_journal['nb_drugs_mentioned'] == most_mention]\
        [['journal_name', 'nb_drugs_mentioned']].drop_duplicates()

    return most_mentioning_journals
