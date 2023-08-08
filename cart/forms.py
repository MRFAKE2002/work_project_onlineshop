from django import forms

class AddProductToCartForm(forms.Form):
    QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 30)]
    
    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)

    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput)
    
    color = forms.CharField(max_length=100)

    size = forms.CharField(max_length=100)
