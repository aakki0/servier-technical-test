import re
from configparser import ConfigParser
from servier.io.dataHandler import read_input_files, write_output_file
from servier.io.dataProcessor import process_data
import sys


if __name__ == "__main__":
    """
        This pipeline is meant to read input files from data folder,
        process the data to find where each drug is mentioned (medical
        publications, trials and journals) and produce a json file 
        that represents these mentions as direct relations
    """

    # Read configuration file
    config_file = ConfigParser()
    config_file.read("conf/config.ini")

    # Read input data
    pubmed, drugs, clinical_trials = read_input_files(config_file)

    if pubmed is None and drugs is None and clinical_trials is None:
        sys.exit()

    # Transform data and apply necessary rules
    # the result is a dataframe containing the mapping between drugs, pubmed, trials and journals
    drugs_mapping = process_data(pubmed, drugs, clinical_trials)

    # Write output data
    write_output_file(config_file, drugs_mapping)
