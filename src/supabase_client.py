from supabase import create_client, Client
import streamlit as st

from src.config import config 


#supabase: Client = create_client(config["url_supabase"], config["key_supabase"])
supabase: Client = create_client(st.secrets["url_supabase"], st.secrets["key_supabase"])

__all__ = ["supabase"]