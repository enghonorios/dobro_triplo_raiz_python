#crie um algoritmo que leia o numero e mostre o seu dobro triplo e raiz quadrada

#recebe um numero do usuario
numero= int(input('Ano que você nasceu: '))
import math
resultado= numero
dobro= numero *2
triplo= numero *3
raiz_quadrada= math.sqrt(numero)

#mostra resultado na tela
print(f'O dobro de {numero} é {dobro}.')
print(f'O triplo de {numero} é {triplo}.')
print(f'A raiz quadrada de {numero} é {raiz_quadrada:.2f}.')
