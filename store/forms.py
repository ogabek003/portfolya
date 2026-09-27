from django import forms
from django.contrib.auth.models import User

from .models import ContactMessage


# =========================
# REGISTER
# =========================

class RegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label="Parol",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]

    def clean_username(self):

        username = self.cleaned_data["username"]

        if User.objects.filter(
            username=username
        ).exists():

            raise forms.ValidationError(
                "Bu username allaqachon band."
            )

        return username

    def save(self, commit=True):

        user = super().save(
            commit=False
        )

        user.set_password(
            self.cleaned_data["password1"]
        )

        if commit:
            user.save()

        return user


# =========================
# CONTACT MESSAGE
# =========================

class ContactMessageForm(forms.ModelForm):

    class Meta:

        model = ContactMessage

        fields = [
            "name",
            "email",
            "phone",
            "message",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "placeholder": "Ismingizni kiriting"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Emailingizni kiriting"
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "placeholder": "+998 90 123 45 67"
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "placeholder": "Xabaringizni yozing...",
                    "rows": 6
                }
            ),
        }