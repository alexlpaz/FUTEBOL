import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from meu_sorteio_times.core import formar_times

# -------------- Estilo do App --------------
st.set_page_config(page_title="Sorteio de Times", page_icon="⚽", layout="centered")
st.markdown("<h1 style='text-align: center;'>⚽ Sorteio de Times</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Distribua jogadores de forma equilibrada com goleiros fixos.</p>", unsafe_allow_html=True)
st.markdown("---")

# ----------- Entrada de Dados -------------
with st.expander("📋 Instruções", expanded=True):
    st.markdown("""
    - Digite um jogador por linha no formato: `Nome,Ranking`.
    - Acrescente `_Gol` ao nome dos goleiros.  
    - Exemplo:
      ```
      João_Gol,90
      Maria,85
      Pedro,80
      ```
    """)

texto = st.text_area("Jogadores (nome,ranking):", height=250)

# ----------- Processamento -----------------
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
    if st.button("🎲 Sortear Times", use_container_width=True):
        times = formar_times(jogadores, num_por_time=6)

        for i, time in enumerate(times):
            with st.container():
                st.markdown(f"### 🟦 Time {i+1}")
                data = []
                for jogador, rank in time:
                    nome = jogador.replace("_Gol", "").strip()
                    if "_Gol" in jogador:
                        nome = f"🧤 **{nome}** (Goleiro)"
                        rank_display = "⭐"
                    else:
                        rank_display = f"`{rank}`"
                    data.append({"Jogador": nome, "Ranking": rank_display})
                df = pd.DataFrame(data)
                st.dataframe(df, use_container_width=True, hide_index=True)
                st.markdown("---")
