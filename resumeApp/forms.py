from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=250)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = ""
        self.fields['email'].label = ""
        self.fields['content'].label = ""

        self.fields['full_name'].widget.attrs['placeholder'] = 'Type your full name...'
        self.fields['content'].widget.attrs['placeholder'] = 'Type your message...'

        self.fields['email'].widget.attrs['name'] = 'email'
        self.fields['email'].widget.attrs['type'] = 'text'
        self.fields['email'].widget.attrs['placeholder'] = 'Type your email here'

        for field in ['full_name', 'email', 'content']:
            self.fields[field].help_text = None

