from django import forms
from .models import *
from django.core.exceptions import ValidationError


# def validate_name(value):
#     try:
#         Publisher.objects.get(name=value)
#         raise ValidationError("%s的信息已经存在" % value)
#     except Publisher.DoesNotExist:
#         pass


class PublisherForm(forms.ModelForm):
    # name = forms.CharField(validators=[validate_name])

    class Meta:
        model = Publisher
        fields = '__all__'
