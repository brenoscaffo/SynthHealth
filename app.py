import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from src.generator import generate_synthetic_population

st.set_page_config(
    page_title="Gerador de dados sintéticos de saúde",
    page_icon="🧬",
    layout="wide",
)

st.title("SynthHealth")
st.caption("Gerador de dados sintéticos de saúde e ferramenta de análise exploratória")

st.sidebar.header("Configurações do gerador de dados sintéticos")

n = st.sidebar.slider(
    "Tamanho da população sintética",
    min_value=100,
    max_value=50000,
    value=10000,
    step=100
)

seed = st.sidebar.number_input(
    "Semente para geração de números aleatórios",
    min_value=0,
    value=42
)

min_age, max_age = st.sidebar.slider(
    "Faixa etária da população sintética",
    min_value=0,
    max_value=120,
    value=(18, 98)
)

if st.sidebar.button("Gerar população sintética"):
    st.session_state["data"] = generate_synthetic_population(
        n=n, 
        seed=int(seed), 
        min_age=min_age, 
        max_age=max_age)

if "data" in st.session_state:
    df = st.session_state["data"]

    st.success(f"População sintética gerada com sucesso! Tamanho: {len(df)} registros.")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total de indivíduos", f"{len(df):,}")
    col2.metric("Idade média", f"{df['age'].mean():.2f}")
    col3.metric("Média do custo anual", f"${df['annual_cost'].mean():,.2f}")
    col4.metric("Proporção de diabéticos", f"{df['diabetes'].mean() * 100:.1f}%")

    st.subheader("Distribuição de idades")
    st.bar_chart(df['age'].value_counts().sort_index())


    st.subheader("Visualização prévia dos dados sintéticos")
    st.dataframe(df.head(50), use_container_width=True)

    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="Baixar dados sintéticos como CSV",
        data=csv,
        file_name='synthetic_dataset.csv',
        mime='text/csv'
    )

else:
    st.info("Clique no botão 'Gerar população sintética' na barra lateral para criar um conjunto de dados sintéticos.")