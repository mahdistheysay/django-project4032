from django import  forms
from django.contrib.auth import get_user_model # to have access to db
# made this to reduce limitations/حرف اولوشون باید بزرگ باشه



class ContactForm(forms.Form):
    fullName = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control'}),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control'}),
    )


class LoginForm(forms.Form):
    userName = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Enter username'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'Enter password'}),
    )

user = get_user_model()
class RegisterForm(forms.Form):
    userName = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Enter username'}),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control' , 'placeholder':'Enter email'}),

    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'Enter password'}),
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'Re-enter password'}),
    )

    def clean_userName(self):
        userName = self.cleaned_data.get('userName')
        query = user.objects.filter(username=userName)

        if query.exists():
            raise forms.ValidationError('Username already exists')

        return userName


    def clean_email(self):#validation
        email = self.cleaned_data.get('email')
        query = user.objects.filter(email=email)

        if query.exists():
            raise forms.ValidationError('email already exists')
        return email



    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError("Passwords don't match")

        return data
