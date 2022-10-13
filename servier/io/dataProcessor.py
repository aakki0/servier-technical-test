import re
import pandas as pd


def clean_data(df, columns):
    """
        Clean the columns of the input dataframe from bad characters
        to avoid multiple values for the same journal/title
    """

    for column in columns:
        df[column] = df[column].apply(lambda x: re.sub(r'\\x[0-9A-Fa-z][0-9A-Fa-z]', r'', str(x)))
    return df


def process_data(pubmed, drugs, clinical_trials):
    """
        Process input data by finding for each drug :
            the list of journals,
            the list of trials
            and the list of medical publications mentioning the drug
        the result is a dataframe with detailed mapping for each drug
    """

    # Clean data
    columns_to_be_cleaned = ['journal']
    pubmed = clean_data(pubmed, columns_to_be_cleaned)
    clinical_trials = clean_data(clinical_trials, columns_to_be_cleaned)

    # adding a helper column to gather drugs and titles of trials/pubmed in the same dataframe
    pubmed['join'] = 1
    drugs['join'] = 1
    clinical_trials['join'] = 1
    pubmed_drugs_matching = drugs.merge(pubmed, on='join').drop('join', axis=1)
    trials_drugs_matching = drugs.merge(clinical_trials, on='join').drop('join', axis=1)

    # look up each drug in each title of pubmed or trial
    pubmed_drugs_matching['match'] = pubmed_drugs_matching.apply(
        lambda x: x.title.upper().find(x.drug.upper()), axis=1).ge(0)
    trials_drugs_matching['match'] = trials_drugs_matching.apply(
        lambda x: x.scientific_title.upper().find(x.drug.upper()), axis=1).ge(0)

    # gather all titles found for each drug in the same row
    # it makes it easier for displaying the output json file
    trials_drugs = trials_drugs_matching[trials_drugs_matching.match] \
        .groupby(['atccode', 'drug']) \
        .apply(lambda x: x[['scientific_title', 'date']].to_dict('records')) \
        .reset_index() \
        .rename(columns={0: 'trial'})

    pubmed_drugs = pubmed_drugs_matching[pubmed_drugs_matching.match] \
        .groupby(['atccode', 'drug']) \
        .apply(lambda x: x[['title', 'date']].to_dict('records')) \
        .reset_index() \
        .rename(columns={0: 'pubmed'})

    # get all the journal mentioning a drug through a trial or a medical publication
    journal_drugs_matching = pd.concat([
        trials_drugs_matching[trials_drugs_matching.match][['atccode', 'drug', 'journal', 'date']],
        pubmed_drugs_matching[pubmed_drugs_matching.match][['atccode', 'drug', 'journal', 'date']]
    ])

    # gather all journals name found for each drug in the same row
    journal_drugs = journal_drugs_matching \
        .groupby(['atccode', 'drug']) \
        .apply(lambda x: x[['journal', 'date']].to_dict('records')) \
        .reset_index() \
        .rename(columns={0: 'journal'})

    # merge all the titles/journals found by drug and output the result
    drugs_output = journal_drugs.merge(pubmed_drugs, on=['atccode', 'drug'], how='outer') \
        .merge(trials_drugs, on=['atccode', 'drug'], how='outer')

    return drugs_output
