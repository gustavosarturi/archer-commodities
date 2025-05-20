import streamlit as st
import plotly.graph_objects as go
from logic.market import load_prices

# Título
st.set_page_config(layout="wide")
st.title("Simulador de Mercado de Commodities")

# Carregando dados
df = load_prices()
total_days = len(df)

# Estado: dia atual
if "current_day" not in st.session_state:
    st.session_state.current_day = 1

# Manchetes pré-definidas
headlines = {
    10: "Mercado reage a anúncio de crise global.",
    25: "Novas regulamentações afetam o setor.",
    50: "Alta inesperada na demanda de commodities.",
    75: "Risco geopolítico aumenta incertezas.",
}

# Exibir manchete como balão (expander) sempre aberto no dia certo
if st.session_state.current_day in headlines:
    with st.expander(f"💬 Manchete do dia: {headlines[st.session_state.current_day]}"):
        st.write("Leia essa notícia importante antes de continuar!")

# Botões para controlar o dia
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("◀️ Voltar um dia"):
        if st.session_state.current_day > 1:
            st.session_state.current_day -= 1
with col2:
    if st.button("Avançar um dia ▶️"):
        if st.session_state.current_day < total_days:
            st.session_state.current_day += 1

# Subconjunto de dados até o dia atual
df_display = df.iloc[:st.session_state.current_day]

# Gráfico candlestick
fig = go.Figure(data=[go.Candlestick(
    x=df_display['date'],
    open=df_display['open'],
    high=df_display['high'],
    low=df_display['low'],
    close=df_display['close']
)])
fig.update_layout(title="Evolução dos Preços", xaxis_title="Data", yaxis_title="Preço")
st.plotly_chart(fig, use_container_width=True)

# Último preço
latest = df_display.iloc[-1]
st.metric(label="Preço de Fechamento", value=f"{latest['close']:.2f}")
