# cli.py

import sys
import joblib

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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cli.py 'votre phrase à analyser'")
        sys.exit(1)

    sentence = sys.argv[1]
    tokens = sentence.strip().split()

    model = joblib.load("crf_model.joblib")
    X_test = [sent2features(tokens)]
    y_pred = model.predict(X_test)[0]

    print("\nRésultat de slot filling :")
    for token, label in zip(tokens, y_pred):
        print(f"{token:<15} -> {label}")
