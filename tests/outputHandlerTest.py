from configparser import ConfigParser

import pandas as pd
import pytest
from servier.io import outputHandler


def test_get_journal_with_most_drug_mentions():
    config_file = ConfigParser()
    config_file.read("../servier/conf/config.ini")

    data = {
        "journal_name": ["Journal of emergency nursing", "The journal of maternal-fetal & neonatal medicine",
                         "Psychopharmacology"],
        "nb_drugs_mentioned": [2, 2, 2]
    }
    expected_df = pd.DataFrame(data)
    results = outputHandler.get_journal_with_most_drug_mentions(config_file).reset_index(drop=True)

    assert (results.compare(expected_df).__len__() == 0)



