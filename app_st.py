
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
#@st.cache
def load_data():
    return pd.read_csv("diagnostico_evasao_retencao.csv")

df = load_data()

# Título
st.title("Análise de Evasão e Retenção")

# Widgets para filtros
campus = st.multiselect("Selecione o Campus", df['Campus'].unique())
situacao = st.multiselect("Selecione a Situação no Curso", df['Situação no Curso'].unique())
modalidade = st.multiselect("Selecione a Modalidade", df['Modalidade'].unique())
curso = st.multiselect("Selecione o Curso", df['Curso'].unique())
ano_semestre = st.multiselect("Selecione o Ano/Semestre letivo da ocorrência", df['Ano/Semestre letivo da ocorrência'].unique())
serie_periodo = st.multiselect("Selecione a Série/Período da ocorrência", df['Série/Período da ocorrência'].unique())

# Seleção de motivos
motivos_cols = {
    "Principal": "Principal motivo da ocorrência",
    "Secundário": "Motivo secundário da ocorrência",
    "Terciário": "Motivo terciário da ocorrência"
}
selected_motivos = st.multiselect("Selecione os motivos", list(motivos_cols.keys()))

# Botão para visualizar
if st.button("Visualizar"):
    # Filtros
    if campus:
        df = df[df['Campus'].isin(campus)]
    if situacao:
        df = df[df['Situação no Curso'].isin(situacao)]
    if modalidade:
        df = df[df['Modalidade'].isin(modalidade)]
    if curso:
        df = df[df['Curso'].isin(curso)]
    if ano_semestre:
        df = df[df['Ano/Semestre letivo da ocorrência'].isin(ano_semestre)]
    if serie_periodo:
        df = df[df['Série/Período da ocorrência'].isin(serie_periodo)]
    
    # Agregando contagem dos motivos selecionados
    agg_data = pd.concat([df[col] for col in [motivos_cols[motivo] for motivo in selected_motivos]]).value_counts()
    
    # Plotando gráfico
    plt.figure(figsize=(10, 6))
    agg_data.plot(kind='bar')
    plt.title('Contagem das Respostas')
    plt.ylabel('Quantidade')
    plt.xlabel('Motivos')
    plt.xticks(rotation=45, ha='right')
    st.pyplot(plt)

if __name__ == '__main__':
    main()
