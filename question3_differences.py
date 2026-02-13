def calculer_differences_approbations(profil):
    """
    profil: liste de n bulletins de votes par oui/non
    chaque bulletin est une liste de m valeurs binaires 0:vote pas et 1: vote pour
    
    RETURN: liste de toutes les valeurs dckcl(p) pour toutes les paires de candidates
    """


    #petite verif 
    if len(profil)==0 :
        raise ValueError("erreur aucune votantes")
    
    if len(profil[0])==0 :
        raise ValueError("erreur aucune candidates")

    
    m = len(profil[0]) #nb de candidates
    
    #liste pour stocker toutes les differences
    differences = []
    
    #parcourir toutes les tuples de candidates "(k,l)", on impose aussi k < l pour eviter les doublons.
    for k in range(m):

        for l in range(k+1, m):
            
            #compter combien de votantes preferent candidate k a candidate l
            #une votante prefere k a l si elle approuve k par 1 et n'approuve pas l par 0

            nb_k_prefere_l = 0
            
            for bulletin in profil:

                if (bulletin[k] == 1) and (bulletin[l] == 0):

                    nb_k_prefere_l += 1
            
            #idem dans l'autre sens
            nb_l_prefere_k = 0
            
            for bulletin in profil:
                if (bulletin[l] == 1) and (bulletin[k] == 0):
                    nb_l_prefere_k += 1
        
            difference = abs(nb_k_prefere_l - nb_l_prefere_k)
            
            differences.append(difference)
    
    return differences


def calculer_differences_ordres_totaux(profil):
    """
    profil: liste de n bulletins de votes par ordres totaux : chaque bulletin est une liste de m rangs
    l'index i du bulletin correspond a la candidate i, la valeur est son rang dans le classement d'appréciation
    
    RETURN: liste de toutes les valeurs dckcl(p) pour toutes les paires de candidates
    """

    #petite verif 
    if len(profil)==0 :
        raise ValueError("erreur aucune votantes")
    
    if len(profil[0])==0 :
        raise ValueError("erreur aucune candidates")

    m = len(profil[0])
    
    differences = []
    
    for k in range(m):
        for l in range(k+1, m):
            
            #ici la logique change pour compter : une votante prefere k a l si le rang de k est plus petit que le rang de l
            nb_k_prefere_l = 0
            
            for ordre in profil:

                if ordre[k] < ordre[l]:

                    nb_k_prefere_l += 1
            
            #symétriquement on fait la même chose (on aurait pu je penses aussi faire un if else et ajouter direct dans nb_l_prefere_k)
            #on aurait gagner un peu de complexité 
            nb_l_prefere_k = 0
            
            for ordre in profil:

                if ordre[l] < ordre[k]:
                    nb_l_prefere_k += 1
            
            difference = abs(nb_k_prefere_l - nb_l_prefere_k)
            
            differences.append(difference)
    
    return differences


"""
#tests pour votes par approbations [GENERER PAR IA]
print("Test 1 - Profil avec 2 bulletins opposes:")
print(calculer_differences_approbations([[1, 0, 1, 0, 1], [0, 1, 0, 1, 0]]))
print(" ")

print("Test 2 - Profil avec 3 bulletins varies:")
print(calculer_differences_approbations([[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 1, 1, 1, 1]]))
print(" ")

print("Test 3 - Profil avec consensus (tous identiques):")
print(calculer_differences_approbations([[1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [1, 1, 1, 0, 0]]))
print(" ")

print("Test 4 - Profil simple avec 3 candidates:")
print(calculer_differences_approbations([[1, 0, 1], [0, 1, 0], [1, 1, 0]]))
print(" ")

print("Test 5 - Profil avec une seule votante:")
print(calculer_differences_approbations([[1, 0, 1, 0]]))
print(" ")

print("Test 6 - Ordres totaux avec 2 bulletins opposes:")
print(calculer_differences_ordres_totaux([[1, 2, 3], [3, 2, 1]]))
print(" ")

print("Test 7 - Ordres totaux avec 3 bulletins:")
print(calculer_differences_ordres_totaux([[1, 2, 3, 4], [2, 1, 4, 3], [4, 3, 2, 1]]))
print(" ")

print("Test 8 - Ordres totaux avec consensus (tous identiques):")
print(calculer_differences_ordres_totaux([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
print(" ")

print("Test 9 - Ordres totaux simple avec 3 candidates:")
print(calculer_differences_ordres_totaux([[1, 2, 3], [3, 1, 2]]))
print(" ")


"""
