from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div
from django import forms
from .models import ConferenceUser

# Import login form
from django.contrib.auth.forms import AuthenticationForm

class ConferenceUserForm(forms.ModelForm):
    class Meta:
        model = ConferenceUser
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'bio',
            'linkedin',
        ]
        # set password as password widget
        widgets = {
            'password': forms.PasswordInput(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.label_class = 'col-sm-4'
        self.helper.field_class = 'col-sm-8'
        self.helper.layout.append(Submit('submit', 'Register!'))

class LoginForm(AuthenticationForm):
    class Meta:
        model = ConferenceUser
        fields = [
            'username',
            'password',
        ]
        # set password as password widget
        widgets = {
            'password': forms.PasswordInput(),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set up crispy form helper
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.label_class = 'col-sm-4'
        self.helper.field_class = 'col-sm-8'
        self.helper.layout.append(Submit('submit', 'Login!'))
