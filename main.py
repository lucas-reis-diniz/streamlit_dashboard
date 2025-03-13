import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

st.set_page_config(page_title="Dashboard e Portifolio Profissional", layout="wide")

st.sidebar.markdown(
    """
    <style>
    .circle-img {
        width: 100px; 
        height: 100px;
        border-radius: 50%;  
        object-fit: cover;  
    }
    </style>
    """, unsafe_allow_html=True)


st.sidebar.title("💼 Portifolio")
pagina = st.sidebar.radio("Escolha uma página:", ["📌 Sobre Mim", "🎓 Formação e Experiência", "🛠️ Skills", "📊 Análise de Dados"])

if pagina == "📌 Sobre Mim":
    st.image("Profile.png", caption="Minha Foto :)", width=300)
    st.title("Bem-vindo ao meu Dashboard Profissional")
    st.write("## Lucas Reis Diniz")
    st.write("💡 Engenheiro de Software em formação na FIAP, com sólida experiência em C++ (5 anos) e forte interesse em Inteligência Artificial, Big Data e Computação Quântica.")
    st.write("🧠 Apaixonado por resolver problemas complexos, explorar novas tecnologias e desenvolver soluções inovadoras.")
    st.write("### 🎯 Objetivo:")
    st.write("Meu objetivo é ingressar em um time de pesquisa e desenvolvimento ou engenharia de dados, onde possa trabalhar na construção de modelos preditivos, análise de grandes volumes de dados e desenvolvimento de microserviços escaláveis. Busco um ambiente desafiador que me permita crescer profissionalmente e inovar, seja otimizando sistemas de recomendação, criando soluções inteligentes para análise de sentimentos ou contribuindo para novas abordagens em computação de alto desempenho.")
    st.write("### 🚀 Principais Experiências e Projetos:")
    st.write("- Classificação de Síndromes Genéticas: Aplicação de machine learning, embeddings e visualização com t-SNE para diagnóstico médico.")
    st.write("- Geração de Resumo Automático com IA: Processamento de Big Data e NLP no Amazon Product Reviews, utilizando Docker e modelos de IA.")
    st.write("- Projetos de IoT: Experiência prática em robótica e hardware embarcado.")

elif pagina == "🎓 Formação e Experiência":
    st.title("🎓 Formação e Experiência")
    st.write("### Formação Acadêmica")
    st.write("- Analise e Desenvolvimento de Sistemas - SENAI ( Fev/2021 - Ago/2022 )")
    st.write("- Engenharia de Software - FIAP ( Ago/2023 - Jun/2027 )")
    st.write("### Experiência Profissional")
    st.write(" - Buscando primeira experiencia")
    st.write(" - Freelances Envolvendo Analise da Dados e ML")

elif pagina == "🛠️ Skills":
    st.title("🛠️ Habilidades & Competências")

# Seção de Hard Skills
    with st.container():
        st.header("📚 Tecnologias & Ferramentas")
        cols = st.columns(3)
        
        tech_skills = {
            "Linguagens": ["Python", "R", "C++", "Q#"],
            "Desenvolvimento": ["Flutter", "Docker", "Big Data"],
            "Análise": ["Data Analytics", "Pandas", "SQL", "Power BI"]
        }
    
        for category, skills in tech_skills.items():
            with cols[0 if category == "Linguagens" else 1 if category == "Desenvolvimento" else 2]:
                st.subheader(f"🔧 {category}")
                for skill in skills:
                    st.markdown(f"- {skill}")
    
    # Seção de Soft Skills
    with st.container():
        st.header("🌟 Competências Interpessoais")
        cols = st.columns(2)
        
        soft_skills = [
            ("💡", "Resolução de Problemas Complexos"),
            ("🤝", "Trabalho em Equipe Multidisciplinar"),
            ("🧠", "Pensamento Analítico e Estratégico"),
            ("🚀", "Aprendizado Ágil e Contínuo"),
            ("🎨", "Criatividade e Inovação"),
            ("⏳", "Gestão de Tempo e Prioridades"),
            ("📢", "Comunicação Técnica Clara"),
            ("🌐", "Adaptação Intercultural")
        ]

    for i, (icon, skill) in enumerate(soft_skills):
        with cols[0] if i % 2 == 0 else cols[1]:
            st.markdown(f"{icon} **{skill}**")

