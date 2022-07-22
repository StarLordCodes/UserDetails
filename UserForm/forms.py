from django import forms
from UserForm.models import User

roles = [('student', 'Student'), ('staff', 'Staff'), ('admin', 'Admin'), ('editor', 'Editor')]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
            'role': forms.Select(choices=roles),
        }
        fields = "__all__"
    
    
