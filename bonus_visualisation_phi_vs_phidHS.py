import matplotlib.pyplot as plt
from question1_generer_approbations import generer_profil
from question2_generer_ordres_totaux import generer_profil_ordres_totaux
from question5_phi2 import phi2_approbations, phi2_ordres_totaux
from question14_phi import phidH_approbations, phidS_ordres_totaux


n = 20 
m = 5  
nb_points = 50 
nb_relances = 5

polarisations = [i / nb_points for i in range(nb_points + 1)]

phi2_approb = []
phi2_ordres = []
phidH_approb = []
phidS_ordres = []

print("calcul en cours d'un super graphe")
for p in polarisations:

    profil_approb = generer_profil(n, m, p)
    profil_ordres = generer_profil_ordres_totaux(n, m, p)
    
    #calculer φ2 question 6
    phi2_approb.append(phi2_approbations(profil_approb))
    phi2_ordres.append(phi2_ordres_totaux(profil_ordres))
    
    #calculer φdH et φdS comme question 15
    phidH_approb.append(phidH_approbations(profil_approb, nb_relances))
    phidS_ordres.append(phidS_ordres_totaux(profil_ordres, nb_relances))


#[---debut du graphe---]
plt.figure(figsize=(12, 7))
plt.plot(polarisations, phi2_approb, 'b-', label='φ2 - Approbations', linewidth=2, linestyle='-')
plt.plot(polarisations, phi2_ordres, 'r-', label='φ2 - Ordres totaux', linewidth=2, linestyle='-')
plt.plot(polarisations, phidH_approb, 'b--', label='φdH - Approbations', linewidth=2, linestyle='--')
plt.plot(polarisations, phidS_ordres, 'r--', label='φdS - Ordres totaux', linewidth=2, linestyle='--')

plt.xlabel('nv de polarisation', fontsize=12)
plt.ylabel('val de polarisation', fontsize=12)
plt.title("Comparaison φ2 vs φdH & φdS", fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.xlim(0, 1)

plt.tight_layout()

#BONUS d'analyste sauvegarde du graphique
plt.savefig('visualisations/comparaison_phi2_vs_phidHS.png', dpi=300, bbox_inches='tight')

#[-------Fin du graphe-----]

plt.show()
