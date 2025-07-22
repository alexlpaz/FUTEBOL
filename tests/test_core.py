import pytest
from meu_sorteio_times.core import snake_draft, formar_times

def test_snake_draft():
    jogadores = [("A", 10), ("B", 9), ("C", 8), ("D", 7)]
    times = snake_draft(jogadores, 2)
    assert len(times) == 2
    assert times[0] == [("A", 10), ("D", 7)]
    assert times[1] == [("B", 9), ("C", 8)]

def test_formar_times():
    jogadores = [("J1_Gol", 90), ("J2", 80), ("J3", 70), ("J4", 60), ("J5", 50), ("J6", 40)]
    times = formar_times(jogadores, num_por_time=3)
    assert len(times) == 2
    assert all(len(time) == 3 for time in times)
    assert any("_Gol" in jogador[0] for jogador in times[0])
