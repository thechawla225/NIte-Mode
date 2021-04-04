
from pdf2jpg import pdf2jpg
import img2pdf
from PIL import Image , ImageChops
from PyPDF2 import PdfFileReader, PdfFileMerger
import os
import shutil
import re
import subprocess

file_handles = []

def do_Stuff(merger,name,inputpath,base_dir,i,finalpath):
    f1 = open(name,"wb+")
    file_handles.append(open(name,"wb+"))
    f2 = open("temp.jpg",'rb')
    file_handles[-1].write(img2pdf.convert(f2))
    merger.append(f1)
    f1.close()
    os.remove(inputpath %i)
    finalpath = os.path.join(base_dir,'media\DarkFile.pdf')
    with open(finalpath, 'wb') as f:
        merger.write(f)
    f2.close()
    merger.close()
    return finalpath
    
