import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from meu_sorteio_times.core import formar_times

st.title("⚽ Sorteio de Times com Goleiros Repetidos")

texto = st.text_area(
    "Digite os jogadores e ranking separados por vírgula (exemplo: João_Gol,90):",
    height=250,
)

jogadores = []
for linha in texto.strip().split("\n"):
    if "," in linha:
        nome, rank = linha.split(",", 1)
        try:
            rank = int(rank.strip())
        except:
            rank = 0
        jogadores.append((nome.strip(), rank))

if len(jogadores) < 6:
    st.warning("Digite pelo menos 6 jogadores para formar times.")
else:
    if st.button("🎲 Sortear Times"):
        times = formar_times(jogadores, num_por_time=6)

        for i, time in enumerate(times):
            st.subheader(f"Time {i+1}")
            data = []
            for jogador, rank in time:
                nome = jogador.replace("_Gol", "").strip()
                if "_Gol" in jogador:
                    nome = f"{nome} (Goleiro)"
                    rank = "*"
                data.append({"Jogador": nome, "Ranking": rank})
            df = pd.DataFrame(data)
            st.table(df)
