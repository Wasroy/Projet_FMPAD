import matplotlib.pyplot as plt
from question1_generer_approbations import generer_profil
from question2_generer_ordres_totaux import generer_profil_ordres_totaux
from question5_phi2 import phi2_approbations, phi2_ordres_totaux


n = 20 
m = 5  
nb_points = 50  # nombre de valeurs de polarisation à tester

# valeurs de polarisation à tester ramener sur intervalle 0 à 1
polarisations = [i / nb_points for i in range(nb_points + 1)]

#on créer des istes pour stocker les valeurs de φ2
phi2_approb = []
phi2_ordres = []

print("CALCUL EN COURS... ")

for p in polarisations:

    #générer des profils avec la polarisation p
    profil_approb = generer_profil(n, m, p)

    profil_ordres = generer_profil_ordres_totaux(n, m, p)
    

    #on les stocks
    phi2_approb.append(phi2_approbations(profil_approb))

    phi2_ordres.append(phi2_ordres_totaux(profil_ordres))

    #print(phi_2)


#voir doc matplotlib
#[------]
plt.figure(figsize=(10, 6))
plt.plot(polarisations, phi2_approb, 'b-', label='Votes par approbations', linewidth=2)
plt.plot(polarisations, phi2_ordres, 'r-', label='Votes par ordres totaux', linewidth=2)

plt.xlabel('Niveau de polarisation (p)', fontsize=12)
plt.ylabel('φ2(p)', fontsize=12)
plt.title("Evolution de φ2", fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.xlim(0, 1)
plt.ylim(0, 1)

plt.tight_layout()

#BONUS a ajouté dans rendu pdf on sauvegarde le graphique au cas où on veut l'analyser plus tard ou le partager
plt.savefig('visualisation/evolution_phi2.png', dpi=300, bbox_inches='tight')

#[-------Fin du graphe-----]


print("Le graphique a de plus été sauvegardé dans 'visualisations/evolution_question6_phi2.png'")
plt.show()
