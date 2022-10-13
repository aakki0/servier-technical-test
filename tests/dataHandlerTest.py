from configparser import ConfigParser

import pandas as pd
import pytest
from servier.io import dataHandler

config_file = ConfigParser()
config_file.read("conf/config.ini")


def test_read_input_files():
    pubmed, drugs, clinical_trials = dataHandler.read_input_files(config_file)
    assert pubmed is not None and drugs is not None and clinical_trials is not None


def test_write_output_file():
    data = {
        "id": [31, 2],
        "drug": ["DIPHENHYDRAMINE", "ETHANOL"]
    }

    df = pd.DataFrame(data)
    dataHandler.write_output_file(config_file, df)

    output_path = config_file["output"]["data_path"] + "/" + config_file["output"]["file_name"] + ".json"
    output_df = pd.read_json(output_path)

    assert(df.compare(output_df).__len__() == 0)


def test_read_output_json_file():
    df = dataHandler.read_output_json_file(config_file)
    assert df is not None
