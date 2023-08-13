from django.db import models

class Venta(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    tipo_cliente = models.PositiveIntegerField()
    cantidad_hojas = models.PositiveIntegerField()
    precio_por_hoja = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def calcular_total(self):
        descuentos = {1: 0.05, 2: 0.08, 3: 0.12, 4: 0.15}

        if self.tipo_cliente in descuentos:
            descuento = descuentos[self.tipo_cliente]
        else:
            descuento = 0.0

        subtotal = self.cantidad_hojas * self.precio_por_hoja
        neto_por_pagar = subtotal * (1 - descuento)
        return subtotal, neto_por_pagar
