from .models import Profile
from django import forms
from django.contrib.auth.forms import UserChangeForm

# class EditProfileForm(UserChangeForm):
#     username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form.control'}))
#     first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form.control'}))
#     class Meta:
#         model = Profile
#         fields = ('image','username','city')


class EditProfileForm(UserChangeForm):
    image = forms.ImageField(required=False, widget=forms.FileInput)
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form.control'}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form.control'}))
    class Meta:
        model = Profile
        fields = ('image','username','city')