from question8_distances import distance_hamming, distance_spearman
from scipy.optimize import linear_sum_assignment


def u1_etoile_approbations(profil):

    """
    calcule u*1(p) pour des votes par approbations
    on trouve le bulletin de consensus qui minimise la somme des distances de Hamming
    
    profil: liste de n bulletins de votes par approbations
    chaque bulletin est une liste de m valeurs binaires 0 ou 1
    
    RETURN: valeur optimale u*1(p) = somme minimale des distances de Hamming
    """

    #petite verif
    if len(profil) == 0:
        raise ValueError("erreur aucune votantes")
    
    if len(profil[0]) == 0:
        raise ValueError("erreur aucune candidates")



    n = len(profil)  #nb de votantes

    m = len(profil[0])  #nb de candidates
    
    #------étape 1: construire le bulletin de consensus -------

    #pour chaque position, on prend la valeur majoritaire (0 ou 1)
    bulletin_consensus = []
    
    for i in range(m):
        
        #compter combien de bulletins ont 1 à la position i
        nb_uns = 0
        
        for bulletin in profil:
            
            if bulletin[i] == 1:
                nb_uns += 1
        
        #compter les zeros
        nb_zeros = n - nb_uns
        
        #ajouter la valeur la plus présente
        if nb_uns >= nb_zeros:
            bulletin_consensus.append(1)

        else:
            bulletin_consensus.append(0)
    
    #------etape 2: calculer la somme des distances de Hamming-----

    #entre le bulletin de consensus et tous les bulletins du profil
    somme_distances = 0
    
    for bulletin in profil:
        
        distance = distance_hamming(bulletin_consensus, bulletin)
        somme_distances += distance

    
    return somme_distances


def u1_etoile_ordres_totaux(profil):

    """

    calcule u*1(p) pour des votes par ordres totaux
    trouve l'ordre total de consensus qui minimise la somme des distances de Spearman
    on utilise le couplage parfait de poids minimum et le module scipy pour faire comme dans un graphe biparti (algorithme hongrois)
    on peut penser aux notions de biparti vu au semestre précédent en [Algorithme dans les graphes]
    
    profil: liste de n ordres totaux
    chaque ordre est une liste de m rangs (ordre[i] = rang de la candidate i, de 1 à m)
    
    RETURN: valeur optimale u*1(p) = somme minimale des distances de Spearman

    """

    #petite verif comme d'habitude :)
    if len(profil) == 0:
        raise ValueError("erreur aucune votantes")
    
    if len(profil[0]) == 0:
        raise ValueError("erreur aucune candidates")



    n = len(profil)  #nb de votantes

    m = len(profil[0])  #nb de candidates
    
    #-----etape 1: construire la matrice de coûts---------------------


    #matrice_cout[i][j] = coût d'assigner le rang i+1 à la candidate j
    #cout = somme sur tous les bulletins de |(i+1) - rang_actuel_de_j|
    matrice_cout = []
    
    for rang in range(1, m + 1):
        
        ligne_couts = []
        
        for candidate_j in range(m):
            
            #calculer le cout: somme des |rang - rang_actuel| pour tous les bulletins
            cout = 0
            
            for ordre in profil:
                
                rang_actuel = ordre[candidate_j]  

                cout += abs(rang - rang_actuel)
            
            ligne_couts.append(cout)
        
        matrice_cout.append(ligne_couts)
    
    #----etape 2: résoudre le couplage parfait de poids minimum---


    #algorithme hongrois (celui du sujet on dit hongrois car c'est un mathématicien hongrois qui l'a crée) implémenté dans scipy
    ligne_indices, col_indices = linear_sum_assignment(matrice_cout)

    #voir https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linear_sum_assignment.html
    
    #ici on choisit
    #ligne_indices[i] = indice du rang assigné
    #col_indices[i] = indice de la candidate assignée
    

    #------étape 3: calculer la valeur optimale---------
    #c'est la somme des coûts du couplage optimal
    #"idx" diminutif de index = indice


    optimale = 0
    
    for i in range(len(ligne_indices)):
        
        rang_idx = ligne_indices[i]

        candidate_idx = col_indices[i]

        optimale += matrice_cout[rang_idx][candidate_idx]
    
    return optimale

"""
profil_test1 = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
print(u1_etoile_approbations(profil_test1))
print(" ")

profil_test2 = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
print(u1_etoile_ordres_totaux(profil_test2))
"""