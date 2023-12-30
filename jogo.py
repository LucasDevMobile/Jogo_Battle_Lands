from random import randint
print('')
print('-=-'*10)
print(' Bem Vindo ao Battle Lands!!!')
print('-=-'*10)
print('')
jogador1=str(input('Jogador 1 Escolha o nome do seu personagem:'))
print('')
print('O nome do seu personagem sera {}'.format(jogador1))
print('')
print('''As classes disponiveis sao:
[1] guerreiro
[2] mago
[3] paladino''')
print('')
jogador1classe=str(input('Digite o nome da sua classe:'))
print('')
print('A classe do seu personagem sera {}'.format(jogador1classe))
print('')
jogador2=str(input('Jogador 2 Escolha o nome do seu personagem:'))
print('')
print('O nome do seu personagem sera {}'.format(jogador2))
print('')
print('''As classes disponiveis sao:
[1] guerreiro
[2] mago
[3] paladino''')
print('')
jogador2classe=str(input('Digite o nome da sua classe:'))
print('')
print('A classe do seu personagem sera {}'.format(jogador2classe))
print('')
print('=====A BATALHA VAI COMECAR=====')



dados1=int(input('jogador 1 Digite 1 para rolar o dado:'))

if dados1==1 :
   dados2=randint(1,2)
if dados2==1 or dados2==2:

    mago = {'atk': 100, 'def': 40, 'hp': 100}
    guerreiro = {'atk': 80, 'def': 60, 'hp': 150}
    paladino = {'atk': 50, 'def': 80, 'hp': 200}

    if jogador1classe == 'mago':
            jogador1 = mago
    elif jogador1classe == 'guerreiro':
            jogador1 = guerreiro
    elif jogador1classe == 'paladino':
            jogador1 = paladino
    else:
        print("Classe inválida para o Jogador 1.")
    if jogador2classe == 'mago':
            jogador2 = mago
    elif jogador2classe == 'guerreiro':
            jogador2 = guerreiro
    elif jogador2classe == 'paladino':
            jogador2 = paladino
    else:
        print("Classe inválida para o Jogador 2.")

    resultado = jogador1['atk'] - jogador2['def']
    print(resultado)
    
else:print('Voce perdeu a vez, jogador 2 se prepare! ')


#======================================================================================


dados2=int(input('jogador 2 Digite 1 para rolar o dado:'))

if dados1==1 :
   dados2=randint(1,2)
if dados2==1 or dados2==2:

    mago = {'atk': 100, 'def': 40, 'hp': 100}
    guerreiro = {'atk': 80, 'def': 60, 'hp': 150}
    paladino = {'atk': 50, 'def': 80, 'hp': 200}
        
    resultado = jogador2['atk'] - jogador1['def']
    print(resultado)
        
else:print('Voce perdeu a vez, jogador 1 se prepare! ')
      
    



