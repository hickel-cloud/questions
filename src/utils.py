from src.supabase_client import supabase


def get_materias():
    data = supabase.table("questoes").select("materia").execute().data
    return sorted(list(set([q["materia"] for q in data])))

def get_assuntos(materia):
    data = supabase.table("questoes").select("assunto").eq("materia", materia).execute().data
    return sorted(list(set([q["assunto"] for q in data])))

def get_questoes_filtradas(materia, assunto):
    return supabase.table("questoes").select("*").eq("materia", materia).eq("assunto", assunto).order("ordem").execute().data

def registrar_resposta(q_id, correto):
    campo = "acertos" if correto else "erros"
    questao = supabase.table("questoes").select(campo).eq("id", q_id).single().execute().data
    novo_valor = questao[campo] + 1
    supabase.table("questoes").update({campo: novo_valor}).eq("id", q_id).execute()

def adicionar_questao(materia, assunto, assertiva, gabarito, justificativa):
    dados = supabase.table("questoes").select("ordem").eq("materia", materia).eq("assunto", assunto).order("ordem", desc=True).limit(1).execute().data
    ordem = dados[0]["ordem"] + 1 if dados else 1
    supabase.table("questoes").insert({
        "materia": materia,
        "assunto": assunto,
        "assertiva": assertiva,
        "gabarito": gabarito,
        "justificativa": justificativa,
        "ordem": ordem
    }).execute()