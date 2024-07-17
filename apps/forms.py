from django.forms import ModelForm, ImageField

from apps.models import User


class ProfileForm(ModelForm):
    photo = ImageField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'name', 'phone_number', 'email')
