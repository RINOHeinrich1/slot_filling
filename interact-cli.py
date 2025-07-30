import joblib
import readline
import os
import sys

HISTORY_FILE = ".slot_history"

# Chargement de l'historique si présent
if os.path.exists(HISTORY_FILE):
    readline.read_history_file(HISTORY_FILE)

def word2features(sent, i):
    word = sent[i]
    features = {
        "word.lower()": word.lower(),
        "word.isupper()": word.isupper(),
        "word.istitle()": word.istitle(),
        "word.isdigit()": word.isdigit(),
    }
    if i > 0:
        word1 = sent[i - 1]
        features.update({
            "-1:word.lower()": word1.lower(),
            "-1:word.istitle()": word1.istitle(),
        })
    else:
        features["BOS"] = True

    if i < len(sent) - 1:
        word1 = sent[i + 1]
        features.update({
            "+1:word.lower()": word1.lower(),
            "+1:word.istitle()": word1.istitle(),
        })
    else:
        features["EOS"] = True

    return features

def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def main():
    print("=== Slot Filling Shell (type 'exit' pour quitter) ===")

    try:
        model = joblib.load("crf_model.joblib")
    except Exception as e:
        print(f"[!] Erreur lors du chargement du modèle : {e}")
        sys.exit(1)

    try:
        while True:
            try:
                sentence = input("> ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\n[✓] Fin du programme.")
                break

            if sentence.lower() in {"exit", "quit"}:
                break

            if not sentence:
                continue

            try:
                tokens = sentence.split()
                X_test = [sent2features(tokens)]
                y_pred = model.predict(X_test)[0]

                print("Résultat :")
                for token, label in zip(tokens, y_pred):
                    print(f"{token:<15} -> {label}")
            except Exception as e:
                print(f"[!] Erreur pendant la prédiction : {e}")

    finally:
        try:
            readline.write_history_file(HISTORY_FILE)
            print("[*] Historique sauvegardé.")
        except Exception:
            pass

if __name__ == "__main__":
    main()
