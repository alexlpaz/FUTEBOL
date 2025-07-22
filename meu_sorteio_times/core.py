import random
def snake_draft(jogadores, num_times):
    times = [[] for _ in range(num_times)]
    reverse = False
    idx = 0
    while idx < len(jogadores):
        ordem = list(range(num_times))
        if reverse:
            ordem = ordem[::-1]
        for i in ordem:
            if idx >= len(jogadores):
                break
            times[i].append(jogadores[idx])
            idx += 1
        reverse = not reverse
    return times

def formar_times(jogadores, num_por_time=6):
    goleiros = sorted([j for j in jogadores if "_Gol" in j[0]], key=lambda x: x[1], reverse=True)
    jogadores_linha = sorted([j for j in jogadores if "_Gol" not in j[0]], key=lambda x: x[1], reverse=True)

    if not goleiros:
        raise ValueError("É necessário pelo menos um goleiro (com '_Gol' no nome).")

    total_jogadores = len(jogadores)
    num_times_completos = total_jogadores // num_por_time
    total_usados = num_times_completos * num_por_time

    num_jogadores_linha_necessarios = total_usados - num_times_completos
    escalados = jogadores_linha[:num_jogadores_linha_necessarios]

    # Distribuir jogadores em ordem forte-fraco alternado individualmente
    times = [[] for _ in range(num_times_completos)]
    esquerda = 0
    direita = len(escalados) - 1
    idx_time = 0

    while esquerda <= direita:
        if esquerda == direita:
            times[idx_time].append(escalados[esquerda])
            esquerda += 1
        else:
            times[idx_time].append(escalados[esquerda])
            times[idx_time].append(escalados[direita])
            esquerda += 1
            direita -= 1
        idx_time = (idx_time + 1) % num_times_completos

    # Adiciona 1 goleiro por time
    for i in range(num_times_completos):
        goleiro = goleiros[i % len(goleiros)]
        times[i].insert(0, goleiro)

    # Se algum time ficou com menos que 6 jogadores, preenche com extras para garantir 6
    # (Se escalados não fossem suficientes, vamos usar os extras para completar)
    extras = jogadores_linha[num_jogadores_linha_necessarios:]
    idx_extra = 0
    for time in times:
        while len(time) < num_por_time and idx_extra < len(extras):
            time.append(extras[idx_extra])
            idx_extra += 1

    # Jogadores restantes (depois de preencher os completos)
    extras_restantes = extras[idx_extra:]
    if extras_restantes:
        goleiro_extra = goleiros[len(times) % len(goleiros)]
        time_extra = [goleiro_extra] + extras_restantes
        random.shuffle(time_extra[1:])
        times.append(time_extra)

    # Embaralha jogadores dentro dos times mantendo goleiro na frente
    for time in times:
        goleiro = time[0]
        jogadores_restantes = time[1:]
        random.shuffle(jogadores_restantes)
        time[1:] = jogadores_restantes

    return times