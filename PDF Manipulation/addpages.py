import PyPDF2
from PyPDF2.pdf import PdfFileReader, PdfFileWriter

# open .pdf
with open('file.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0) 
    page.rotateClockwise(90) 
    writer = PdfFileWriter()
    writer.addPage(page) 
    with open('title.pdf', 'wb') as new_file: 
        writer.write(new_file) 


 