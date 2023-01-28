from django import forms

from . models import Blog



class BlogPostFrom(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'category']
        labels = {'title':'Title', 'description':'Description'}
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'})
            }

