import xlrd
from xlrd.sheet import ctype_text
from peewee import *
from app import db
from app.mod_xls.models import Book, BaseModel


class FileProcesser():
    XLS_TO_MODEL = {
        "status": "státusz", "description_id": "műleírás Id", "book_id": "termék Id", "author": "szerző",
        "title": "cím", "publication_year": "kiadási év", "publisher": "kiadó", "barcode": "vonalkód",
        "storage_place": "tárolóhely", "picture_url": "kép", "price": "egységár", "uploaded": "felvitel dátuma",
        "sold_in_shop": "bolti eladás dátuma", "shop": "bolt", "weight": "súly", "number_of_pages": "oldalszám",
        "cover": "kötés (extra)", "quality": "minőség", "moreinfo": "moreinfo", "uploader": "feltöltő",
        "category": "kategória", "annotation": "annotáció", "publication_id": "kiadás Id", "isbn": "isbn"
    }

    def __init__(self, route):
        book = xlrd.open_workbook(route)
        sheet = book.sheet_by_index(0)

        self.dict_list = []
        for row in range(1, sheet.nrows):
            current_row = {}
            for column in range(sheet.ncols):
                current_row[sheet.cell(0, column).value] = sheet.cell(row, column).value
            self.dict_list.append(current_row)

    def add_to_database(self):
        print(self.XLS_TO_MODEL)
        # with db.atomic():
            # Book.insert_many(self.dict_list).execute()
