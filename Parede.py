larg = float(input('Qual a largura da sua parede em metros?: '))
alt = float(input('Agora, qual a altura dela?: '))
area = larg*alt
print ('A dimensão da sua parede é de {} X {}, e sua área é de {:.3f}m²'.format (larg, alt, area))
print ('Para poder pintar a sua parede você necessitaria de {:.3f}L de tinta'.format (area/2))