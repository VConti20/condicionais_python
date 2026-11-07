km=float(input("Distancia de entrega (km): "))

if km <= 5:
    frete = 0
elif km <= 15:
    frete=8
else:
    frete=15

print(f"Frete : R$ {frete:.2f}")
