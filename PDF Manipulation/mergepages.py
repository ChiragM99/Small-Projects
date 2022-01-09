# We want to merge multiple pdfs in order of args
import sys

inputs = sys.argv[1:] # : grabs all other args

def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger() # Object to merge pdfs
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('merged.pdf')

pdf_merger(inputs)