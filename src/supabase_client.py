from supabase import create_client, Client
import streamlit as st

from src.config import config 


#supabase: Client = create_client(config["url_supabase"], config["key_supabase"])
supabase: Client = create_client(st.secrets["URL_SUPABASE"], st.secrets["KEY_SUPABASE"])

__all__ = ["supabase"]