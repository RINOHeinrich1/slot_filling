import re

# Définition des slots à remplir
slots = {
    "nom": None,
    "date": None,
    "lieu": None,
    "produit": None,
    "intention": None
}

# Fonctions simples pour détecter les entités
def detect_nom(text):
    match = re.search(r"je m'appelle (\w+)", text, re.IGNORECASE)
    return match.group(1) if match else None

def detect_date(text):
    match = re.search(r"(?:le|la)? ?(\d{1,2} [a-zéû]+(?: \d{4})?)", text, re.IGNORECASE)
    return match.group(1) if match else None

def detect_lieu(text):
    match = re.search(r"à ([A-Z][a-z]+)", text)
    return match.group(1) if match else None

def detect_produit(text):
    match = re.search(r"(acheter|réserver|commander) un[e]? (\w+)", text)
    return match.group(2) if match else None

def detect_intention(text):
    if "acheter" in text:
        return "achat"
    elif "réserver" in text:
        return "réservation"
    elif "annuler" in text:
        return "annulation"
    return "inconnue"

# Interaction en boucle
print("Bienvenue dans l'agent intelligent ! Tapez 'exit' pour quitter.")
while True:
    user_input = input("\nVotre requête : ").strip()
    if user_input.lower() in ['exit', 'quit']:
        break

    # Extraction des slots
    slots["nom"] = detect_nom(user_input) or slots["nom"]
    slots["date"] = detect_date(user_input) or slots["date"]
    slots["lieu"] = detect_lieu(user_input) or slots["lieu"]
    slots["produit"] = detect_produit(user_input) or slots["produit"]
    slots["intention"] = detect_intention(user_input) or slots["intention"]

    # Affichage
    print("\n🧠 Slots détectés :")
    for key, value in slots.items():
        print(f" - {key.capitalize()} : {value or 'Non détecté'}")
