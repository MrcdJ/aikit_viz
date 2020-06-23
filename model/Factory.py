from xlrd import open_workbook
from flask_restplus import fields
import re
from model import Result


# Singleton and Factory
class Factory:
    def __init__(self):
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance is None:
            self.instance = Factory(*args, **kwds)
        return self.instance

    @staticmethod
    def xl_to_Results(file):
        """ creates instance of Results, from an excel file which should be generated with 'aikit result' command """
        wb = open_workbook(file)
        sheet = wb.sheet_by_index(0)

        # Columns names and columns indexes we merge together
        header = [cell.value for cell in sheet.row(0)]

        merging_columns_dict = {'train_params': [], 'test_params': [], 'valid_params': []}
        train_pattern = '^train_'
        test_pattern = '^test_'
        valid_pattern = '^[a-z]'
        pattern = '^' + header[1] + '__'

        for col_idx in range(1, len(header)):
            if re.match(pattern, header[col_idx]):
                col_name = pattern[1:] + "params"
                if col_name not in merging_columns_dict:
                    merging_columns_dict[col_name] = []
                merging_columns_dict[col_name].append(col_idx)
            elif re.match(test_pattern, header[col_idx]):
                merging_columns_dict['test_params'].append(col_idx)
            elif re.match(train_pattern, header[col_idx]):
                merging_columns_dict['train_params'].append(col_idx)
            elif re.match(valid_pattern, header[col_idx]):
                merging_columns_dict['valid_params'].append(col_idx)
            else:
                merging_columns_dict[header[col_idx]] = [col_idx]
                pattern = '^' + header[col_idx] + '__'

        # Result
        results = {}
        for row_idx in range(1, sheet.nrows):
            row = [int(cell.value) if isinstance(cell.value, float) else cell.value
                   for cell in sheet.row(row_idx)]

            # "hasblock" columns
            data = {header[0]: row[0]}
            for i in range(1, 4):
                data[header[i]] = row[i]
            # other columns
            for key in merging_columns_dict.keys():
                if key not in data:
                    data[key] = {}
                for col_idx in merging_columns_dict[key]:
                    data[key][header[col_idx]] = row[col_idx]
                    
            results[row[0]] = Result.Result(data)

        return Result.Results(results)

    @staticmethod
    def swagger_Results():
        """ defines json format required for Result """
        return {'result': fields.Raw()}

