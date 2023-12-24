from django import forms 
from crud_data.models import shop_data

class shop_dataForm(forms.ModelForm):
    class Meta:
        model=shop_data
        fields=['date','trade_code','high','low','open','close','volume']