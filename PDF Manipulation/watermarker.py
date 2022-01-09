# Watermark a pdf file

template = PyPDF2.PdfFileReader(open('dummy.df', 'rb'))
watermark = PdfFileReader(open('wtm.pdf', 'rb'))
output = PdfFileWriter()

#we dont know how many pages dummy has. We want to make program flexible, no matter how many pages, we should be able to proces
for i in range(template.getNumPages()): 
    page = template.getPage(i) 
    page.mergePage(watermark.getPage(0)) 
    output.addPage(page)

    with open('wtrmked.pdf', 'wb') as file:
        output.write(file)