import xlrd
from xlrd.sheet import ctype_text


class FileProcesser():

    def __init__(self, route):
        book = xlrd.open_workbook(route)
        sheet = book.sheet_by_index(0)
        keys = [sheet.cell(0, col_index).value for col_index in range(sheet.ncols)]

        dict_list = []
        for row in range(1, sheet.nrows):
            current_row = {}
            for column in range(sheet.ncols):
                current_row[sheet.cell(0, column).value] = sheet.cell(row, column).value
            dict_list.append(current_row)

        print(dict_list)
