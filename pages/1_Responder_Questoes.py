import streamlit as st
from src.utils import get_materias, get_assuntos, get_questoes_filtradas, registrar_resposta

st.header("Responder Questões")

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
                resposta = st.radio("Sua resposta:", ["Certo", "Errado"], index=None, key=f"resposta_{q['id']}")
                if st.button("Confirmar", key=f"confirmar_{q['id']}"):
                    correto = resposta == q["gabarito"]
                    if correto:
                        st.success("Resposta correta!")
                        st.info(f"Justificativa: {q['justificativa']}")
                    else:
                        st.error("Resposta errada.")
                    registrar_resposta(q["id"], correto)
