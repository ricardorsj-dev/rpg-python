from random import randint

#cadastrando jogador e inimigo
jogador = 'Gandalf'
inimigo = 'Gollum'
opcao = 'S'

#loop externo para controlar o reset do jogo
while opcao == 'S':
    vida_jogador = 100
    vida_inimigo = 100

   
    print('RPG PYTHON'.center(30, '='))
    
    print(f'{jogador} VS {inimigo}.'.center(30))

    #loop interno para controlar o combate
    while vida_jogador > 0 and vida_inimigo > 0:

        #verificando ataque do jogador
        ataque_jogador = randint(10, 20)
        #verificando dano e vida atual do inimigo
        dano_inimigo = ataque_jogador
        vida_inimigo = vida_inimigo - dano_inimigo

        #condicional para evitar número negativo no code
        if vida_inimigo < 0:
            vida_inimigo = 0 
        print(f'{jogador} causou {dano_inimigo} de dano.')
        print(f'Status atual: {jogador} = {vida_jogador} | {inimigo} = {vida_inimigo}.')

        #verificando se o jogador morreu
        if vida_inimigo <= 0:
            print(f'{jogador} venceu a batalha!')
            break

        #verificando ataque do inimigo    
        ataque_inimigo = randint(8, 15)
        #verificando dano e vida atual do jogador
        dano_jogador = ataque_inimigo
        vida_jogador = vida_jogador - dano_jogador
        if vida_jogador < 0:
            vida_jogador = 0

        print(f'{inimigo} causou {dano_jogador} de dano. ')
        print(f'Status atual: {jogador} = {vida_jogador} | {inimigo} = {vida_inimigo}.')
        
        #verificando se o jogador morreu
        if vida_jogador <= 0:
            print(f'{jogador} perdeu a batalha!')
            break
    #verificando o status final da partida        
    print(f'--- Status da partida --- ') 
    print(f'Gandalf = {vida_jogador}.') 
    print(f'Gollum: {vida_inimigo}.')
    
    #pergunta se quer jogar novamente ou encerrar o jogo 
    opcao = input ('Quer jogar novamente? [S/N]').upper().strip()
    if opcao == 'N':
        print('-=*30')
        print('\nObrigado por jogar! Volte sempre.')
        print('-=*30')
        break
    



    

    


