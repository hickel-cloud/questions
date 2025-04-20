import bcrypt
from src.supabase_client import supabase

# Gerar o hash da senha
def hash_senha(senha: str) -> str:
    senha_bytes = senha.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_bytes = bcrypt.hashpw(senha_bytes, salt)
    return hash_bytes.decode('utf-8')  # salvar como string no banco

# Verificar senha com hash salvo
def verificar_senha(senha_digitada: str, hash_salvo: str) -> bool:
    return bcrypt.checkpw(senha_digitada.encode('utf-8'), hash_salvo.encode('utf-8'))

senha = "senha"
hash_armazenado = hash_senha(senha)

# salvar no banco:
supabase.table("usuarios").insert({
    "usuario": "usuario",
    "senha": hash_armazenado
}).execute()
