from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError #


class registerForm(forms.ModelForm):
    passsword = forms.CharField(
        label= "Mot de passe",
        widget=forms.passwordInput #
    )
    confirm_password = forms.CharField(
        label= "Confirmer le mot de passe",
        widget=forms.passwordInput#
    )  
    phone = forms.CharField(
        label="Numéro de téléphone",
        max_length=15,
        required=True
    )   
    isOwner = forms.BooleanField(#
        label="Êtes-vous propriétaire?",
        required=False
    )   
    class Meta:
        model = User
        fields = ['username', 'email', 'passsword', 'confirm_password', 'phone', 'isOwner'] 
    def clean(self):#
        cleaned_data = super().clean()#
        email = cleaned_data.get("email")#
        if User.objects.filter(email=email).exists():
            raise ValidationError(#
                "Un utilisateur avec cet email existe déjà."
            )
        password = cleaned_data.get("passsword")#
        confirm_password = cleaned_data.get("confirm_password")#

        if password != confirm_password:
            raise ValidationError(#
                "Le mot de passe et la confirmation du mot de passe ne correspondent pas."
            )
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["passsword"])#
        if commit:
            user.save()
            phoneNuber=self.cleaned_data["phone"],#
            isOwner=self.cleaned_data["isOwner"]#

        return user
    