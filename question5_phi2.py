from question3_differences import calculer_differences_approbations, calculer_differences_ordres_totaux


def phi2_approbations(profil):
    """

    profil : ensemble des votes binaires par approbation 

    RETURN : valeur de φ^2(p) entre 0 et 1 plus c'est proche de 1 plus l'éléctorat est polarisé /séparé en idéologies distinctes

    """
    n = len(profil)

    if n == 0:
        raise ValueError("erreur aucune votantes")
    
    m = len(profil[0])

    if m < 2:
        raise ValueError("Il faut au moins 2 candidates")
    
    differences = calculer_differences_approbations(profil)
    

    
    somme = sum(n - d for d in differences)    #Σ (n - d_ck_cl(p))

    nb_paires = m * (m - 1) // 2 #m parmis 2

    
    phi2 = somme / (n * nb_paires)
    
    return phi2


def phi2_ordres_totaux(profil):
    """
    profil : liste de liste des votes par classement style ordre totaux
    RETURN : valeur de φ2(p) entre 0 et 1 plus c'est proche de 1 plus l'éléctorat est polarisé /séparé en idéologies distinctes
    """

    n = len(profil)

    if n == 0:
        raise ValueError("erreur aucune votantes")
    
    m = len(profil[0])

    if m < 2:
        raise ValueError("Il faut au moins 2 candidates")
    
    differences = calculer_differences_ordres_totaux(profil)
    
    somme = sum(n - d for d in differences)
    
    nb_paires = m * (m - 1) // 2

    phi2 = somme / (n * nb_paires)
    
    return phi2


#print(phi2_approbations([[1, 0, 1], [0, 1, 0], [1, 1, 0]]))
