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

    if meses >= pago_extra_mes_comienzo and meses <= pago_extra_mes_fin and saldo > pago_mensual:
        total_pagado = total_pagado + pago_mensual  + pago_extra
        saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra 
    elif saldo > pago_mensual:
       total_pagado = total_pagado + pago_mensual 
       saldo = saldo * (1+tasa/12) - pago_mensual 
    else:
        total_pagado = total_pagado + saldo 
        saldo = 0    
    print(meses, round(total_pagado,2), round(saldo,2)) 

print(f'Total pagado: {round(total_pagado, 2)} Meses: {meses}')