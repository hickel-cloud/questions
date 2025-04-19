import streamlit as st
from time import sleep
from src.utils import get_materias, get_assuntos, adicionar_questao

st.header("Adicionar Nova Questão")

# States para limpar campos após submissão
if "assertiva" not in st.session_state:
    st.session_state.assertiva = ""
if "justificativa" not in st.session_state:
    st.session_state.justificativa = ""


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
        'DHU': [],
        'EDA': [],
        'EFV': ['1. HISTÓRICO DA IDENTIFICAÇÃO VEICULAR NO BRASIL', 
                '2. IDENTIFICAÇÃO VEICULAR',
                '3. DOCUMENTOS ELETRÔNICOS', 
                '4. SISTEMAS DE CONSULTAS'],
        'FPD': [],
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
        'RLH': []
        }
    assuntos_add = dict_assuntos[materia]
    assunto = st.selectbox("Assunto", assuntos_add)

    if assunto:
        st.session_state.assertiva = st.text_area("Assertiva", value=st.session_state.assertiva, key="assertiva_input")
        st.session_state.gabarito = st.radio("Gabarito", ["Certo", "Errado"], index=None, horizontal=True, key="gabarito_input")
        st.session_state.justificativa = st.text_area("Justificativa", value=st.session_state.justificativa, key="justificativa_input")

        if st.button("Salvar Questão"):
            adicionar_questao(materia, 
                              assunto, 
                              st.session_state.assertiva, 
                              st.session_state.gabarito, 
                              st.session_state.justificativa)
            st.success("Questão adicionada com sucesso!")

            sleep(1.5)

            st.cache_data.clear()

            st.session_state.assertiva = ""
            st.session_state.justificativa = ""

            
            # Força a interface a atualizar os campos
            st.rerun()

            
