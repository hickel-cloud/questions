import streamlit as st
from time import sleep
from src.utils import adicionar_questao

st.header("➕ Adicionar Nova Questão")

if "logado" not in st.session_state or not st.session_state["logado"]:
    st.warning("Você precisa estar logado para acessar esta página. Acesse a página app no menu lateral e realize o login.")
    st.stop()

st.sidebar.title(f"Bem-vindo, {st.session_state['usuario']}")
if st.sidebar.button("Sair"):
    st.session_state.clear()
    st.rerun()

# States para limpar campos após submissão
if "assertiva" not in st.session_state:
    st.session_state.assertiva = ""
if "justificativa" not in st.session_state:
    st.session_state.justificativa = ""
if "gabarito" not in st.session_state:
        st.session_state.gabarito = None


materias = ['ALP', 'DHU', 'EDA', 'EFV', 'FPD','FTR','PER', 'PLF', 'RLH']
materia = st.selectbox("Matéria", materias)

if materia:
    dict_assuntos = {
        'ALP': ['3. COMPETÊNCIAS LEGAIS DA PRF', 
                '4. ASPECTOS LEGAIS DO USO DA FORÇA', 
                '5. ASPECTOS LEGAIS DA ABORDAGEM POLICIAL', 
                '6. PERSECUÇÃO PENAL NA PRÁTICA PRF', 
                '7. PRISÃO', '8. NARRATIVA POLICIAL', 
                '9. ABUSO DE AUTORIDADE', 
                '10. TORTURA',
                '11. CRIMES EM ESPÉCIE MAIS COMUNS'],
        'DHU': ['4. DIREITOS HUMANOS DOS POLICIAIS',
                '5. ESTRUTURAS DE DIREITOS HUMANOS DA PRF',
                '6. CONHECIMENTO HUMANO E MÉTODO CIENTÍFICO',
                '7. VIESES COGNITIVOS E ERROS DE PERCEPÇÃO',
                '8. VIOLÊNCIA E CRIMINALIDADE',
                '9. RACISMO',
                '10. PESSOAS EMPOBRECIDAS, PESSOAS EM SITUAÇÃO DE RUA, ANDARILHOSTRECHEIROS',
                '11. POVOS INDÍGENAS E QUILOMBOLAS',
                '13. PESSOAS COM DEFICIÊNCIA',
                '20. TRABALHO ESCRAVO CONTEMPORÂNEO'],
        'EDA': ['1. O TRÁFICO DE DROGAS E O CRIME ORGANIZADO NO BRASIL',
                '2. DAS DROGAS',
                '3. DAS REGIÕES PRODUTORAS E DAS ROTAS DO TRÁFICO DE DROGAS, ARMAS E MUNIÇÕES',
                '4 DA ENTREVISTA'],
        'EFV': ['1. HISTÓRICO DA IDENTIFICAÇÃO VEICULAR NO BRASIL', 
                '2. IDENTIFICAÇÃO VEICULAR',
                '3. DOCUMENTOS ELETRÔNICOS', 
                '4. SISTEMAS DE CONSULTAS'],
        'FPD': ['1. CONCEITOS EM CAPACIDADE VEICULAR',
                '2. LIMITES DE PESO',
                '3. LIMITE LEGAL DE PESO',
                '4. LIMITE TÉCNICO DE PESO',
                '5. LIMITE REGULAMENTAR DE PESO',
                '6. DIMENSÕES MÁXIMAS REGULAMENTARES'],
        'FTR': ['1. INTRODUÇÃO', 
                '2. MEDIDAS ADMINISTRATIVAS', 
                '3. HABILITAÇÃO, ESPÉCIES, CATEGORIAS, CURSOS ESPECIALIZADOS E EXAME TOXICOLÓGICO',
                '4. VEÍCULOS: REGISTRO, LICENCIAMENTO E EMPLACAMENTO',
                '5. NORMAS GERAIS DE CIRCULAÇÃO E CONDUTA',
                '6. EQUIPAMENTOS OBRIGATÓRIOS'],
        'PER': ['2. DEFINIÇÕES',
                '3. ESTADO FÍSICO DOS ENVOLVIDOS',
                '4. DINÂMICA DO SINISTRO',
                '5. PRIORIDADES NO ATENDIMENTO DE SINISTROS',
                '6. RECEBIMENTO DA COMUNICAÇÃO DE SINISTRO'],
        'PLF': ['2. DIRECIONAMENTO ESTRATÉGICO OPERACIONAL',
                '3. SERVIÇOS E ATIVIDADES OPERACIONAIS',
                '4. ESTRUTURA E COMPETÊNCIAS OPERACIONAIS',
                '5. EXECUÇÃO OPERACIONAL',
                '6. ROTINAS OPERACIONAIS',
                '10. SISTEMAS, REGISTROS E RELATÓRIOS'],
        'RLH': ['4. INTELIGÊNCIA',
                '5. COMUNICAÇÃO',
                '6. EQUIPE',
                '7. ESTRESSE',
                '8. MUDANÇA',
                '9. ATENDIMENTO AO CIDADÃO']
        }
    assuntos_add = dict_assuntos[materia]
    assunto = st.selectbox("Assunto", assuntos_add)

