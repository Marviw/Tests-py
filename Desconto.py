produto = float(input('Qual o valor do produto?:R$'))
desconto = float(input('Quanto é o desconto?:'))
final = produto - (produto * desconto/100)
print ('No final o produto ficaria no valor de R${:.2f} por conta do desconto de {}%'. format (final, desconto))