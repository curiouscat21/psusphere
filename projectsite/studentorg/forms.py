from django.forms import ModelForm
from django import forms
from .models import Organization
from .models import OrgMember
from .models import Student
from .models import College
from .models import Program

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"

class OrgMemberForm(forms.ModelForm):
    class Meta:
        model = OrgMember
        fields = ['student', 'organization', 'date_joined']
        widgets = {
            'date_joined': forms.DateInput(attrs={'type': 'date'})
        }

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__" 

class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = "__all__" 
        

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = "__all__" 

