from question8_distances import distance_hamming, distance_spearman
from scipy.optimize import linear_sum_assignment


def u1_etoile_approbations(profil):

    """
    calcule u*1(p) pour des votes par approbations
    trouve le bulletin de consensus qui minimise la somme des distances de Hamming
    
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
    
    #étape 1: construire le bulletin de consensus
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
    
    #étape 2: calculer la somme des distances de Hamming
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
    utilise le couplage parfait de poids minimum dans un graphe biparti (algorithme hongrois)
    
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
    
    #étape 1: construire la matrice de coûts
    #cost[i][j] = coût d'assigner le rang i+1 à la candidate j
    #coût = somme sur tous les bulletins de |(i+1) - rang_actuel_de_j|
    cost_matrix = []
    
    for rang in range(1, m + 1):  #rang de 1 à m
        
        ligne_couts = []
        
        for candidate_j in range(m):  #candidate j (index 0 à m-1)
            
            #calculer le coût: somme des |rang - rang_actuel| pour tous les bulletins
            cout = 0
            
            for ordre in profil:
                
                rang_actuel = ordre[candidate_j]  
                cout += abs(rang - rang_actuel)
            
            ligne_couts.append(cout)
        
        cost_matrix.append(ligne_couts)
    
    #étape 2: résoudre le couplage parfait de poids minimum
    #algorithme hongrois (celui du sujet on dit hongrois car c'est un mathématicien hongrois qui l'a crée) implémenté dans scipy
    row_indices, col_indices = linear_sum_assignment(cost_matrix)

    #voir https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linear_sum_assignment.html
    
    #ici on choisit
    #row_indices[i] = index du rang assigné
    #col_indices[i] = index de la candidate assignée
    
    #étape 3: calculer la valeur optimale
    #c'est la somme des coûts du couplage optimal

    valeur_optimale = 0
    
    for i in range(len(row_indices)):
        
        rang_idx = row_indices[i]

        candidate_idx = col_indices[i]

        valeur_optimale += cost_matrix[rang_idx][candidate_idx]
    
    return valeur_optimale


#tests
print("Test u*1 - Approbations:")
profil_test1 = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
print(u1_etoile_approbations(profil_test1))
print(" ")

print("Test u*1 - Ordres totaux:")
profil_test2 = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
print(u1_etoile_ordres_totaux(profil_test2))
print(" ")
