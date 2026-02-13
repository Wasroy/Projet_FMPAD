import matplotlib.pyplot as plt
from question1_generer_approbations import generer_profil
from question2_generer_ordres_totaux import generer_profil_ordres_totaux
from question14_phi import phidH_approbations, phidS_ordres_totaux


n = 20 
m = 5  
nb_points = 50  # nombre de valeurs de polarisation à tester on reprends les valeurs de la question 6
nb_relances = 5  # nombre de relances pour utilde_2_etoile(p) (peut être réduit pour accélérer le calcul)


# valeurs de polarisation à tester ramener sur intervalle 0 à 1 comme q6
polarisations = [i / nb_points for i in range(nb_points + 1)]

phidH_approb = []
phidS_ordres = []

print("CALCUL EN COURS... - cela peut prendre du temps car kmeans avec plusieurs relance")

for p in polarisations:

    profil_approb = generer_profil(n, m, p)
    profil_ordres = generer_profil_ordres_totaux(n, m, p)
    
    phidH_approb.append(phidH_approbations(profil_approb, nb_relances))

    phidS_ordres.append(phidS_ordres_totaux(profil_ordres, nb_relances))


    #print(profil_approb)
    #print(profil_ordres)

    #print(phidH_approb)
    #print(phidS_ordres)


#voir doc matplotlib
#[------------------------]
plt.figure(figsize=(10, 6))
plt.plot(polarisations, phidH_approb, 'b-', label='nb votes par approbations (φdH)', linewidth=2)
plt.plot(polarisations, phidS_ordres, 'r-', label='nb votes par ordres totaux (φdS)', linewidth=2)

plt.xlabel('Niveau de polarisation (p)', fontsize=12)
plt.ylabel('φdH(p) / φdS(p)', fontsize=12)
plt.title("Evolution de φdH et φdS", fontsize=14)
plt.legend(fontsize=11)

plt.grid(True, alpha=0.3)
plt.xlim(0, 1)

plt.tight_layout()

#BONUS comme q6 a ajouté dans rendu pdf on sauvegarde le graphique au cas où on veut l'analyser plus tard ou le partager
plt.savefig('visualisations/evolution_phidH_phidS.png', dpi=300, bbox_inches='tight')

#[-------Fin du grapheee-------------]


print("Le graphique a de plus été sauvegardé dans 'visualisations/evolution_question15_phidH_phidS.png'")
plt.show()
