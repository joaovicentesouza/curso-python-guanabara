dias_alugados = int(input("Quantos dias alugados? "))
km_rodados = float(input("Quantos km foram rodados? "))

print(f"O total a pagar é de R${dias_alugados*60 + km_rodados*0.15}")