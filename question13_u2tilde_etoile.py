import random
from question8_distances import distance_hamming, distance_spearman
from question12_u1_etoile import u1_etoile_approbations, u1_etoile_ordres_totaux
from scipy.optimize import linear_sum_assignment




def u2_tilde_approbations(profil, nb_relances):
    """
    calcule u2_tilde*(p) pour des votes par approbations
    utilise l'algorithme k-means avec k=2 pour trouver deux clusters de consensus
    
    profil: liste de n bulletins de votes par approbations
    chaque bulletin est une liste de m valeurs binaires 0 ou 1
    nb_relances: nombre de fois qu'on relance l'algorithme (pour éviter les optima locaux)
    
    RETURN: valeur optimale = c'est la somme minimale des distances avec 2 clusters
    """

    #petite verif comme d'hab
    if len(profil) == 0:
        raise ValueError("erreur aucune votantes")
    
    if len(profil[0]) == 0:
        raise ValueError("erreur aucune candidates")

    n = len(profil)  #nb de votantes

    m = len(profil[0])  #nb de candidates
    
    meilleur_resultat = float('inf')  #on garde le meilleur résultat sur tous les lancés on init avec infini
    
    #on va relancer plusieurs fois étant donné qu'on initialise avec deux centroides aléatoires on pourrait avec des clusters mal séparés par exemple
    #sert à éviter les optimum locaux

    for relance in range(nb_relances):
        
        #------etape 1: initialiser deux centroïdes aléatoirement------
        
        #un centroide est un bulletin de consensus (liste binaire comme d'habitude), à la base on les crée aléatoirement
        centroide1 = []
        for i in range(m):
            centroide1.append(random.randint(0, 1))
        
        centroide2 = []
        for i in range(m):
            centroide2.append(random.randint(0, 1))
        
        #éviter que les deux centroïdes soient identiques
        if centroide1 == centroide2:
            centroide2 = [1 - x for x in centroide1]  #prendre l'opposé
        
        changement = True
        
        #----------------------étape 2: répéter jusqu'à convergence------
        
        while changement:
            
            changement = False
            
            #étape 3: affecter chaque bulletin au cluster le plus proche------
            

            cluster1 = []

            cluster2 = []
            
            for bulletin in profil:
                
                dist1 = distance_hamming(bulletin, centroide1)

                dist2 = distance_hamming(bulletin, centroide2)
                
                #affecter au cluster le plus proche
                if dist1 <= dist2:
                    cluster1.append(bulletin)
                else:
                    cluster2.append(bulletin)
            
            #-étape 4: recalculer les centroïdes------ ça nous fait penser au Kmeans vu en TP d'analyse de données
            
            #pour chaque cluster, trouver le bulletin de consensus optimal
            #on utilise la même méthode que u*1 mais seulement sur le cluster
            
            #pour cluster1: trouver le bulletin de consensus (valeur majoritaire à chaque position)
            if len(cluster1) > 0:
                
                nouveau_centroide1 = []
                
                for i in range(m):
                    
                    #compter combien de bulletins ont 1 à la position i dans cluster1
                    nb_uns = 0
                    
                    for bulletin in cluster1:
                        
                        if bulletin[i] == 1:
                            nb_uns += 1
                    
                    #prendre la valeur la plus présente comme dans question12 
                    if nb_uns >= len(cluster1) - nb_uns:
                        nouveau_centroide1.append(1)
                    else:
                        nouveau_centroide1.append(0)
                
                #verifier si le centroïde a changé
                if nouveau_centroide1 != centroide1:
                    centroide1 = nouveau_centroide1
                    changement = True
            
            #pour cluster2 on fait la même chose
            if len(cluster2) > 0:
                
                nouveau_centroide2 = []
                
                for i in range(m):
                    
                    nb_uns = 0
                    
                    for bulletin in cluster2:
                        
                        if bulletin[i] == 1:
                            nb_uns += 1
                    
                    if nb_uns >= len(cluster2) - nb_uns:
                        nouveau_centroide2.append(1)

                    else:
                        nouveau_centroide2.append(0)
                
                if nouveau_centroide2 != centroide2:
                    centroide2 = nouveau_centroide2
                    changement = True
        
        #------étape 5: calculer la somme des distances---
        
        #somme des distances de tous les bulletins à leur centroïde respectif
        somme = 0
        
        for bulletin in cluster1:
            somme += distance_hamming(bulletin, centroide1)
        
        for bulletin in cluster2:
            somme += distance_hamming(bulletin, centroide2)
        
        #garder le meilleur résultat
        if somme < meilleur_resultat:
            meilleur_resultat = somme
    
    return meilleur_resultat


