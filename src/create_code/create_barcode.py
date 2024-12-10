from barcode import EAN13
from barcode.writer import ImageWriter

def create_barcode(number):
    my_code = EAN13(number, writer=ImageWriter())
    my_code.save("new_code1")
    return  my_code