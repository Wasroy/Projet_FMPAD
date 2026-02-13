def distance_hamming(bulletin1, bulletin2):
    """
    fonction qui calcul la distance de Hamming entre deux bulletins de vote par approbations.
    RETURN : distance de Hamming (nombre de positions où les bulletins diffèrent)
    """
    if len(bulletin1) != len(bulletin2): 
        raise ValueError("Les bulletins doivent avoir la même longueur")
    
    distance_total = 0

    for i in range(len(bulletin1)):

        if bulletin1[i] != bulletin2[i]:

            distance_total += 1
    
    return distance_total

#print(distance_hamming([1, 0, 1, 0, 1], [0, 1, 1, 0, 1]))  #doit donner 2



def distance_spearman(ordre1, ordre2):
    """
    calcul la distance de Spearman entre deux ordres totaux.
    RETURN : distance de Spearman = la somme des différences absolues de rangs

    """
    if len(ordre1) != len(ordre2):

        raise ValueError("les ordres doivent avoir la même longueur")
    
    distance_total = 0

    for i in range(len(ordre1)): #on pourrait choisir aussi ordre2 mais idem car meme longueur

        distance_total += abs(ordre1[i] - ordre2[i])
    
    return distance_total


#print(distance_spearman([1, 2, 3, 4], [4, 3, 2, 1]))  #doit donner 8
