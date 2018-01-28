from django import forms


class LoginForm(forms.Form):
    email_address = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'mdl-textfield__input',
        'id': 'login'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'mdl-textfield__input',
        'type': 'password',
        'id': 'password'
    }))
