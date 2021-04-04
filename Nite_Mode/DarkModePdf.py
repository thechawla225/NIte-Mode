from pdf2jpg import pdf2jpg
import img2pdf
from PIL import Image , ImageChops
from PyPDF2 import PdfFileReader, PdfFileMerger
import os

maininputpath = ""
file_handles = []

def pdf_to_images(filename,inputpath,outputpath):
    inputpath = inputpath + filename
    pdf2jpg.convert_pdf2jpg(inputpath, outputpath, pages="ALL")

def image_to_pdf(filename,inputpath,base_dir):
    inputpath = inputpath + filename
    pdf_reader = PdfFileReader(open(inputpath, "rb"))
    num_pages = pdf_reader.numPages

    merger = PdfFileMerger()
    maininputpath = inputpath + "_dir" 
    inputpath = inputpath + "_dir/%d_" + filename + ".jpg"
    
    for i in range(num_pages):
        image = Image.open(inputpath %i)
        image = ImageChops.invert(image)
        image = image.save('temp.jpg')
        number = str(i)
        name = "temp" + number + ".pdf" 
        f1 = open(name,"wb+")
        file_handles.append(open(name,"wb+"))
        f2 = open("temp.jpg",'rb')
        file_handles[-1].write(img2pdf.convert(f2))
        merger.append(f1)
        file_handles[-1].close()
        print(file_handles[-1].name)
        os.remove(file_handles[-1].name)
        print("Deleted")
        os.remove(inputpath %i)
    
    finalpath = os.path.join(base_dir,'media\DarkFile.pdf') 
    with open(finalpath, 'wb') as f:
            merger.write(f)
   
    f2.close()
    merger.close()

    for fh in file_handles:
        fh.close()
    
    print("Moving on to maininputpath")
    os.removedirs(maininputpath)
    return num_pages