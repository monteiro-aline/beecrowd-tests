valores = list(map(int, input().split()))

maiorAB = (valores[0] + valores[1] + abs(valores[0] - valores[1])) // 2
maior = (maiorAB + valores[2] + abs(maiorAB - valores[2])) // 2

print(f"{maior} eh o maior")
