#Crie uma lista preenchida com os 5 primeiros colocados de um
#Campeonato de Futebol, na ordem de colocação. Depois mostre:
#a. Apenas os 3 primeiros colocados;
#b. Os últimos 2 colocados;
#c. Uma lista com os times em ordem alfabética;
#d. Em que posição da tabela se encontra o Barcelona;

times = ['Flamengo', 'Palmeiras', 'Atlético-MG', 'São Paulo', 'Barcelona']
print(times)
print("Os 3 primeiros colocados:")
for i in range(3):
    print(f"{i + 1}º lugar: {times[i]}")
print("\nOs últimos 2 colocados:")
for i in range(3, 5):
    print(f"{i + 1}º lugar: {times[i]}")
print("\nTimes em ordem alfabética:")
for time in sorted(times):
    print(time)
print("\nPosição do Barcelona:")
print(f"Barcelona está na {times.index('Barcelona') + 1}ª posição.")