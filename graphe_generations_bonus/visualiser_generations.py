import sys
import os
import matplotlib.pyplot as plt
import numpy as np

# Ajouter le répertoire parent au path pour importer generations
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from generations import generer_profil, generer_profil_ordres_totaux


def visualiser_profil_binaire(profil, titre="Profil de votes binaires"):
    """
    Visualise un profil de votes binaires (approbation)
    
    Args:
        profil: liste de bulletins binaires
        titre: titre du graphique
    """
    if not profil:
        print("Profil vide, impossible de visualiser")
        return
    
    m = len(profil[0])  # nombre de candidats
    n = len(profil)     # nombre de votants
    
    # Compter les votes pour chaque candidat
    votes_par_candidat = [0] * m
    for bulletin in profil:
        for i in range(m):
            if bulletin[i] == 1:
                votes_par_candidat[i] += 1
    
    # Créer le graphique
    fig, ax = plt.subplots(figsize=(10, 6))
    
    candidats = [f"Candidat {i+1}" for i in range(m)]
    x_pos = np.arange(len(candidats))
    
    bars = ax.bar(x_pos, votes_par_candidat, color='steelblue', alpha=0.7)
    
    # Ajouter les valeurs sur les barres
    for i, v in enumerate(votes_par_candidat):
        ax.text(i, v + 0.5, str(v), ha='center', va='bottom', fontweight='bold')
    
    ax.set_xlabel('Candidats', fontsize=12)
    ax.set_ylabel('Nombre de votes (approbations)', fontsize=12)
    # Titre plus lisible avec explication
    ax.set_title(f'{titre}\nNombre de votants qui approuvent chaque candidat\n({n} votants, {m} candidats)', 
                 fontsize=13, fontweight='bold', pad=15)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(candidats)
    ax.set_ylim(0, max(votes_par_candidat) * 1.2 if votes_par_candidat else 1)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    return fig


def visualiser_profil_ordres_totaux(profil, titre="Profil d'ordres totaux"):
    """
    Visualise un profil d'ordres totaux (classements)
    
    Args:
        profil: liste de bulletins avec ordres totaux
        titre: titre du graphique
    """
    if not profil:
        print("Profil vide, impossible de visualiser")
        return
    
    m = len(profil[0])  # nombre de candidats
    n = len(profil)     # nombre de votants
    
    # Calculer le rang moyen pour chaque candidat
    # Note: dans le profil, l'index i correspond au candidat i, la valeur est son rang
    rangs_moyens = [0.0] * m
    for ordre in profil:
        for i in range(m):
            rangs_moyens[i] += ordre[i]
    
    # Calculer la moyenne
    for i in range(m):
        rangs_moyens[i] /= n
    
    # Créer le graphique
    fig, ax = plt.subplots(figsize=(10, 6))
    
    candidats = [f"Candidat {i+1}" for i in range(m)]
    x_pos = np.arange(len(candidats))
    
    bars = ax.bar(x_pos, rangs_moyens, color='coral', alpha=0.7)
    
    # Ajouter les valeurs sur les barres
    for i, v in enumerate(rangs_moyens):
        ax.text(i, v + 0.05, f'{v:.2f}', ha='center', va='bottom', fontweight='bold')
    
    ax.set_xlabel('Candidats', fontsize=12)
    ax.set_ylabel('Rang moyen (1 = meilleur, ' + str(m) + ' = pire)', fontsize=12)
    # Titre plus lisible avec explication
    ax.set_title(f'{titre}\nPosition moyenne de chaque candidat dans les classements\n({n} votants, {m} candidats)', 
                 fontsize=13, fontweight='bold', pad=15)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(candidats)
    ax.set_ylim(0, m + 1)
    ax.invert_yaxis()  # Inverser pour que le meilleur rang (1) soit en haut
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    return fig


