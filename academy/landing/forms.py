from django import forms
from .models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead  # связка формы с моделью Lead
        fields = ['name', 'last_name', 'phone_number']  # перечисление необходимых полей
