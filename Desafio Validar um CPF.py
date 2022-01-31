cpf=input('Digite um CPF sem pontos ou traços')
novo_cpf=cpf[:-2]

soma=0
reverso=10
for index in range(19):
    if index>8:
        index-=9

    soma+=int(novo_cpf[index])*reverso
    reverso-=1

    if reverso<2:
        reverso=11
        d=11-(soma%11)
        if d>9:
            d=0
        soma=0
        novo_cpf+=str(d)
    
if cpf==novo_cpf:
    print('Válido')
else:
    print('Inválido')