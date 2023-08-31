
def categorizar_sueldo(sueldo_promedio):
    if sueldo_promedio < 300:
        return "Bajo"
    elif sueldo_promedio <= 900:
        return "Normal"
    else:
        return "Mejor de lo normal"

sueldos_por_mes = (300*6+500*4+700*2)

sueldo_promedio =(sueldos_por_mes/12)

categoria = categorizar_sueldo(sueldo_promedio)

print(f"Sueldo promedio de Juan: {sueldo_promedio:.0f} dólares")
print(f"Su sueldo es: {categoria}")