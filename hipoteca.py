# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
meses = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0: 
    
    meses = meses + 1   

    if meses >= pago_extra_mes_comienzo and meses <= pago_extra_mes_fin:
        pago_mensual_ef = pago_mensual + pago_extra 
    else: 
       pago_mensual_ef = pago_mensual
    if pago_mensual_ef > saldo * (1 + tasa/12):
        pago_mensual_ef = saldo * (1 + tasa/12)
    saldo = saldo * (1 + tasa/12) - pago_mensual_ef
    total_pagado = total_pagado + pago_mensual_ef           
    print(meses, round(total_pagado,2), round(saldo,2)) 

print(f'Total pagado: {round(total_pagado, 2)} Meses: {meses}')