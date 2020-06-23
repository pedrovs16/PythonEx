partidas = []
jogador = {}
gols = gol = 0
resposta = str
jogadores = {}
contagem = 0
resposta2 = 0
while resposta != 'n' and resposta != 'N':
    jogador['nome'] = input('Digite o nome do jogador: ')
    jogador['partidas'] = int(input('Digite quantas partidas ele jogou: '))
    for p in range(1, 1 + jogador['partidas']):
        gol = (int(input(f'Digite quantos gols ele fez na {p}° partida: ')))
        gols += gol
        partidas.append(gol)
    contagem += 1
    jogador['gol'] = partidas.copy()
    jogador['gols'] = gols
    jogadores[f'jogador{contagem}'] = jogador.copy()
    partidas = []
    gols = 0
    resposta = input('Quer continuar? [S/N]')
print('CODIGO    NOME      PARTIDAS      GOLS')
for c in range(0, contagem):
    print(f'{c}    {jogadores[f"jogador{c + 1}"]["""nome"""]}    {jogadores[f"jogador{c + 1}"]["""partidas"""]}    {jogadores[f"jogador{c + 1}"]["""gols"""]}')
while resposta2 != -1:
    resposta2 = int(input('Mostrar o resultado de qual jogador, se não quiser digite [-1]: '))
    print(f'O nome do jogador é {jogadores[f"jogador{resposta2 + 1}"]["""nome"""]}')
    print(f'O campo gols tem {jogadores[f"jogador{resposta2 + 1}"]["""gol"""]}')
    print(f'O total de gols é {jogadores[f"jogador{resposta2 + 1}"]["""gols"""]}')
    print(f'O jogador {jogadores[f"jogador{resposta2 + 1}"]["""nome"""]} jogou {jogadores[f"jogador{resposta2 + 1}"]["""partidas"""]}')
    for p in range(1,1 + jogadores[f"jogador{resposta2 + 1}"]["""partidas"""]):
        print(f'Na partida {p}, fez {jogadores[f"jogador{resposta2 + 1}"]["""gols"""]} gols')