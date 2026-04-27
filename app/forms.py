from django import forms
from .models import ExamForm

class ExamFormForm(forms.ModelForm):
    class Meta:
        model = ExamForm
        exclude = ['user', 'status']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit() or len(phone) != 10:
            raise forms.ValidationError("Phone must be 10 digits")
        return phone