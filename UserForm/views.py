from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.contrib.auth.forms import AuthenticationForm
from UserForm.forms import UserForm
from django.urls import reverse_lazy

class homepage(FormView):
    form_class = UserForm
    template_name = 'home.html'
    success_url = reverse_lazy('login')
        
    
class loginpage(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    
    def get_success_url(self):
        role = self.request.get('role')
        if role == 'admin':
            return 'admin/'
        else:
            return reverse_lazy(str(role))
    
    
class studentpage(TemplateView):
    template_name = 'student.html'
  
    
class staffpage(TemplateView):
    template_name = 'staff.html'
    
    
class editorpage(TemplateView):
    template_name = 'editor.html'
