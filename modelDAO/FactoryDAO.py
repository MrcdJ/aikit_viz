from modelDAO import ResultDAO
from xlrd import open_workbook
import re


# Singleton and Factory
class FactoryDAO:
    def __init__(self):
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance is None:
            self.instance = FactoryDAO(*args, **kwds)
        return self.instance

    @staticmethod
    def xl_to_ResultDAO(file):
        wb = open_workbook(file)
        sheet = wb.sheet_by_index(0)

        # Columns names
        header = [cell.value for cell in sheet.row(0)]
        merging_columns_dict = {}
        pattern = '^' + header[1] + '__'
        for i in range(1, len(header)):
            if re.match(pattern, header[i]):
                col_name = pattern[1:] + "params"
                if col_name not in merging_columns_dict:
                    merging_columns_dict[col_name] = []
                merging_columns_dict[col_name].append(i)
            else:
                merging_columns_dict[header[i]] = [i]
                pattern = '^' + header[i] + '__'

        # Results
        results = {}
        for row_idx in range(1, sheet.nrows):
            row = [int(cell.value) if isinstance(cell.value, float) else cell.value
                   for cell in sheet.row(row_idx)]

            data = {}
            for key in merging_columns_dict.keys():
                if key not in data:
                    data[key] = []
                for col_idx in merging_columns_dict[key]:
                    data[key].append(row[col_idx])

            results[row[0]] = ResultDAO.ResultDAO(data)

        return ResultDAO.Response(results)

    @staticmethod
    def swagger_ResultDAO():
        """TODO"""
        resultDAO = ResultDAO()
        attributes = [attr for attr in dir(resultDAO) if not callable(getattr(resultDAO, attr)) and not attr.startswith("__")]

        swagger = {}
        for attr in attributes:
            swagger[attr] = type(attr).__name__

        return swagger

