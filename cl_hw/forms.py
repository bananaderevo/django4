from django import forms


class SendMailForm(forms.Form):
    email = forms.EmailField()
    text = forms.CharField(min_length=5, max_length=300)
    time = forms.DateTimeField(widget=forms.SelectDateWidget)
