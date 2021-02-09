from django.shortcuts import render
from Nite_Mode.DarkModePdf import pdf_to_images, image_to_pdf
import os
from django.core.files.storage import FileSystemStorage
from Nite_Mode.forms import UploadPDFForm
from django.http import HttpResponse
from django.core.files import File

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

inputpath = os.path.join(BASE_DIR,'media\\')
outputpath = os.path.join(BASE_DIR,'media')


def index(request):
    context={'a': 1}
    return render(request,'index.html',context)

def convert_pdf(request):

    fileObj=request.FILES['filePath']
    fsObj=FileSystemStorage()
    filePathName=fsObj.save(fileObj.name,fileObj)
    filePathName=fsObj.url(filePathName)
    print("This is filePathName")
    filename = filePathName[7:]
    print(filename)
    predictedLabel = "Process Complete Check Folder"

    pdf_to_images(filename,inputpath,outputpath)
    num_pages = image_to_pdf(filename,inputpath,BASE_DIR)
    print(num_pages)

    context={'predictedLabel': predictedLabel}

    path_to_file = os.path.join(BASE_DIR,'media\Main.pdf')
    f = open(path_to_file, 'rb')
    myfile = File(f)
    response = HttpResponse(myfile, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=' + 'Main.pdf'

    return response




    


# Create your views here.
