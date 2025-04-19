import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()

def load_config():
    config = {}

    config['url_supabase'] = os.getenv("URL_SUPABASE")
    config['key_supabase'] = os.getenv("KEY_SUPABASE")

    return config


config = load_config()