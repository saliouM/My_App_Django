from django import forms

from .import models

#Formulaire de téléchargement des photo

class PhotoForm(forms.ModelForm):
    edit_photo = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model=models.Photo
        fields=['image', 'caption']

class BlogForm(forms.ModelForm):
    edit_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Blog
        fields = ['title', 'content']
        
# permet de supprimer un blog    
class DeleteBlogForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)

class DeletePhotoForm(forms.Form):
    delete_photo = forms.BooleanField(widget=forms.HiddenInput, initial=True)