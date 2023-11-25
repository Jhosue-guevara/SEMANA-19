from django import forms
from .models import Productos,Proveedores

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'stock', 'fk_prov']
    
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['fk_prov'].queryset = Proveedores.objects.all()
