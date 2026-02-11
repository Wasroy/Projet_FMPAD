# Explication des graphiques de visualisation

## 1. Graphique "Profil binaire" (profil_binaire.png)

**Ce que ça représente :**
- Ce graphique montre le **nombre de votants qui approuvent chaque candidat** dans un système de vote par approbation (oui/non).
- Chaque barre indique combien de personnes ont voté "oui" (1) pour ce candidat.
- Plus la barre est haute, plus le candidat est populaire.

**Exemple :** Si le Candidat 1 a une barre à 15, cela signifie que 15 votants sur 20 ont approuvé ce candidat.

**Paramètres :**
- `n` : nombre total de votants
- `m` : nombre de candidats
- `p` : polarisation (0 = consensus, 1 = opposition totale)

---

## 2. Graphique "Profil d'ordres totaux" (profil_ordres_totaux.png)

**Ce que ça représente :**
- Ce graphique montre le **rang moyen** de chaque candidat dans les classements des votants.
- Chaque candidat est classé de 1 (meilleur) à m (pire) par chaque votant.
- La barre indique la position moyenne : plus c'est bas (proche de 1), mieux c'est.

**Exemple :** Si le Candidat 1 a un rang moyen de 2.3, cela signifie qu'en moyenne, les votants le placent en 2ème ou 3ème position.

**Note :** L'axe Y est inversé (1 en haut, m en bas) pour que le meilleur candidat soit visuellement en haut.

---

## 3. Graphique "Comparaison polarisation" (comparaison_polarisation.png)

**Ce que ça représente :**
- Ce graphique compare l'effet de la **polarisation** sur les votes par approbation.
- Chaque sous-graphique montre la distribution des votes pour une valeur de polarisation différente.

**Interprétation de la polarisation :**
- **p = 0.0** : Consensus total → tous les votants ont le même bulletin
- **p = 0.5** : Polarisation modérée → mélange de bulletins similaires et opposés
- **p = 1.0** : Opposition totale → deux groupes avec des bulletins complètement opposés

**Observation :** Plus la polarisation est élevée, plus les votes sont concentrés sur certains candidats (effet de groupe).
