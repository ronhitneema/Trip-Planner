import pandas as pd

class ExcelReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_sheet(self, sheet_name=None):
        df = pd.read_excel(self.file_path, index_col=None, header=None)
        data = []
        for index, row in df.iterrows():
            data.append(row.tolist())

        return data