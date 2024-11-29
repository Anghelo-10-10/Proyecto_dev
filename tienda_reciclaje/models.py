from django.db import models

class Producto(models.Model):
    TIPO_PRODUCTO = [
        ('PC', 'Computadora'),
        ('TL', 'Teléfono'),
        ('TB', 'Celular'),
        ('OT', 'Otros'),
    ]

    nombre = models.CharField(max_length=100, choices=TIPO_PRODUCTO, verbose_name="Tipo de Producto")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    cantidad = models.PositiveIntegerField(default=1, verbose_name="Cantidad")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    def __str__(self):
        return f"{self.get_nombre_display()} - {self.cantidad}"

class PuntoReciclaje(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Punto de Reciclaje")
    direccion = models.TextField(verbose_name="Dirección")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    telefono = models.CharField(max_length=15, blank=True, verbose_name="Teléfono")

    def __str__(self):
        return self.nombre

class RegistroReciclaje(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    punto_reciclaje = models.ForeignKey(PuntoReciclaje, on_delete=models.CASCADE, verbose_name="Punto de Reciclaje")
    fecha_entrega = models.DateTimeField(verbose_name="Fecha de Entrega")
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")

    def __str__(self):
        return f"Reciclaje de {self.producto} en {self.punto_reciclaje}"