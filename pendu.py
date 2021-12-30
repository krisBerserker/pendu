"""fichier du pendu, utilisant les fichiers
- donnees.py
-fonctions.py """

from donnees import *
from fonctions import *

#on recupere les scores de la partie
scores = recup_scores ()

#on recupere un nim d utilisateur
utilisateur = recup_nom_utilisateur ()

#Si l'utilisateur n'a pas encore de score, on l'ajoute
if utilisateur not in scores.keys () :
    scores[utilisateur] = 0 #on attribut 0 points pour commencer

continuer_la_partie = 'o'

while continuer_la_partie != 'n' :
    print (" Joueur {0} : {1} point (s) ".format(utilisateur,scores [utilisateur]))
    mot_a_trouver = choisir_mot ()
    lettres_trouvees = []
    mot_trouve = recup_mot_masque (mot_a_trouver, lettres_trouvees)
    nb_chances = nb_coups
    while mot_a_trouver != mot_trouve and nb_chances > 0 :
        print ("Mot a trouver {0} (encore {1} chances ".format (mot_trouve,nb_chances))
        lettre = recup_lettre ()
        if lettre in lettres_trouvees : #la lettre a deja ete trouvees
            print ("vous avez deja trouve cette lettre")
        elif lettre in mot_a_trouver : #la lettre est dans le mot a trouver
            lettres_trouvees.append (lettre)
            print ("bien joue")
            mot_trouve = recup_mot_masque (mot_a_trouver,lettres_trouvees)
        else :
            nb_chances -= 1
            print ("... non, cette lettre ne se trouve pas dans le mot ...")
            mot_trouve = recup_mot_masque (mot_a_trouver,lettres_trouvees)
    #a t on trouve le mot ou le nombre de chance est epuise ?
    if mot_a_trouver == mot_trouve :
        print ("Felicitations ! vous avez trouve le mot {0} . ".format (mot_a_trouver))
    else :
        print ("Perdu ! ! ! vous avez perdu . le mot a trouver etait {0} .".format (mot_a_trouver))
    #on met a jour le score de l utilisateur
    scores [utilisateur] += nb_chances

    continuer_la_partie = input ("Souhaitez-vous continuer la partie (O/N) ?")
    continuer_la_partie = continuer_la_partie.lower()

    enregistrer_scores(scores)

    print ("vous finissez la partie avec {0} points .".format (scores[utilisateur]))
