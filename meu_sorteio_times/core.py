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
    goleiros_originais = sorted([j for j in jogadores if "_Gol" in j[0]], key=lambda x: x[1], reverse=True)
    outros = sorted([j for j in jogadores if "_Gol" not in j[0]], key=lambda x: x[1], reverse=True)

    total_jogadores = len(jogadores)
    num_times_completos = total_jogadores // num_por_time
    total_usados = num_times_completos * num_por_time

    jogadores_para_times = outros[:(total_usados - num_times_completos)]
    times = snake_draft(jogadores_para_times, num_times_completos)

    for i in range(num_times_completos):
        goleiro = goleiros_originais[i % len(goleiros_originais)]
        times[i].insert(0, goleiro)

    restantes = outros[(total_usados - num_times_completos):]
    if restantes:
        time_extra = [goleiros_originais[len(times) % len(goleiros_originais)]]
        time_extra.extend(restantes)
        times.append(time_extra)

    return times
