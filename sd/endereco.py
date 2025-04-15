


entrada = input()
vetor = list(entrada)

lista=[]
i=0
while i <len(vetor):
  lista.append(int(vetor[i]))
  i+=1

print(vetor)
print(lista)

x=0 
soma = 0
potencia = 12
while x < len(lista):
  bit = lista[x]
  soma = bit*(2**potencia)
  soma+= soma
  potencia = potencia - 1
  x+=1
  print(f'bit: {bit} x 2^{potencia} = {soma}')
  print(f'potencia: {x} {potencia}')
  print(f'soma: {soma}')



# bit1 = lista[0]*2**11
# bit2 = lista[1]*2**10
# bit3 = lista[2]*2**9
# bit4 = lista[3]*2**8
# bit5 = lista[4]*2**7
# bit6 = lista[5]*2**6
# bit7 = lista[6]*2**5
# bit8 = lista[7]*2**4
# bit9 = lista[8]*2**3
# bit10 = lista[9]*2**2
# bit11 = lista[10]*2**1
# bit12 = lista[11]*2**0
# soma = bit1 + bit2 + bit3 + bit4 + bit5 + bit6 + bit7 + bit8 + bit9 + bit10 + bit11
print('p')