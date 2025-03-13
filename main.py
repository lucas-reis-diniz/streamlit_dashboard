import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard e Portifolio Profissional", layout="wide")

st.sidebar.title("Portifolio")
pagina = st.sidebar.radio("Escolha uma página:", ["📌 Sobre Mim", "🎓 Formação e Experiência", "🛠️ Skills", "📊 Análise de Dados"])

if pagina == "📌 Sobre Mim":
    st.title("Bem-vindo ao meu Dashboard Profissional")
    st.write("## Lucas Reis Diniz")
    st.write("💡 Engenheiro de Software em formação na FIAP, com sólida experiência em C++ (5 anos) e forte interesse em Inteligência Artificial, Big Data e Computação Quântica.")
    st.write("🧠 Apaixonado por resolver problemas complexos, explorar novas tecnologias e desenvolver soluções inovadoras.")
    st.write("🎯 Objetivo: Construir soluções inovadoras que unem Inteligência Artificial, Computação Quântica e Big Data, combinando tecnologia de ponta com impacto real.")
    st.write("🚀 Principais Experiências e Projetos:")
    st.write("  ✅ Classificação de Síndromes Genéticas: Aplicação de machine learning, embeddings e visualização com t-SNE para diagnóstico médico.")
    st.write("  ✅ Geração de Resumo Automático com IA: Processamento de Big Data e NLP no Amazon Product Reviews, utilizando Docker e modelos de IA.")
    st.write("  ✅ Projetos de IoT: Experiência prática em robótica e hardware embarcado.")

elif pagina == "🎓 Formação e Experiência":
    st.title("🎓 Formação e Experiência")
    st.write("### Formação Acadêmica")
    st.write("- Analise e Desenvolvimento de Sistemas - SENAI ( Fev/2021 - Ago/2022 )")
    st.write("- Engenharia de Software - FIAP ( Ago/2023 - Jun/2027 )")
    st.write("### Experiência Profissional")
    st.write(" - Buscando primeira experiencia")
    st.write(" - Freelances Envolvendo Analise da Dados e ML")

elif pagina == "🛠️ Skills":
    st.title("🛠️ Skills")
    st.write("### Tecnologias e Ferramentas")
    st.write("- Python")
    st.write("- R")
    st.write("- C++")
    st.write("- Flutter")
    st.write("- Docker")
    st.write("- Big Data")
    st.write("- Q#")
    st.write("- Data Analytics")
    st.write("### Soft Skills")
    st.write("- Resolução de problemas")
    st.write("- Trabalho em equipe")
    st.write("- Pensamento analítico")
    st.write("- Aprendizado Rapido")
    st.write("- Criatividade e Inovação")
    st.write("- Gestão de Tempo")
    st.write("- Comunicação Tecnica")


elif pagina == "📊 Análise de Dados":
    st.title("📊 Análise de Dados")
    st.write("Análise de Sentimentos e Avaliações de Consumidores: Visualização de Tendências e Correlação entre Variáveis")


    @st.cache_data
    def load_data():
        df = pd.read_csv("market_comments.csv")
        # Calculando a distribuição de sentimento (Tonality)
        df['positive'] = df['tonality'].apply(lambda x: 1 if x == 'positive' else 0)
        df['negative'] = df['tonality'].apply(lambda x: 1 if x == 'negative' else 0)
        return df


    df = load_data()

    # Exibindo os dados
    st.write("### Apresentação dos Dados")
    st.write(df.head())

    # Medidas Centrais e Dispersão
    st.write("### Medidas Centrais e Dispersão")
    st.write(df.describe())

    # Distribuição das Avaliações
    st.write("### Distribuição das Avaliações")
    fig, ax = plt.subplots(figsize=(2, 1))  # Tamanho menor
    sns.histplot(df["rating"], bins=5, kde=True, ax=ax)
    plt.tight_layout()  # Ajusta o layout
    st.pyplot(fig, use_container_width=True)

    # Distribuição da Tonalidade dos Comentários (Sentimentos)
    st.write("### Distribuição da Tonalidade dos Comentários")
    fig, ax = plt.subplots(figsize=(2, 2))
    sns.countplot(x='tonality', data=df, ax=ax)
    st.pyplot(fig)

    # Aplicação de Distribuições Probabilísticas (Analisando a coluna rating)
    st.write("### Aplicação de Distribuições Probabilísticas")
    fig, ax = plt.subplots(figsize=(2, 2))
    sns.histplot(df["rating"], bins=5, kde=True, ax=ax)
    st.pyplot(fig)

    # Análise de Sentimento (Positivo e Negativo)
    st.write("### Análise de Sentimento dos Comentários")
    fig, ax = plt.subplots(figsize=(2, 2))
    sns.countplot(x='tonality', data=df, ax=ax)
    st.pyplot(fig)
st.sidebar.write("Desenvolvido por Lucas Reis Diniz")
