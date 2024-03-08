from django import forms


class MyInputForm(forms.Form):

    username = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')


class MyConfirmForm(forms.Form):

    confirm = forms.ChoiceField(choices=((1, 'less'), (2, 'more'), (3, 'correct')),
                                label="Is this your number?",)