def visualiser_diversite_bulletins(profil, titre="Diversité des bulletins"):
    """
    Visualise la diversité des bulletins pour montrer qu'il n'y a que 2 types de bulletins
    
    Args:
        profil: liste de bulletins
        titre: titre du graphique
    """
    if not profil:
        print("Profil vide, impossible de visualiser")
        return
    
    # Compter les types de bulletins uniques
    bulletins_uniques = {}
    for bulletin in profil:
        # Convertir en tuple pour pouvoir l'utiliser comme clé de dictionnaire
        bulletin_tuple = tuple(bulletin)
        if bulletin_tuple in bulletins_uniques:
            bulletins_uniques[bulletin_tuple] += 1
        else:
            bulletins_uniques[bulletin_tuple] = 1
    
    n = len(profil)
    nb_types = len(bulletins_uniques)
    
    # Créer le graphique
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Graphique 1: Nombre de bulletins par type
    types = [f"Type {i+1}" for i in range(nb_types)]
    frequences = list(bulletins_uniques.values())
    colors = plt.cm.Set3(np.linspace(0, 1, nb_types))
    
    bars1 = ax1.bar(types, frequences, color=colors, alpha=0.7, edgecolor='black')
    ax1.set_xlabel('Type de bulletin', fontsize=12)
    ax1.set_ylabel('Nombre de bulletins', fontsize=12)
    ax1.set_title(f'Distribution des {nb_types} types de bulletins\n({n} bulletins au total)', 
                  fontsize=12, fontweight='bold', pad=10)
    ax1.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Ajouter les valeurs sur les barres
    for i, v in enumerate(frequences):
        ax1.text(i, v + 0.5, str(v), ha='center', va='bottom', fontweight='bold')
    
    # Graphique 2: Afficher les bulletins uniques
    ax2.axis('off')
    ax2.set_title('Contenu des bulletins uniques', fontsize=12, fontweight='bold', pad=10)
    
    y_pos = 0.9
    for idx, (bulletin_tuple, freq) in enumerate(bulletins_uniques.items()):
        bulletin_str = ' '.join([str(x) for x in bulletin_tuple])
        ax2.text(0.1, y_pos, f"Type {idx+1}: [{bulletin_str}]  (×{freq})", 
                fontsize=11, family='monospace',
                bbox=dict(boxstyle='round', facecolor=colors[idx], alpha=0.3))
        y_pos -= 0.15
    
    # Message d'information
    info_text = f"⚠️ ATTENTION: Seulement {nb_types} type(s) de bulletin(s) unique(s) !\n"
    info_text += f"Tous les bulletins sont soit identiques, soit opposés.\n"
    info_text += f"C'est pourquoi les résultats sont très stables."
    
    ax2.text(0.5, 0.05, info_text, ha='center', va='bottom', 
            fontsize=10, style='italic', color='red',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))
    
    fig.suptitle(titre, fontsize=14, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    return fig


def visualiser_comparaison_polarisation(n, m, polarisations=[0.0, 0.3, 0.5, 0.7, 1.0]):
    """
    Compare l'effet de la polarisation sur les votes binaires
    
    Args:
        n: nombre de votants
        m: nombre de candidats
        polarisations: liste des valeurs de polarisation à comparer
    """
    fig, axes = plt.subplots(1, len(polarisations), figsize=(15, 5))
    
    if len(polarisations) == 1:
        axes = [axes]
    
    for idx, p in enumerate(polarisations):
        profil = generer_profil(n, m, p)
        
        # Compter les votes
        votes_par_candidat = [0] * m
        for bulletin in profil:
            for i in range(m):
                if bulletin[i] == 1:
                    votes_par_candidat[i] += 1
        
        ax = axes[idx]
        candidats = [f"C{i+1}" for i in range(m)]
        x_pos = np.arange(len(candidats))
        
        ax.bar(x_pos, votes_par_candidat, color='steelblue', alpha=0.7)
        ax.set_title(f'p = {p}', fontsize=11, fontweight='bold', pad=8)
        ax.set_xticks(x_pos)
        ax.set_xticklabels(candidats, fontsize=9)
        ax.set_ylabel('Votes', fontsize=10)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Titre principal plus lisible et mieux positionné
    fig.suptitle(f'Effet de la polarisation sur les votes par approbation\n'
                 f'p=0: consensus total | p=1: opposition totale ({n} votants, {m} candidats)', 
                 fontsize=13, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Réserver de l'espace pour le titre
    return fig


if __name__ == "__main__":
    # Exemples de visualisation
    
    print("Génération des graphiques...")
    
    # Définir le répertoire de sauvegarde
    save_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 1. Visualisation d'un profil binaire
    print("1. Profil binaire (n=20, m=5, p=0.5)")
    profil_binaire = generer_profil(20, 5, 0.5)
    fig1 = visualiser_profil_binaire(profil_binaire, "Votes par approbation")
    plt.savefig(os.path.join(save_dir, 'profil_binaire.png'), dpi=150, bbox_inches='tight')
    print("   Graphique sauvegardé: profil_binaire.png")
    
    # 2. Visualisation d'un profil d'ordres totaux
    print("2. Profil d'ordres totaux (n=20, m=5, p=0.5)")
    profil_ordres = generer_profil_ordres_totaux(20, 5, 0.5)
    fig2 = visualiser_profil_ordres_totaux(profil_ordres, "Classements par ordre total")
    plt.savefig(os.path.join(save_dir, 'profil_ordres_totaux.png'), dpi=150, bbox_inches='tight')
    print("   Graphique sauvegardé: profil_ordres_totaux.png")
    
    # 3. Comparaison de différentes polarisations
    print("3. Comparaison des polarisations (n=30, m=4)")
    fig3 = visualiser_comparaison_polarisation(30, 4, [0.0, 0.3, 0.5, 0.7, 1.0])
    plt.savefig(os.path.join(save_dir, 'comparaison_polarisation.png'), dpi=150, bbox_inches='tight')
    print("   Graphique sauvegardé: comparaison_polarisation.png")
    
    # 4. Visualisation de la diversité (pour expliquer la stabilité)
    print("4. Analyse de la diversité des bulletins (n=20, m=5, p=0.5)")
    profil_diversite = generer_profil(20, 5, 0.5)
    fig4 = visualiser_diversite_bulletins(profil_diversite, "Pourquoi les résultats sont stables ?")
    plt.savefig(os.path.join(save_dir, 'diversite_bulletins.png'), dpi=150, bbox_inches='tight')
    print("   Graphique sauvegardé: diversite_bulletins.png")
    print("   ⚠️  Ce graphique montre qu'il n'y a que 2 types de bulletins différents !")
    
    # Afficher les graphiques
    plt.show()
    
    print("\nVisualisation terminée!")
    print("\n💡 EXPLICATION: La fonction generer_profil() ne crée que 2 types de bulletins:")
    print("   1. Un bulletin de base (aléatoire)")
    print("   2. Son opposé exact (complémentaire)")
    print("   Tous les bulletins sont soit identiques au premier, soit identiques au second.")
    print("   C'est pourquoi les résultats sont très stables et prévisibles.")