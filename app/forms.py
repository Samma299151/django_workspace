from django import forms

class CustomerSearchForm(forms.Form):
    customer_code = forms.CharField(max_length=6, label='得意先コード')