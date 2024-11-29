from django import forms
from .models import Producto, RegistroReciclaje

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'cantidad']
        widgets = {
            'nombre': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Tipo de Producto',
            'descripcion': 'Descripción (opcional)',
            'cantidad': 'Cantidad',
        }

class RegistroReciclajeForm(forms.ModelForm):
    class Meta:
        model = RegistroReciclaje
        fields = ['producto', 'punto_reciclaje', 'fecha_entrega', 'observaciones']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'punto_reciclaje': forms.Select(attrs={'class': 'form-control'}),
            'fecha_entrega': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'producto': 'Producto',
            'punto_reciclaje': 'Punto de Reciclaje',
            'fecha_entrega': 'Fecha de Entrega',
            'observaciones': 'Observaciones (opcional)',
        }
