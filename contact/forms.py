
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100 , label='عنوان')
    email = forms.EmailField(required=False, label='ایمیل')
    message = forms.CharField(widget=forms.Textarea , label='پیام')

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("پیام خیلی کوتاه است!")
        return message

