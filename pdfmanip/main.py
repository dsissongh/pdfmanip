from PyPDF2 import PdfFileWriter, PdfFileReader
#from pdfrw import PdfReader, PdfWriter, PageMerge


inputpdf = PdfFileReader(open('test1.pdf', 'rb'))
watermarkpdf = PdfFileReader(open('test2.pdf', 'rb'))
watermark = watermarkpdf.getPage(0)

for i in range(ipdf.getNumPages()):
    page = ipdf.getPage(i)
    page.mergePage(watermark)
    output.addPage(page)

with open('newfile.pdf', 'wb') as f:
   output.write(f)