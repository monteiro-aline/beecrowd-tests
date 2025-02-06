# Utilize a fórmula: MaiorAB = (a+b+abs(a-b))/2
maior_numero = input().split()

a = int(maior_numero[0])
b = int(maior_numero[1])
c = int(maior_numero[2])

if a > b and a > c:
    print(f'{a} eh o maior')

elif b > a and b > c:
    print(f'{b} eh o maior')

else:
    print(f'{c} eh o maior')