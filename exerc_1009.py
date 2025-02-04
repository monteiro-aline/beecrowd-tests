nome_vendedor = input('NOME DO VENDEDOR: ')
salario_fixo = float(input('SALÁRIO FIXO: '))
total_vendas = float(input('TOTAL DE VENDAS EM DINHEIRO: '))

total = (15 / 100 * total_vendas) + salario_fixo


print(f'TOTAL = R$ {total:.2f}')
