import streamlit as st
from src.supabase_client import supabase


st.set_page_config(page_icon="📚", page_title="Sistema de Questões", layout="centered")
st.title("📊 Visão Geral do Banco de Questões")
st.markdown("""
Abaixo está a distribuição de questões cadastradas conforme o conteúdo programático da **1ª Avaliação**.

📌 Utilize o menu à esquerda para **responder questões**, **adicionar novas** ou realizar um **simulado personalizado**.
""")

# Consulta todas as questões do banco
dados = supabase.table("questoes").select("materia", "assunto").execute().data

if not dados:
    st.info("Ainda não há questões cadastradas.")
else:
    # Organiza em dicionário: {materia: {assunto: quantidade}}
    resumo = {}
    for item in dados:
        materia = item["materia"]
        assunto = item["assunto"]
        resumo.setdefault(materia, {})
        resumo[materia].setdefault(assunto, 0)
        resumo[materia][assunto] += 1

    st.markdown("### 📚 Distribuição por Matéria e Assunto")
    # Mostra os dados de forma expandida por matéria
    for materia, assuntos in resumo.items():
        with st.expander(f"**{materia}** ({sum(assuntos.values())} questões)"):
            for assunto, quantidade in sorted(assuntos.items()):
                st.markdown(f"{assunto} ({quantidade} questões)")
                