elif pagina == "📊 Análise de Dados":
    st.title("📊 Análise de Dados")
    st.write("Análise de Sentimentos e Avaliações de Consumidores: Visualização de Tendências e Correlação entre Variáveis")
    st.write("## Porque a escolha desse dataset ?")
    st.write("A escolha do dataset Consumer Sentiments and Ratings é altamente viável para o desenvolvimento de um sistema de geração de resumos automáticos de reviews com IA. Esse conjunto de dados contém avaliações detalhadas de consumidores sobre produtos e serviços, incluindo textos de reviews e classificações de sentimento, proporcionando uma base rica para análise e modelagem de linguagem natural (NLP).")


    @st.cache_data
    def load_data():
        df = pd.read_csv("market_comments.csv")
        df['positive'] = df['tonality'].apply(lambda x: 1 if x == 'positive' else 0)
        df['negative'] = df['tonality'].apply(lambda x: 1 if x == 'negative' else 0)
        return df


    df = load_data()

    st.write("### Apresentação dos Dados")
    st.write(df.head())

    st.title("Identificação das variaveis")
    st.write(df.dtypes)

    st.write("### Medidas Centrais e Dispersão")
    st.write(df.describe())

    selected_chart = st.selectbox(
    "Selecione o gráfico que deseja visualizar:",
    options=[
        "Distribuição das Avaliações",
        "Tonalidade dos Comentários",
        "Distribuição Probabilística",
        "Análise de Sentimento"
    ]
)

    if selected_chart == "Distribuição das Avaliações":
        st.write("### Distribuição das Avaliações")
        fig = px.histogram(df, x="rating", nbins=5, marginal="box", title="Distribuição das Avaliações", opacity=0.7)
        st.plotly_chart(fig, use_container_width=True)

    elif selected_chart == "Tonalidade dos Comentários":
        st.write("### Distribuição da Tonalidade dos Comentários")
        tonality_counts = df["tonality"].value_counts().reset_index()
        tonality_counts.columns = ["tonality", "count"]  # Renomeando colunas
        fig = px.bar(tonality_counts, x="tonality", y="count", title="Distribuição da Tonalidade dos Comentários")
        st.plotly_chart(fig, use_container_width=True)
    
    elif selected_chart == "Distribuição Probabilística":
        st.write("### Aplicação de Distribuições Probabilísticas")
    
        # Cálculo da distribuição normal ajustada
        mu, sigma = df["rating"].mean(), df["rating"].std()
        x = np.linspace(df["rating"].min(), df["rating"].max(), 100)
        y = stats.norm.pdf(x, mu, sigma)
    
        # Criando um gráfico interativo
        fig = px.histogram(df, x="rating", nbins=5, opacity=0.6, histnorm="probability density", title="Distribuição Probabilística")
        fig.add_scatter(x=x, y=y, mode="lines", name="Distribuição Normal", line=dict(color="red"))
    
        st.plotly_chart(fig, use_container_width=True)
        
    elif selected_chart == "Análise de Sentimento":
        st.write("### Análise de Sentimento dos Comentários")
        tonality_counts = df["tonality"].value_counts().reset_index()
        tonality_counts.columns = ["tonality", "count"]  # Renomeando colunas
        fig = px.bar(tonality_counts, x="tonality", y="count", title="Análise de Sentimento")
        st.plotly_chart(fig, use_container_width=True)
    
    st.write("## Foram escolhidas as distribuições Normal e Binomial:")
    st.write("- **Distribuição Normal:** Como as avaliações de produtos geralmente seguem um padrão em torno de um valor médio, a Normal é útil para modelar a variação do Score.")
    st.write("- **Distribuição Binomial:** Utilizada para modelar o número de votos úteis de uma avaliação, pois representa um número fixo de tentativas (votos) com duas possíveis saídas (útil ou não útil).")
    
    fig1 = px.histogram(df, x="rating", nbins=20, marginal="box", title="Distribuição Normal das Avaliações", opacity=0.7)
    st.plotly_chart(fig1, use_container_width=True)
    
    fig2 = px.histogram(df, x="HelpfulnessNumerator", nbins=20, marginal="box", title="Distribuição Binomial dos Votos Úteis", opacity=0.7)
    st.plotly_chart(fig2, use_container_width=True)

st.sidebar.write("Desenvolvido por Lucas Reis Diniz")
