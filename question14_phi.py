from question12_u1_etoile import u1_etoile_approbations, u1_etoile_ordres_totaux
from question13_u2tilde_etoile import u2_tilde_approbations, u2_tilde_ordres_totaux


def phidH_approbations(profil, nb_relances):
    """
    
    profil: liste de n bulletins de votes par approbations (binaire)
    nb_relances: nombre de relances pour utilde*2(p) afin d'éviter les optima locaux comme détaillé en question 13
    
    RETURN: valeur de phidH selon la formule de l'énoncé ==>>> plus c'est élevé plus l'éléctorat est polarisé
    """

    #petite verif on commence à les connaitres par coeur la
    if len(profil) == 0:
        raise ValueError("erreur aucune votantes")
    
    if len(profil[0]) == 0:
        raise ValueError("erreur aucune candidates")

    #init de base
    n = len(profil) 
    m = len(profil[0])
    
    
    u1 = u1_etoile_approbations(profil)
    
    u2_tilde = u2_tilde_approbations(profil, nb_relances)
    
    #globalement si la différence entre les deux est élevé, ça veut dire qu'on gagne beaucoup à faire 2 clusters
    #donc l'éléctorat est mieux avec deux clusters donc il est polarisé
    phidH = (2 / (n * m)) * (u1 - u2_tilde)
    
    return phidH


def phidS_ordres_totaux(profil, nb_relances):
    """
    
    profil: liste de n ordres totaux chaque ordre est une liste de m rangs et donc similaire aux questions précédentes ordre[i] = rang de la candidate i
    nb_relances: nombre de relances pour u_tilde*2(p) (pour éviter les optima locaux)
    
    RETURN: valeur de phidS(p) : ==> plus c'est élevé plus l'éléctorat est polarisé
    """

    #le meme code de verif et init !
    if len(profil) == 0:
        raise ValueError("erreur aucune votantes")
    
    if len(profil[0]) == 0:
        raise ValueError("erreur aucune candidates")

    n = len(profil)
    m = len(profil[0])
    

    u1 = u1_etoile_ordres_totaux(profil)

    u2_tilde = u2_tilde_ordres_totaux(profil, nb_relances)

    phidS = (4 / (n * m * m)) * (u1 - u2_tilde) #formule de l'énoncé
    
    return phidS


print("Test phidH pour un vote par approbation:")
profil_test1 = [[1, 0, 1], [1, 1, 0], [0, 1, 1], [0, 0, 0], [1, 1, 1]]
print(phidH_approbations(profil_test1, 7))
print(" ")

print("test pour phidS avec bulletins par ordres totaux:")
profil_test2 = [[1, 2, 3], [3, 1, 2], [2, 3, 1], [3, 2, 1], [1, 3, 2]]
print(phidS_ordres_totaux(profil_test2, 4))
