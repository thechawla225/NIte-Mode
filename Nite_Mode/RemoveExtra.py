import os

def remove_extra_pdf(num_pages):
    for i in range(num_pages-1,-1,-1):
        number = str(i)
        name = "temp" + number + ".pdf"
        os.remove(name)
'''

remove_extra_pdf(5)
'''