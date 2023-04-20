""" dataset.py - module containing management with datasets"""

import pandas
from dataclasses import dataclass


@dataclass
class Dataset:
    """ class Dataset - has filename field, and method to fetch data from excel, csv """
    filename: str

    def fetch_dataframe(self):
        """ fetch_dataframe - method fetching data from filename to pandas Dataframe"""
        dataframe = pandas.read_excel(self.filename)
        return dataframe
