from Nite_Mode.models import PDFModel
from django import forms

class UploadPDFForm(forms.ModelForm):
    class Meta:
        model = PDFModel
        fields = ('title', 'pdf',)