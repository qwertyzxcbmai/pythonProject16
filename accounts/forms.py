from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False, max_length=20)
    age = forms.IntegerField(required=False, min_value=1)

    class Meta:
        model = User
        fields = ("username", "email", "phone", "age", "password1", "password2")


class AdminRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False, max_length=20)
    age = forms.IntegerField(required=False, min_value=1)

    class Meta:
        model = User
        fields = ("username", "email", "phone", "age", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.phone = self.cleaned_data.get("phone")
        user.age = self.cleaned_data.get("age")
        user.is_admin_user = True
        user.is_staff = True
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