def trouver_centroide_optimal_ordres(cluster, m):
    """
    trouve l'ordre total optimal pour un cluster (même méthode que u*1)
    utilise l'algorithme hongrois idem que question 12 pour trouver le couplage parfait de poids minimum
    
    m: nb de candidates
    
    RETURN: ordre total optimal : une liste de rangs de 1 à m
    """
    
    #matrice_cout[i][j] = coût d'assigner le rang i+1 à la candidate j idem que question12
    matrice_cout = []
    
    for rang in range(1, m + 1):
        
        ligne_couts = []
        
        for candidate_j in range(m):
            
            cout = 0
            
            for ordre in cluster:
                
                rang_actuel = ordre[candidate_j]   #idem que question12
                cout += abs(rang - rang_actuel)
            
            ligne_couts.append(cout)
        
        matrice_cout.append(ligne_couts)
    
    #on résoud le couplage parfait de poids minimum
    ligne_indices, col_indices = linear_sum_assignment(matrice_cout)
    

    
    #centroide[i] = rang de la candidate i
    centroide = [0] * m
    
    for i in range(len(ligne_indices)):
        
        rang_idx = ligne_indices[i]

        candidate_idx = col_indices[i]

        centroide[candidate_idx] = rang_idx + 1  #rang de 1 à m
    
    return centroide


def u2_tilde_ordres_totaux(profil, nb_relances):
    """
    calcule u2*_tilde(p) pour des votes par ordres totaux
    utilise l'algorithme k-means avec k=2 pour trouver deux clusters de consensus
    
    profil: liste de n ordres totaux
    chaque ordre est une liste de m rangs (ordre[i] = rang de la candidate i, de 1 à m)
    nb_relances: nombre de fois qu'on relance l'algorithme
    
    RETURN: valeur optimale u*2_tilde(p) = somme minimale des distances avec 2 clusters
    """

    #toute petite verif
    if len(profil) == 0:
        raise ValueError("erreur aucune votantes")
    
    if len(profil[0]) == 0:
        raise ValueError("erreur aucune candidates")

    n = len(profil)  #nb de votantes
    
    m = len(profil[0])  #nb de candidates
    
    meilleur_resultat = float('inf')
    
    #relancer l'algorithme plusieurs fois, meme logique que pour l'approbation
    for relance in range(nb_relances):
        
        #-----étape 1: initialiser deux centroïdes aléatoirement----------------
        
        #un centroïde est un ordre total donc on initialise avec une liste de rangs de 1 à m
        ordre_base = list(range(1, m + 1))
        random.shuffle(ordre_base) #mélange l'ordre 
        centroide1 = ordre_base.copy() #pour pouvoir manipuler sans changer l'ordre de base bon ici c'est pas forcément NECESSAIRE mais par question de sécurité on sait jamais
        
        ordre_base2 = list(range(1, m + 1))
        random.shuffle(ordre_base2)
        centroide2 = ordre_base2.copy()
        
        changement = True
        
        #----étape 2: répéter jusqu'à convergence-------
        
        while changement:
            
            changement = False
            
            #---étape 3: affecter chaque bulletin au cluster le plus proche-----
            
            cluster1 = []
            cluster2 = []
            
            for ordre in profil:
                
                dist1 = distance_spearman(ordre, centroide1)
                dist2 = distance_spearman(ordre, centroide2)
                
                if dist1 <= dist2:
                    cluster1.append(ordre)
                else:
                    cluster2.append(ordre)
            
            #--étape 4: recalculer les centroïdes----
            
            #pour chaque cluster, trouver l'ordre total optimal
            #on utilise la même méthode que sur approbation et que u*1 mais seulement sur le cluster
            
            if len(cluster1) > 0:
                
                nouveau_centroide1 = trouver_centroide_optimal_ordres(cluster1, m)
                
                if nouveau_centroide1 != centroide1:

                    centroide1 = nouveau_centroide1

                    changement = True
            
            if len(cluster2) > 0:
                
                nouveau_centroide2 = trouver_centroide_optimal_ordres(cluster2, m)
                
                if nouveau_centroide2 != centroide2:
                    centroide2 = nouveau_centroide2
                    changement = True
        
        #----------etape 5: calculer la somme des distances---------------------
        
        somme = 0
        
        for ordre in cluster1:
            somme += distance_spearman(ordre, centroide1)
        
        for ordre in cluster2:
            somme += distance_spearman(ordre, centroide2)
        
        #garder le meilleur résultat
        if somme < meilleur_resultat:
            meilleur_resultat = somme
    
    return meilleur_resultat


print("test u2*tilde ------ pour approbations")
profil_test1 = [[1, 0, 1], [1, 1, 0], [0, 1, 1], [0, 0, 0], [1, 1, 1]]
print(u2_tilde_approbations(profil_test1, 5))
print(" ")

print("Test u*2_tilde pour les ordres totaux:")
profil_test2 = [[1, 2, 3], [3, 1, 2], [2, 3, 1], [3, 2, 1], [1, 3, 2]]
print(u2_tilde_ordres_totaux(profil_test2, 10))
