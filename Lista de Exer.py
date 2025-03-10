##################################### ALGORITMOS ###########################################

# --------------------------Exercício 1

#< 1° inputar nome, 2° armazenar em nom
#< 3° perguntar salário, 4° converter para float 5° armazenar em sal
#< 6° mostrar nome e salário, 7° puxar a varaivel nom, 8° puxar a variavel sal


# --------------------------Exercício 2

#< 1° (função para calcular a média) com parameros n1 e n2
#< 2° (calculo da média) dentro da função
#< 3° perguntar a primeira nota
#< 4° perguntar a segunda nota
#< 5° mostrar a média com a função media


# --------------------------Exercício 3

#< 1° perguntar a altura da parede
#<- 2° perguntar a largura da parede
#< 3° calcular a área da parede
#< 4° calcular a quantidade de tinta necessária
#<- 5° mostrar a área e a quantidade de tinta necessária


# --------------------------Exercício 4
#<1° função locacao com parametros km e temp
#< 2° calculo do valor da locação
#< 3° perguntar quantos km foram rodados
#< 4° perguntar quantos dias o carro foi alugado 
#< 5° mostrar o valor da locação com a função locacao


# --------------------------Desafio

#< 1° perguntar quantos cigarros fuma por dia, 2° converter para int, 3° armazenar em cigas_dia
#< 4° perguntar há quantos anos fuma, 5° converter para int, 6° armazenar em anos_fu
#< 7° calcular o tempo perdido, 8° armazenar na variavel tempo_perdido
#< 9° mostrar o tempo perdido, 10° puxar a variavel tempo_perdido



#%%
#################### EXERCÍCIOS ####################
nom = input('Qual é o seu nome? ') #<------------ 1° inputar nome, 2° armazenar em nom
sal = float(input('Qual é o seu salário? ')) #<------------ 3° perguntar salário, 4° converter para float 5° armazenar em sal
print(f'O funcionário {nom} tem um salário de R${sal:.2f}.') #<------------ 6° mostrar nome e salário, 7° puxar a varaivel nom, 8° puxar a variavel sal


#%%
def media(n1, n2): #<------------ 1° (função para calcular a média) com parameros n1 e n2
    return (n1 + n2)/2 #<------------ 2° (calculo da média) dentro da função

n1 = float(input('Digite a primeira nota: ')) #<------------ 3° perguntar a primeira nota
n2 = float(input('Digite a segunda nota: ')) #<------------ 4° perguntar a segunda nota
print(f'Sua media é {media(n1, n2)}') #<------------ 5° mostrar a média com a função media


#%%
altura = float(input('Digite a altura da parrde: ')) #<------------ 1° perguntar a altura da parede
largura = float(input('Digite a largura da larede: ')) #<------------ 2° perguntar a largura da parede
area = altura * largura #<------------ 3° calcular a área da parede
tinta = area/2 #<------------ 4° calcular a quantidade de tinta necessária
print(f'Para pintar a parede de {area}m², você precisa de {tinta}L de tinta.') #<------------ 5° mostrar a área e a quantidade de tinta necessária

#%%
def locacao(km, temp): #<------------ 1° função locacao com parametros km e temp
    return (temp * 90 + km * 0.20) #<------------ 2° calculo do valor da locação

km = float(input('Quantos km foram rodados? ')) #<------------ 3° perguntar quantos km foram rodados
temp = float(input('Quantos dias o carro foi alugado? ')) #<------------ 4° perguntar quantos dias o carro foi alugado 
print(f'O valor a ser pago é de R${locacao(km, temp):.2f}') #<------------ 5° mostrar o valor da locação com a função locacao




# ------------->1° DESAFIO<----------------
#%%

cigas_dia = int(input('Quantos cigarros você fuma por dia? ')) #<------------ 1° perguntar quantos cigarros fuma por dia, 2° converter para int, 3° armazenar em cigas_dia
anos_fu = int(input('Há quantos anos você fuma? ')) #<------------ 4° perguntar há quantos anos fuma, 5° converter para int, 6° armazenar em anos_fu
tempo_perdido = (cigas_dia * 10) * (anos_fu * 365)/1440    #<------------ 7° calcular o tempo perdido, 8° armazenar na variavel tempo_perdido
print(f'Você perdeu {tempo_perdido:.2f} dias de vida fumando cigarros.') #<------------ 9° mostrar o tempo perdido, 10° puxar a variavel tempo_perdido





