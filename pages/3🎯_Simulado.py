import streamlit as st
import random
from src.supabase_client import supabase

st.set_page_config(page_title="Simulado", layout="wide")
st.title("Simulado Personalizado")

# Carrega todas as questões do banco
dados = supabase.table("questoes").select("*").execute().data

if not dados:
    st.info("Ainda não há questões cadastradas.")
    st.stop()

# Agrupa por matéria
materias_disponiveis = sorted(set(q["materia"] for q in dados))

# Seletor de matérias (com opção "Todas")
materias_selecionadas = st.multiselect(
    "Escolha as matérias para o simulado:",
    options=["Todas"] + materias_disponiveis,
    default=["Todas"]
)

if "Todas" in materias_selecionadas:
    materias_filtradas = materias_disponiveis
else:
    materias_filtradas = materias_selecionadas

# Número de questões por matéria
quantidade_por_materia = st.number_input(
    "Quantidade de questões por matéria:",
    min_value=1, max_value=50, value=10
)

# Botão para gerar simulado
if st.button("🎬 Gerar Simulado"):
    questoes_por_materia = {}
    for q in dados:
        materia = q["materia"]
        if materia in materias_filtradas:
            questoes_por_materia.setdefault(materia, []).append(q)

    simulado = []
    for materia, questoes in questoes_por_materia.items():
        selecionadas = random.sample(questoes, min(quantidade_por_materia, len(questoes)))
        for q in selecionadas:
            q["materia_grupo"] = materia  # adiciona campo para agrupamento
            simulado.append(q)

    random.shuffle(simulado)

    st.session_state.simulado = simulado
    st.session_state.respostas_simulado = {}

# Exibe simulado, se já tiver sido gerado
if "simulado" in st.session_state:
    simulado = st.session_state.simulado
    st.subheader(f"{len(simulado)} questões selecionadas")

    # Agrupamento por matéria com numeração contínua
    questoes_agrupadas = {}
    for q in simulado:
        materia = q.get("materia_grupo", q["materia"])  # usa materia_grupo se existir, senão materia
        questoes_agrupadas.setdefault(materia, []).append(q)

    contador_global = 1
    for materia, questoes in questoes_agrupadas.items():
        st.subheader(f"📘 {materia}")
        for q in questoes:
            with st.expander(f"{contador_global}. {q['assunto']}"):
                st.write(q["assertiva"])
                resposta = st.radio(
                    "Sua resposta:",
                    ["Certo", "Errado"],
                    key=f"resposta_simulado_{q['id']}"
                )

                if st.button("Confirmar", key=f"confirmar_simulado_{q['id']}"):
                    correto = resposta == q["gabarito"]
                    st.session_state.respostas_simulado[q["id"]] = correto

                    if correto:
                        st.success("✅ Resposta correta!")
                        st.info(f"Justificativa: {q['justificativa']}")
                    else:
                        st.error("❌ Resposta incorreta.")
            contador_global += 1

    respondidas = len(st.session_state.respostas_simulado)
    total = len(simulado)

    if respondidas == total:
        acertos = sum(1 for c in st.session_state.respostas_simulado.values() if c)
        percentual = round((acertos / total) * 100, 2)
        st.markdown("---")
        st.subheader("Resultado do Simulado")
        st.success(f"Acertos: {acertos} / {total}  ({percentual}%)")

        if st.button("Refazer Simulado"):
            del st.session_state.simulado
            del st.session_state.respostas_simulado
            st.rerun()
