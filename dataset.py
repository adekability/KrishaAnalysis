""" dataset.py - module containing management with datasets"""

import pandas
from dataclasses import dataclass


@dataclass
class Dataset:
    """ class Dataset - has filename field, and method to fetch data from excel, csv """
    filename: str = "krisha_data.xlsx"

    @classmethod
    def fetch_dataframe(cls):
        """ fetch_dataframe - method fetching data from filename to pandas Dataframe"""
        file = pandas.read_excel(cls.filename)
        dataframe = pandas.DataFrame(file)
        return dataframe
