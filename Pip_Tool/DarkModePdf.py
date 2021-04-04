from pdf2jpg import pdf2jpg
import img2pdf
from PIL import Image , ImageChops
from PyPDF2 import PdfFileReader, PdfFileMerger
import os

maininputpath = ""
file_handles = []


def pdf_to_images(filename,inputpath):
    outputpath = inputpath
    inputpath = os.path.join(inputpath,filename)
    pdf2jpg.convert_pdf2jpg(inputpath, outputpath, pages="ALL")

def image_to_pdf(filename,inputpath,outputpath):
    inputpath = os.path.join(inputpath,filename)
    pdf_reader = PdfFileReader(open(inputpath, "rb"))
    num_pages = pdf_reader.numPages

    maininputpath = inputpath + "_dir" 
    inputpath = inputpath + "_dir/%d_" + filename + ".jpg"
    
    for i in range(num_pages):
        merger = PdfFileMerger()
        if(i>=1):
            merger.append(PdfFileReader(open(finalpath, "rb")))
        image = Image.open(inputpath %i)
        image = ImageChops.invert(image)
        image = image.save('temp.jpg')
        number = str(i)
        name = "temp" + number + ".pdf"
        with open(name, 'wb+') as f1:
            file_handles.append(open(name,"wb+"))
            f2 = open("temp.jpg",'rb')
            file_handles[-1].write(img2pdf.convert(f2))
            merger.append(f1)
            os.remove(inputpath %i)
            
            finalpath = os.path.join(outputpath,'DarkFile.pdf') 
            with open(finalpath, 'wb') as f:
                merger.write(f)
            f2.close()
            merger.close()

    
   

    for fh in file_handles:
        fh.close()
    try:
        os.removedirs(maininputpath)
    except:
        pass
    pid = os.getpid()
    return num_pages,pid





