from random import choice

jogo_on = True

def deu_empate(): 
    print ('Deu empate')

while jogo_on:
    itens = ['Pedra', 'Papel', 'Tesoura']
    computador = choice(itens)
    print(computador)
    
    jogador = str(input('Jokenpô: Pedra, Papel ou Tesoura: '))
    if jogador not in itens:
        raise Exception ('Jogo incorreto: Pedra, Papel ou Tesoura:' )
    if jogador == computador:
        deu_empate()

    elif jogador == 'Pedra':
        if computador != 'Papel':
            print ('Parabéns, você ganhou!')
        else:
            print("Poxa, o computador ganhou...")
        jogo_on=False
    elif jogador == 'Papel':
        if computador !='Tesoura':
            print ('Parabéns, você ganhou!')
        else:
            print('Poxa, o computador ganhou...')
        jogo_on=False
    elif jogador == 'Tesoura':
        if computador !="Pedra":
                     print ('Parabéns, você ganhou!')
        else:
            print('Poxa, o computador ganhou...')
        
            