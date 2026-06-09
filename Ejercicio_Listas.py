'''El Escenario:
Eres el programador de una app de entrega de comida a domicilio. Tienes una lista con los montos de los últimos pedidos del día, pero hay un problema: ¡algunos montos se registraron en negativo por un error del sistema!

Tu misión es limpiar los datos y calcular el dinero real de la empresa.

Python
pedidos_sucios = [150, -20, 300, 0, -50, 450]'''



pedidos_sucios = [150, -20, 300, 0, -50, 450]
pedidos_validos = []
total_caja = 0
for pedido in pedidos_sucios:
    if pedido > 0:
        total_caja += pedido
        pedidos_validos.append(pedido)
print(f'Pedidos validos procesados: {pedidos_validos}')
print(f'El total neto en caja es: {total_caja}')