#     if assunto:
#         st.session_state.assertiva = st.text_area("Assertiva", value=st.session_state.assertiva, key="assertiva_input")
        
#         # Colunas para os checkboxes estilizados
#         col1, col2 = st.columns(2)

#         with col1:
#             if st.button("✅ Certo", key="btn_certo", use_container_width=True):
#                 st.session_state.gabarito = "Certo"

#         with col2:
#             if st.button("❌ Errado", key="btn_errado", use_container_width=True):
#                 st.session_state.gabarito = "Errado"

#         # Mostrar gabarito selecionado com destaque
#         if st.session_state.gabarito:
#             if st.session_state.gabarito == "Certo":
#                 st.success("Gabarito selecionado: ✅ Certo")
#             else:
#                 st.error("Gabarito selecionado: ❌ Errado")

#         st.session_state.justificativa = st.text_area("Justificativa", value=st.session_state.justificativa, key="justificativa_input")

#         if st.button("Salvar Questão", type='primary'):
#             if not st.session_state.gabarito:
#                 st.warning("Selecione um gabarito antes de salvar a questão.")
#             elif not st.session_state.assertiva.strip() or not st.session_state.justificativa.strip():
#                 st.warning("Preencha todos os campos antes de salvar.")
#             else:
#                 adicionar_questao(materia, 
#                                 assunto, 
#                                 st.session_state.assertiva, 
#                                 st.session_state.gabarito, 
#                                 st.session_state.justificativa)
#                 st.success("Questão adicionada com sucesso!")

#                 sleep(1.5)

#                 st.cache_data.clear()

#                 st.session_state.assertiva = ""
#                 st.session_state.justificativa = ""
#                 st.session_state.gabarito = None
                
#                 # Força a interface a atualizar os campos
#                 st.rerun()

            

    if assunto:
        with st.form("form_adicionar_questao", border=False):
            st.session_state.assertiva = st.text_area(
                "Assertiva", 
                value=st.session_state.assertiva, 
                key="assertiva_input"
            )

            col1, col2 = st.columns(2)
            with col1:
                if st.form_submit_button("✅ Certo", use_container_width=True):
                    st.session_state.gabarito = "Certo"
            with col2:
                if st.form_submit_button("❌ Errado", use_container_width=True):
                    st.session_state.gabarito = "Errado"

            # Mostra o gabarito escolhido
            if st.session_state.gabarito:
                if st.session_state.gabarito == "Certo":
                    st.success("Gabarito selecionado: ✅ Certo")
                else:
                    st.error("Gabarito selecionado: ❌ Errado")

            st.session_state.justificativa = st.text_area(
                "Justificativa", 
                value=st.session_state.justificativa, 
                key="justificativa_input"
            )

            submit = st.form_submit_button("💾 Salvar Questão", use_container_width=True)

            if submit:
                if not st.session_state.gabarito:
                    st.warning("Selecione um gabarito antes de salvar a questão.")
                elif not st.session_state.assertiva.strip() or not st.session_state.justificativa.strip():
                    st.warning("Preencha todos os campos antes de salvar.")
                else:
                    adicionar_questao(
                        materia, 
                        assunto, 
                        st.session_state.assertiva, 
                        st.session_state.gabarito, 
                        st.session_state.justificativa
                    )
                    st.success("Questão adicionada com sucesso!")
                    sleep(1.5)
                    st.cache_data.clear()

                    st.session_state.assertiva = ""
                    st.session_state.justificativa = ""
                    st.session_state.gabarito = None
                    st.rerun()
