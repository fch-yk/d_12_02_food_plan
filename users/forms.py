from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': 'Введите адрес эл.почты'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'username', 'name': 'username'}), required=False)
    email = forms.CharField(widget=forms.EmailInput(), required=False, disabled=True)
    avatar = forms.ImageField(widget=forms.FileInput(), required=False) 
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password1', 'name': 'password1'}), required=False)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password2', 'name': 'password2'}), required=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'