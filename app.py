import streamlit as st

st.set_page_config(page_title="Sistema de Questões", layout="centered")
st.title("Sistema de Questões")
st.markdown("Navegue pelas páginas usando o menu à esquerda.")




# import streamlit as st
# from supabase import create_client, Client

# from src.config import config


# st.set_page_config(page_title="Sistema de Questões", layout="centered")
# st.title("Sistema de Questões")
# st.markdown("Navegue pelas páginas usando o menu à esquerda.")

# @st.cache_resource
# def conectar_supabase() -> Client:
#     return create_client(config["url_supabase"], config["key_supabase"])

# supabase = conectar_supabase()

# st.title("Banco de Questões")

# # Botão para forçar atualização dos dados
# if st.button("🔄 Atualizar Lista de Matérias/Assuntos"):
#     st.cache_data.clear()

# @st.cache_data
# def get_materias():
#     result = supabase.table("questoes").select("materia").execute()
#     return sorted(set([m["materia"] for m in result.data]))

# @st.cache_data
# def get_assuntos(materia):
#     result = supabase.table("questoes").select("assunto").eq("materia", materia).execute()
#     return sorted(set([a["assunto"] for a in result.data]))

# # Abas principais
# aba_responder, aba_adicionar, aba_rank = st.tabs([
#     "📝 Responder Questões", 
#     "➕ Adicionar Nova Questão", 
#     "📊 Ranking de Questões"
# ])

# # ======================
# # Aba: Responder Questões
# # ======================
# with aba_responder:
#     st.header("Responder Questões")

#     materias = get_materias()
#     materia = st.selectbox("Selecione a Matéria", materias, key="materia_responder")

#     if materia:
#         assuntos = get_assuntos(materia)
#         assunto = st.selectbox("Selecione o Assunto", assuntos, key="assunto_responder")

#         questoes = supabase.table("questoes")\
#             .select("*")\
#             .eq("materia", materia)\
#             .eq("assunto", assunto)\
#             .order("ordem", desc=False)\
#             .execute()

#         st.subheader(f"Questões de {materia} - {assunto}")

#         for q in questoes.data:
#             with st.expander(f"Q{q['ordem']}: {q['assertiva'][:80]}..."):
#                 resposta = st.radio("Sua resposta:", ["Certo", "Errado"], key=f"resposta_{q['id']}")
#                 if st.button("Responder", key=f"botao_{q['id']}"):
#                     if resposta == q["gabarito"]:
#                         st.success("Acertou!")
#                         supabase.table("questoes").update({"acertos": q["acertos"] + 1}).eq("id", q["id"]).execute()
#                     else:
#                         st.error("Errou.")
#                         supabase.table("questoes").update({"erros": q["erros"] + 1}).eq("id", q["id"]).execute()

#                 total = q["acertos"] + q["erros"]
#                 if total > 0:
#                     perc = round((q["acertos"] / total) * 100, 1)
#                     st.info(f"{perc}% de acertos em {total} respostas.")
                    
#                     if perc >= 80:
#                         st.markdown("**Nível: Fácil**")
#                     elif perc >= 50:
#                         st.markdown("**Nível: Médio**")
#                     else:
#                         st.markdown("**Nível: Difícil**")
#                 else:
#                     st.info("Sem estatísticas ainda.")

# # ============================
# # Aba: Adicionar Nova Questão
# # ============================
# with aba_adicionar:
#     st.header("Adicionar Nova Questão")

#     materias = ['ALP', 'DHU', 'EDA', 'EFV', 'FPD','FTR','PER', 'PLF', 'RLH']
#     materia_add = st.selectbox("Selecione uma matéria", materias, key="materia_add")

