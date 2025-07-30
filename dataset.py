# dataset.py

train_sentences = [
    [("Je", "O"), ("veux", "O"), ("réserver", "O"), ("un", "O"), ("vol", "O"),
     ("de", "O"), ("Paris", "B-from_location"), ("à", "O"), ("Tokyo", "B-to_location"),
     ("demain", "B-date")],

    [("Réserve", "O"), ("moi", "O"), ("un", "O"), ("vol", "O"),
     ("de", "O"), ("Londres", "B-from_location"), ("à", "O"), ("Berlin", "B-to_location"),
     ("lundi", "B-date")],

    [("Je", "O"), ("cherche", "O"), ("un", "O"), ("billet", "O"), ("d'avion", "O"),
     ("de", "O"), ("Marseille", "B-from_location"), ("vers", "O"), ("New", "B-to_location"), ("York", "I-to_location"),
     ("le", "O"), ("25", "B-date"), ("août", "I-date")],

    [("Vol", "O"), ("direct", "O"), ("Nice", "B-from_location"), ("à", "O"),
     ("Rome", "B-to_location"), ("vendredi", "B-date")],

    [("Je", "O"), ("pars", "O"), ("de", "O"), ("Toulouse", "B-from_location"),
     ("pour", "O"), ("Montréal", "B-to_location"), ("ce", "B-date"), ("soir", "I-date")],

    [("Trouve", "O"), ("moi", "O"), ("un", "O"), ("vol", "O"), ("au", "O"),
     ("départ", "O"), ("de", "O"), ("Bruxelles", "B-from_location"), ("vers", "O"),
     ("Amsterdam", "B-to_location"), ("demain", "B-date")],

    [("Vol", "O"), ("pas", "O"), ("cher", "O"), ("de", "O"), ("Lyon", "B-from_location"),
     ("à", "O"), ("Madrid", "B-to_location"), ("le", "O"), ("1er", "B-date"), ("septembre", "I-date")],

    [("Réservation", "O"), ("vol", "O"), ("au", "O"), ("départ", "O"),
     ("de", "O"), ("Genève", "B-from_location"), ("à", "O"), ("Lisbonne", "B-to_location"),
     ("samedi", "B-date")],

    [("Je", "O"), ("veux", "O"), ("voler", "O"), ("de", "O"), ("Nantes", "B-from_location"),
     ("à", "O"), ("Dubaï", "B-to_location"), ("dimanche", "B-date")],

    [("Trouve", "O"), ("un", "O"), ("vol", "O"), ("pour", "O"), ("Bangkok", "B-to_location"),
     ("depuis", "O"), ("Marseille", "B-from_location"), ("le", "O"), ("10", "B-date"), ("octobre", "I-date")],
]
