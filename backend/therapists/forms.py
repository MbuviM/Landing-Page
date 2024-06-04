# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from .models import User

class SearchForm(forms.Form):
    location = forms.CharField(max_length=100, required=False, label='Enter location')
    therapy = forms.CharField(max_length=100, required=False, label='Enter type of therapy')

class CreateUserForm(UserCreationForm):
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }

    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )

    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise ValidationError(("Your password must contain at least 8 characters."), code='password_too_short')
        if password1.isdigit():
            raise ValidationError(("Your password can't be entirely numeric."), code='password_entirely_numeric')
        # Add more custom validation as needed
        return password1

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return cleaned_data

class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Invalid username or password. Please try again.",
        'inactive': "This account is inactive.",
    }

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(max_length=100)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError("This email is not associated with any account.")
        return email