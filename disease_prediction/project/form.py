from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'rating','content']
        widgets = {
            'name':forms.TextInput(attrs={'class':'re-name','placeholder':'Enter Your Name'}),
            'email':forms.EmailInput(attrs={'class':'re-name','placeholder':'Enter Your Email'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5,'class':'re-name'}),
            'content': forms.Textarea(attrs={'rows': 6,'placeholder':'Your Review'}),    
        }


class ImageUploadForm(forms.Form):
    image = forms.ImageField()