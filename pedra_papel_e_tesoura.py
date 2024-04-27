# Jogo de pedra papel e tesoura usuário x máquina
import random

# Escolha do usuário, da máquina e validação das escolhas
escolha_usuario = input('Escolha Pedra, Papel ou Tesoura: ').upper()
escolhas_validas = ['PEDRA', 'PAPEL', 'TESOURA']
escolha_maquina = random.choice(escolhas_validas)

# Validar escolha do usuário
if escolha_usuario not in escolhas_validas:
    print(f'A opção {escolha_usuario} não é válida.')
# Defiinir vencedor
else:
    if escolha_usuario == escolha_maquina:
        print(f'Empate! Você selecionou {escolha_usuario} e a máquina também.')
    elif (escolha_usuario == 'PEDRA' and escolha_maquina == 'TESOURA') or (escolha_usuario == 'PAPEL' and escolha_maquina == 'PEDRA') or (escolha_usuario == 'TESOURA' and escolha_maquina == 'PAPEL'):
        print(f'Parabéns!, você selecionou {escolha_usuario} e eu selecionei {escolha_maquina}')
    else:
        print(f'Ganhei!, você selecionou {escolha_usuario} e eu selecionei {escolha_maquina}')

