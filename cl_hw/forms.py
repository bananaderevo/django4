from django import forms


class SendMailForm(forms.Form):
    email = forms.EmailField()
    text = forms.CharField(label='text', min_length=1, max_length=300)
    time = forms.DateTimeField(widget=forms.SelectDateWidget())

    # def send_email(self):
    #     send_feedback_email_task.delay(
    #         self.cleaned_data['email'], self.cleaned_data['text'], self.cleaned_data['time']
    #     )