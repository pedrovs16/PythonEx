partidas = []
jogador = {}
gols = gol = 0
jogador['nome'] = input('Digite o nome do jogador: ')
jogador['partidas'] = int(input('Digite quantas partidas ele jogou: '))
for p in range(1, 1 + jogador['partidas']):
    gol = (int(input(f'Digite quantos gols ele fez na {p}° partida: ')))
    gols += gol
    partidas.append(gol)
jogador['gol'] = partidas
jogador['gols'] = gols
print(f'O nome do jogador é {jogador["nome"]}')
print(f'O campo gols tem {jogador["gol"]}')
print(f'O total de gols é {jogador["gols"]}')
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]}')
for p in range(1,1 + jogador["partidas"]):
    print(f'Na partida {p}, fez {jogador["gol"][p - 1]}')