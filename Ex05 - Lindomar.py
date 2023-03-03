num_list = []
pares_list = []
impares_list = []

while True:
    num = int(input(f"Digite um número: "))
    num_list.append(num)
    continuar = input(f"Deseja continuar?Digite S ou N. ").lower()
    if continuar != "s":
        for num in num_list:
            if num % 2 == 0:
                pares_list.append(num)
            else:
                impares_list.append(num)
        break

print(f"Lista: ", num_list)
print(f"Pares: ", pares_list)
print(f"Impares: ", impares_list)

