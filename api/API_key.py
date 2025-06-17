import os
from dotenv import load_dotenv

load_dotenv()

def get_api_key(provider: str) -> str:
    provider = provider.lower()
    if provider == "mistral":
        api_key = os.getenv("MISTRAL_API_KEY")
    elif provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
    elif provider == "huggingface":
        api_key = os.getenv("HUGGINGFACE_API_KEY")
    else:
        raise ValueError(f"Unsupported provider: {provider}")
    
    if not api_key:
        raise ValueError(f"API key for {provider} not found in environment.")
    return api_key

