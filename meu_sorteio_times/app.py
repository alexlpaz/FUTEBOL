import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from meu_sorteio_times.core import formar_times # type: ignore

# -------------- Estilo do App --------------
st.set_page_config(page_title="Sorteio de Times - Pelada Monstra", page_icon="⚽", layout="centered")
st.markdown("<h1 style='text-align: center;'>⚽ Sorteio de Times - Pelada Monstra</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Distribuição de jogadores de forma equilibrada com goleiros fixos.</p>", unsafe_allow_html=True)
st.markdown("---")

# ----------- Entrada de Dados -------------
with st.expander("📋 Instruções", expanded=True):
    st.markdown("""
    - Digite um jogador por linha no formato: 'Nome,Estrelas'.
    - Acrescente '_Gol' ao nome dos goleiros.  
    - Exemplo:
      '''
      João_Gol,3
      José,5
      Pedro,3
      Andre,4
      '''
    """)

texto = st.text_area("Jogadores (Nome,Estrelas):", height=250)

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

if len(jogadores) < 12:
    st.warning("Digite pelo menos 12 jogadores para formar times.")
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
                        rank_display = "⭐" * rank
                    data.append({"Jogador": nome, "Ranking": rank_display})
                df = pd.DataFrame(data)
                st.dataframe(df, use_container_width=True, hide_index=True)
                st.markdown("""
                    <style>
                    /* Fonte menor para as tabelas */
                    .stTable table {
                        font-size: 12px !important;
                        border-spacing: 0 6px !important;
                    }

                    /* Fonte menor para o corpo do texto e lista */
                    .css-1d391kg p, .css-1d391kg li {
                        font-size: 12px !important;
                        line-height: 1.2 !important;
                    }

                    /* Títulos menores e compactos */
                    h1 {
                        font-size: 24px !important;
                        margin-bottom: 0.3rem !important;
                    }
                    h2 {
                        font-size: 20px !important;
                        margin-top: 0.6rem !important;
                        margin-bottom: 0.3rem !important;
                    }
                    h3 {
                        font-size: 16px !important;
                        margin-top: 0.4rem !important;
                        margin-bottom: 0.2rem !important;
                    }

                    /* Espaçamento interno das células da tabela */
                    .stTable table th, .stTable table td {
                        min-width: 80px !important;   /* ajusta para a largura desejada */
                        max-width: 120px !important;
                        white-space: nowrap;           /* evita quebra de linha dentro da célula */
                        overflow: hidden;
                        text-overflow: ellipsis;       /* mostra "..." se o texto for maior */
                        padding: 6px 8px !important;
                    }

                    /* Remover margens extras */
                    .block-container {
                        padding-top: 1rem !important;
                        padding-bottom: 1rem !important;
                    }
                    </style>
                """, unsafe_allow_html=True)
