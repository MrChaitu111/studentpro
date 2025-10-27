from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'student_id': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'student_date_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'student_age': forms.NumberInput(attrs={'class': 'form-control'}),
            'student_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'student_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
        }