#     if materia_add:
#         dict_assuntos = {
#             'ALP': ['3. COMPETÊNCIAS LEGAIS DA PRF', 
#                     '4. ASPECTOS LEGAIS DO USO DA FORÇA', 
#                     '5. ASPECTOS LEGAIS DA ABORDAGEM POLICIAL', 
#                     '6. PERSECUÇÃO PENAL NA PRÁTICA PRF', 
#                     '7. PRISÃO', '8. NARRATIVA POLICIAL', 
#                     '9. ABUSO DE AUTORIDADE', 
#                     '10. TORTURA',
#                     '11. CRIMES EM ESPÉCIE MAIS COMUNS'],
#             'DHU': [],
#             'EDA': [],
#             'EFV': ['1. HISTÓRICO DA IDENTIFICAÇÃO VEICULAR NO BRASIL', 
#                     '2. IDENTIFICAÇÃO VEICULAR',
#                     '3. DOCUMENTOS ELETRÔNICOS', 
#                     '4. SISTEMAS DE CONSULTAS'],
#             'FPD': [],
#             'FTR': ['1. INTRODUÇÃO', 
#                     '2. MEDIDAS ADMINISTRATIVAS', 
#                     '3. HABILITAÇÃO, ESPÉCIES, CATEGORIAS, CURSOS ESPECIALIZADOS E EXAME TOXICOLÓGICO',
#                     '4. VEÍCULOS: REGISTRO, LICENCIAMENTO E EMPLACAMENTO',
#                     '5. NORMAS GERAIS DE CIRCULAÇÃO E CONDUTA',
#                     '6. EQUIPAMENTOS OBRIGATÓRIOS'],
#             'PER': ['2. DEFINIÇÕES',
#                     '3. ESTADO FÍSICO DOS ENVOLVIDOS',
#                     '4. DINÂMICA DO SINISTRO',
#                     '5. PRIORIDADES NO ATENDIMENTO DE SINISTROS',
#                     '6. RECEBIMENTO DA COMUNICAÇÃO DE SINISTRO'],
#             'PLF': ['2. DIRECIONAMENTO ESTRATÉGICO OPERACIONAL',
#                     '3. SERVIÇOS E ATIVIDADES OPERACIONAIS',
#                     '4. ESTRUTURA E COMPETÊNCIAS OPERACIONAIS',
#                     '5. EXECUÇÃO OPERACIONAL',
#                     '6. ROTINAS OPERACIONAIS',
#                     '10. SISTEMAS, REGISTROS E RELATÓRIOS'],
#             'RLH': []
#         }
#         assuntos_add = dict_assuntos[materia_add]
#         assunto_add = st.selectbox("Assunto", assuntos_add, key="assunto_add")

#         nova_assertiva = st.text_area("Assertiva")
#         novo_gabarito = st.radio("Gabarito", ["Certo", "Errado"], horizontal=True)
#         nova_justificativa = st.text_area("Justificativa")

#         if st.button("Adicionar questão"):
#             resposta = supabase.table("questoes")\
#                 .select("id")\
#                 .eq("materia", materia_add)\
#                 .eq("assunto", assunto_add)\
#                 .execute()
            
#             nova_ordem = len(resposta.data) + 1

#             nova = {
#                 "materia": materia_add,
#                 "assunto": assunto_add,
#                 "assertiva": nova_assertiva,
#                 "gabarito": novo_gabarito,
#                 "justificativa": nova_justificativa,
#                 "ordem": nova_ordem,
#                 "acertos": 0,
#                 "erros": 0
#             }

#             supabase.table("questoes").insert(nova).execute()
#             st.success(f"Questão adicionada como número {nova_ordem}!")

#             st.cache_data.clear()

# # ===============================
# # Aba: Ranking de Questões
# # ===============================
# with aba_rank:
#     st.header("📊 Ranking de Questões Mais Erradas")

#     todas_questoes = supabase.table("questoes").select("*").execute()

#     ranking = sorted(
#         todas_questoes.data, 
#         key=lambda q: q["erros"], 
#         reverse=True
#     )[:10]  # Top 10

#     for i, q in enumerate(ranking, start=1):
#         total = q["acertos"] + q["erros"]
#         perc = round((q["acertos"] / total) * 100, 1) if total > 0 else 0
#         st.markdown(f"**{i}. {q['materia']} - {q['assunto']} (Q{q['ordem']})**")
#         st.write(f"• {q['assertiva'][:100]}...")
#         st.write(f"• **Acertos:** {q['acertos']} | **Erros:** {q['erros']} | **Acerto %:** {perc}%")
#         st.divider()