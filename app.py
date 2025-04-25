import streamlit as st
from src.supabase_client import supabase
import bcrypt

st.set_page_config(page_icon="📚", page_title="Sistema de Questões", layout="centered")

# Autenticação simples com usuário e senha
def autenticar_usuario(usuario, senha_digitada):
    response = supabase.table("usuarios").select("senha").eq("usuario", usuario).execute()
    if response.data:
        senha_hash = response.data[0]["senha"]
        if verificar_senha(senha_digitada, senha_hash):
            return True
    return False


def verificar_senha(senha_digitada, senha_hash):
    return bcrypt.checkpw(senha_digitada.encode(), senha_hash.encode())

def login():
    st.title("Login no Sistema de Questões")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar", type='primary'):
        if autenticar_usuario(usuario, senha):
            st.session_state["logado"] = True
            st.session_state["usuario"] = usuario
            st.success("Bem-vindo, " + usuario + "!")
            st.rerun()
        else:
            st.error("Credenciais inválidas. Tente novamente.")

def logout():
    st.session_state.clear()
    st.rerun()

def main():
    if "logado" not in st.session_state:
        st.session_state["logado"] = False

    if not st.session_state["logado"]:
        login()
    else:
        st.sidebar.title(f"Bem-vindo, {st.session_state['usuario']}")
        if st.sidebar.button("Sair"):
            logout()
            
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

if __name__ == "__main__":
    main()    