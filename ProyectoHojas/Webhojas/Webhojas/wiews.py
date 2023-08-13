from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Venta

@login_required
def crear_venta(request):
    if request.method == 'POST':
        nombre_cliente = request.POST['nombre_cliente']
        tipo_cliente = int(request.POST['tipo_cliente'])
        cantidad_hojas = int(request.POST['cantidad_hojas'])
        precio_por_hoja = float(request.POST['precio_por_hoja'])

        venta = Venta(nombre_cliente=nombre_cliente, tipo_cliente=tipo_cliente,
                      cantidad_hojas=cantidad_hojas, precio_por_hoja=precio_por_hoja)
        venta.save()
        return redirect('listar_ventas')

    return render(request, 'crear_venta.html')

@login_required
def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'listar_ventas.html', {'ventas': ventas})
