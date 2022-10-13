from configparser import ConfigParser
import pandas as pd


def read_input_files(config_file: ConfigParser):
    """
        Read input files from data path that should be read from
        the config file of the project.
        Three dataframes are produced that represent respectively
        medical publication (pubmed), drugs and clinical trials
    """

    # Get input files path from the configuration file
    input = config_file["input"]
    data_path = input["data_path"]
    pubmed_csv_path = data_path + "/" + input["pubmed_csv"] + "/pubmed.csv"
    pubmed_json_path = data_path + "/" + input["pubmed_json"] + "/pubmed.json"
    drugs_path = data_path + "/" + input["drugs"] + "/drugs.csv"
    clinical_trials_path = data_path + "/" + input["clinical_trials"] + "/clinical_trials.csv"

    # read data from the input files path
    try:
        pubmed_csv = pd.read_csv(pubmed_csv_path)
        pubmed_json = pd.read_json(pubmed_json_path)
        pubmed = pd.concat([pubmed_csv, pubmed_json])
        drugs = pd.read_csv(drugs_path)
        clinical_trials = pd.read_csv(clinical_trials_path)

        return pubmed, drugs, clinical_trials
    except:
        print("cannot load the data properly")
        return None, None, None


def write_output_file(config_file: ConfigParser, output_dataframe: pd.DataFrame):
    """
        Write the output json file from the input dataframe
        into the data path found in the configuration file.
        The json file name is retrieved from the conf file as well.
    """

    output = config_file["output"]
    output_path = output["data_path"] + "/" + output["file_name"] + ".json"
    with open(output_path, 'w') as f:
        f.write(output_dataframe.to_json(orient='records'))


def read_output_json_file(config_file: ConfigParser):
    """
        Read the json file that was created by the processing pipeline.
    """

    output = config_file["output"]
    output_path = output["data_path"] + "/" + output["file_name"] + ".json"

    try:
        return pd.read_json(output_path)
    except:
        print("cannot the json file properly")
        return None
