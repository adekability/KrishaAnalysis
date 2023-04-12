import pandas
from dataclasses import dataclass


@dataclass
class Dataset:
    filename: str

    def get_data(self):
        dataframe = pandas.read_excel(self.filename)
        return dataframe
