from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()
class RegisterForm(forms.Form):
    username = forms.CharField(
        label="Nom d'utilisateur",
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "w-full p-2 mb-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Nom d'utilisateur"
        })
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "w-full p-2 mb-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Email"
        })
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            "class": "w-full p-2 mb-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Mot de passe"
        })
    )
    confirm_password = forms.CharField(
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput(attrs={
            "class": "w-full p-2 mb-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Confirmer le mot de passe"
        })
    )
    phone = forms.CharField(
        label="Téléphone",
        max_length=15,
        widget=forms.TextInput(attrs={
            "class": "w-full p-2 mb-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Numéro de téléphone"
        })
    )
    is_owner = forms.BooleanField(
        label="Êtes-vous propriétaire ?",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "mr-2"})
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Un utilisateur avec cet email existe déjà.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError("Le mot de passe et la confirmation ne correspondent pas.")
        return cleaned_data

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        # Ici tu peux sauvegarder phone ou is_owner dans ton Profile si tu en as un
        return user
