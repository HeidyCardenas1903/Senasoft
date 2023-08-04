def calcular_total(nombre, tipo_cliente, cantidad, precio_por_hoja):
    descuentos = {1: 0.05, 2: 0.08, 3: 0.12, 4: 0.15}
    
    if tipo_cliente in descuentos:
        descuento = descuentos[tipo_cliente]
    else:
        descuento = 0.0
    
    subtotal = cantidad * precio_por_hoja
    neto_por_pagar = subtotal * (1 - descuento)
    
    imprimir_recibo(nombre, subtotal, neto_por_pagar)

def imprimir_recibo(nombre, subtotal, neto_por_pagar):
    print("Nombre del cliente:", nombre)
    print("Subtotal por pagar:", subtotal)
    print("Neto por pagar:", neto_por_pagar)