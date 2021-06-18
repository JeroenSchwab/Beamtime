from django import forms
from .models import Add_file_model

#DataFlair #File_Upload
class Add_file_form(forms.ModelForm):
    class Meta:
        model = Add_file_model
        fields = [
        'file',
        'Project_Code',
        ]