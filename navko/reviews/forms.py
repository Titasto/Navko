from django import forms

from reviews.models import Reviews


class ReviewForm(forms.ModelForm):
    text = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'review_text'}))

    class Meta:
        model = Reviews
        fields = ['text']

