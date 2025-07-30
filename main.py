import os
import json
import readline
import requests
from dotenv import load_dotenv
load_dotenv()

AI_TOKEN = os.getenv("AI_API_TOKEN")
AI_PRODUCT_ID = os.getenv("AI_PRODUCT_ID")
print(AI_PRODUCT_ID)
AI_URL = f"https://api.infomaniak.com/1/ai/{AI_PRODUCT_ID}/openai/chat/completions"

def call_llm(model, messages, temperature=0.5, max_tokens=300):
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    headers = {
        "Authorization": f"Bearer {AI_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.post(AI_URL, headers=headers, data=json.dumps(payload))
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()

# Fonction pour générer le prompt et interroger le LLM
def extract_slots_with_llm(user_input):
    system_prompt = {
        "role": "system",
        "content": (
            "Tu es un assistant intelligent chargé d'extraire des informations clés d'une phrase utilisateur. "
            "Retourne uniquement un JSON valide contenant les champs suivants si disponibles : "
            "intention, nom, date, lieu, produit,quantités. "
            "Si un champ est absent, mets sa valeur à null."
        )
    }
    user_prompt = {
        "role": "user",
        "content": f"Phrase utilisateur : {user_input}"
    }

    output = call_llm("mixtral", [system_prompt, user_prompt])
    
    # Tente de parser le JSON retourné
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        print("⚠️ Erreur : le LLM n'a pas retourné un JSON valide. Réponse brute :")
        print(output)
        return {}

# Boucle interactive
if __name__ == "__main__":
    print("=== Slot Filling avec LLM (tape 'exit' pour quitter) ===")
    while True:
        user_input = input("\nVotre requête : ").strip()
        if user_input.lower() in ["exit", "quit"]:
            break
        slots = extract_slots_with_llm(user_input)
        print("\n🎯 Slots détectés :")
        for key in ["intention", "nom", "date", "lieu", "produit","quantités"]:
            print(f" - {key.capitalize()} : {slots.get(key)}")
