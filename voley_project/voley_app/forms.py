from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    # Hacemos el email opcional para mantener compatibilidad con flujos existentes.
    email = forms.EmailField(required=False, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # aplicar clases a widgets para que hereden estilos
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

    def save(self, commit=True):
        user = super().save(commit=False)
        email = self.cleaned_data.get('email')
        if email:
            user.email = email
        if commit:
            user.save()
        return user
