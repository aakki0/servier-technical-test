# Servier
Technical test for Servier

This repository is organised to contain : 
- The pipeline code `main.py`. It should be used to run the pipeline.
- data in the `servier/data` folder
- configuration file in `servier/conf` folder
- helper modules to handle data in `servier/io` folder
- tests available in `tests` folder
- The `questions` folder contains the answers for the questions asked in the tech in the Test. The folder `questions/sql` for SQL queries and the folder `questions/improvements` for the data engineering part. 

Install
-------

Create a virtualenv and activate it :

    $ python3 -m venv venv
    $ . venv/bin/activate
    $ pip install -r requirements.txt

Or on Windows cmd :

    $ python3 -m venv venv
    $ venv\Scripts\activate.bat
    $ pip install -r requirements.txt

Install servier :

    $ pip install -e .


Test
----

    $ pip install '.[test]'
    $ pytest

Or on Windows cmd :

    $ pip install .[test]
    $ pytest

Run
----

The `main.py` file should be th entry point to run the pipeline.
