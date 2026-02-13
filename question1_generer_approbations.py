import random

def generer_profil(n, m, p):

    """
    n: nb de personnes qui votent / nb de bulletins de votes car une personne qui vote = un bulletin
    m : nb de candidates donc chaque bulletin contient m valeurs
    p : valeur de polarisation entre 0 et 1 (on a rajouté une verif d'erreur au cas ou)

    RETURN : list de liste d'entier binaire 1:vote pour le candidat i | 0: ne vote pas pour candidat i

    """

    #verif d'erreur
    if ( (p < 0) or (p > 1) ) :
        raise ValueError("la polarisation doit etre entre 0 et 1")

    #créer un bulletin de base aléatoire
    bulletin = []
    for i in range(m):
        bulletin.append(random.randint(0, 1))
    

    #print(bulletin)

    #creer bulletin opposé
    bulletin_oppose = []

    for x in bulletin:
        bulletin_oppose.append(1-x)

    #print(bulletin_oppose)
    
    # Calculer combien de bulletins seront identiques et combien seront opposés
    nb_identiques = int( n*(1 - p) )
    nb_opposes = n - nb_identiques #tt les bulletins - ceux identiques
    
    # Construire le profil
    profil = []
    
    #ajouter les bulletins identiques

    for b in range(nb_identiques):

        copie_bulletin = []

        for j in range(m):

            copie_bulletin.append(bulletin[j])

        profil.append(copie_bulletin)
    
    #ajouter les bulletins opposés
    for b in range(nb_opposes):

        copie_bulletin_oppose = []

        for j in range(m):

            copie_bulletin_oppose.append(bulletin_oppose[j])

        profil.append(copie_bulletin_oppose)
    
    #melanger aléatoiement le profil pour éviter ordre évident qui est tous les identiques puis ensuite tous les opposés
    random.shuffle(profil)
    
    return profil


print(generer_profil(2,5,0.7)) #nb de votants, nb de candidats, polarisation
