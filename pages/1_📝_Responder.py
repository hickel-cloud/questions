import streamlit as st
from src.utils import get_materias, get_assuntos, get_questoes_filtradas, registrar_resposta


st.header("📝 Responder Questões")

if "logado" not in st.session_state or not st.session_state["logado"]:
    st.warning("Você precisa estar logado para acessar esta página. Acesse a página app no menu lateral e realize o login.")
    st.stop()

st.sidebar.title(f"Bem-vindo, {st.session_state['usuario']}")
if st.sidebar.button("Sair"):
    st.session_state.clear()
    st.rerun()

materias = get_materias()
materia = st.selectbox("Matéria", materias)

if materia:
    assuntos = get_assuntos(materia)
    assunto = st.selectbox("Assunto", assuntos)

    if assunto:
        questoes = get_questoes_filtradas(materia, assunto)

        for q in questoes:
            with st.expander(f"Questão {q['ordem']}"):
                st.write(q["assertiva"])    
                resposta = st.radio("Sua resposta:", ["✅ Certo", "❌ Errado"], horizontal=True, index=None, key=f"resposta_{q['id']}")
                if st.button("Confirmar", key=f"confirmar_{q['id']}", type='primary'):
                    correto = resposta == q["gabarito"]
                    if correto:
                        st.success("✅ Muito bom, você é o(a) melhor!")
                        st.info(f"Justificativa: {q['justificativa']}")
                    else:
                        st.error(" ❌ Que pena, resposta errada.")
                    registrar_resposta(q["id"], correto)
