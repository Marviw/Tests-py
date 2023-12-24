print('-'*42)
Dias = float(input ('Quantos dias alugado?:'))
KM = float(input('Quantos quilometros foram rodados?:'))
dr = Dias * 60
kmr = KM * 0.15
print ('='*42)
print ('Você andou {}Km por {:.0f} dias \nLogo você deve pagar R${:.2f} pelos dias \nE R${:.2f} pelos quilometros rodados\n No total ficaria R${:.2f}'.format(KM, Dias, dr, kmr, dr+kmr))
print ('='*42)