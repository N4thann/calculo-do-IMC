import os

print('#'*50)
print('Cálculo do IMC - Indice de massa corporal'.center(50))
print('#'*50)

nome = input('Digite o seu nome: ')
peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em cm: '))

imc = peso / (altura ** 2)

print('Seu nome é ', nome, ' e seu IMC é ', round(imc,2))
print('')
print('')
if imc < 18.5:
    print(nome, ' você está abaixo do peso')
elif (imc >= 18.5) and (imc < 25):
    print(nome, ' você está com peso ideal')
elif (imc >= 25) and (imc < 40):
    print(nome, ' você está com sobrepeso')
else:
    print(nome, ' você está obeso')
print('')
print('')
print('#'*50)
print('Obrigado!'.center(50))
print('#'*50)

os.system('pause')
