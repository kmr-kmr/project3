
from django.forms import Form, ModelForm
from .models import Users Books

class BooksForm(forms.ModelForm):
    """
    This is Model Form for model Books
    """

    class Meta:
        model = Books
        # If u want to access some field from model u can access like below
        #fields = ('title', 'pages', 'author',)


class FormBooks(forms.Form)
    """
    This is Normal form
    """

    pass


class UsersForm(forms.ModelForm):
    """
    This is Model form with extra addings with widget fields
    """
    password = forms.CharField(max_length = 50, widget = forms.PasswordInput())
    confirm_password = forms.CharField(max_length = 50, widget = forms.PasswordInput())

    class Meta:
        model = Users

        fields = ('name', 'username', 'email', 'date_of_birth')
        # to add widget to some fields from model
        
 #       widget {
 #       'password' : forms.PasswordInput(),
 #       'confirm_password': widget = forms.PasswordInput()
 #        }


class FormUsers(forms.ModelForm):
    """
    This is Users ModelForm overriding the main method
    """
    def __init__(self,*args, **kwargs):
        super(FormUsers, self).__init__(*args, **kwargs)
        ## if u want to over ride any model
        # u can write u r logic hear
    class Meta:
        model = Users

    def clean_username(self):
        try:
            User = Users.objects.get(username__iexact == self.cleaned_data['username'])
        except:
            User = self.cleaned_data['username']
        raise forms.ValidationError('User already exist with same user name')


    def clean(self):
        if 'pasword' in self.cleaned_data and 'confirm_password' in self.cleaned_dta:
            if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
     	        raise form.ValidationError("The two passwords does not match")
	return self.cleaned_data


