from django import forms

from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'first_name', 'middle_name', 'last_name', 'role']
        
        widgets = {
            'password': forms.PasswordInput()
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        
        password = self.cleaned_data.get('password')
        user.set_password(password)
        
        if commit:
            user.save()
        
        return user
    
class LoginForm(forms.Form):
    class Meta:
        email = forms.EmailField()
        password = forms.CharField(widget=forms.PasswordInput())