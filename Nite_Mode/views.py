from django.shortcuts import render
from Nite_Mode.DarkModePdf import pdf_to_images, image_to_pdf
import os
from django.core.files.storage import FileSystemStorage
from Nite_Mode.forms import UploadPDFForm
from django.http import HttpResponse
from django.core.files import File
import magic
from Nite_Mode.DarkModePptx import convert_pptx

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

inputpath = os.path.join(BASE_DIR,'media\\')
outputpath = os.path.join(BASE_DIR,'media')


def index(request):
    context={'a': 1}
    return render(request,'index.html',context)

def find_file_type(request):

    fileObj=request.FILES['filePath']
    fsObj=FileSystemStorage()
    filePathName=fsObj.save(fileObj.name,fileObj)
    filePathName=fsObj.url(filePathName)
    filename = filePathName[7:]
    filePathName = '.' + filePathName
    filecheck = magic.from_file(filePathName, mime=True)

    if(filecheck == 'application/pdf'):
        return convert_pdf(filename)
    elif(filecheck == 'application/vnd.openxmlformats-officedocument.presentationml.presentation'):
        return convert_pptx(BASE_DIR,filename,filePathName)
    else:
        return file_error(request)



def convert_pdf(filename):

    pdf_to_images(filename,inputpath,outputpath)
    num_pages = image_to_pdf(filename,inputpath,BASE_DIR)
    print(num_pages)


    path_to_file = os.path.join(BASE_DIR,'media\DarkFile.pdf')
    f = open(path_to_file, 'rb')
    myfile = File(f)
    response = HttpResponse(myfile, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=' + 'DarkFile.pdf'

    return response

def error_404(request, exception):
        data = {}
        return render(request,'error.html', data)

def error_500(request):
        data = {}
        return render(request,'error.html', data)

def error_403(request, exception):
        data = {}
        return render(request,'error.html', data)

def error_400(request,  exception):
        data = {}
        return render(request,'error.html', data)

def file_error(request):
    data = {}
    return render(request,'fileError.html', data)







    


# Create your views here.
