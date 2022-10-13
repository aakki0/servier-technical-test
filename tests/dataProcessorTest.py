from configparser import ConfigParser

import pandas as pd
import pytest
from servier.io import dataProcessor, dataHandler

config_file = ConfigParser()
config_file.read("conf/config.ini")


def test_clean_data():
    data = {
        "id": [1, 2],
        "journal": ["journal 1", "journal 2\\x28"]
    }
    df = pd.DataFrame(data)
    cleaned_df = dataProcessor.clean_data(df, ['journal'])

    clean_data = {
        "id": [1, 2],
        "journal": ["journal 1", "journal 2"]
    }
    clean_df = pd.DataFrame(clean_data)

    assert (clean_df.compare(cleaned_df).__len__() == 0)


def test_process_data():
    data = {
        "atccode": "A01AD",
        "drug": "EPINEPHRINE",
        "journal": [[{"journal":"Journal of emergency nursing","date":"27 April 2020"}, {'journal': 'The journal of allergy and clinical immunology. In practice', 'date': '01/03/2020'}]],
        "pubmed": [[{"title":"Time to epinephrine treatment is associated with the risk of mortality in children who achieve sustained ROSC after traumatic out-of-hospital cardiac arrest.","date":"01/03/2020"}]],
        "trial": [[{"scientific_title":"Tranexamic Acid Versus Epinephrine During Exploratory Tympanotomy","date":"27 April 2020"}]]
    }
    expected_df = pd.DataFrame(data)
    pubmed, drugs, clinical_trials = dataHandler.read_input_files(config_file)
    results = dataProcessor.process_data(pubmed, drugs, clinical_trials)

    assert(results.compare(expected_df).__len__() == 0)
