peca1 = input().split()
codigo = int(peca1[0])
quantidade = int(peca1[1])
valor = float(peca1[2])

peca2 = input().split()
codigo2 = int(peca2[0])
quantidade2 = int(peca2[1])
valor2 = float(peca2[2])

total = (quantidade * valor) + (quantidade2 * valor2)


print(f'VALOR A PAGAR: R$ {total:.2f}')

