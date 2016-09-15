import xlrd
from xlrd.sheet import ctype_text


class FileProcesser():

    def __init__(self, route):
        self.route = route
        self.workbook = xlrd.open_workbook(self.route)
        self.sheet_names = self.workbook.sheet_names()
        print(self.workbook.sheet_by_index(0))
