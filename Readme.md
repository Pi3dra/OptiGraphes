# Sujet Finance 
Groupe de: Vladimir Herrera Nativi, Bartolomei Pedro, Raphael Leonardi

Ce repo explore l’échange de devises via une **modélisation de graphe orienté** :
---
## Aperçu des 3 algorithmes

### Algo 1 — (naïf)
- **Idée** : à chaque étape, depuis le nœud courant `x`, choisir l’arc sortant `(x,y)` de **meilleure valuation**. Répéter jusqu’à épuiser le budget d’échanges, puis **revenir à EUR**.

### Algo 2 — chemins
- **Idée** : **générer tous** les chemins de longueur `p` qui **commencent et finissent par EUR** (option : interdire `x_i = x_{i-1}`), puis **sélectionner le max**.
- **Forces** : donne le **vrai optimum** (dans l’espace exploré).
- **Limites** : explosion combinatoire quand `p` ou le degré moyen augmentent.
- **Complexité** : exponentielle `≈ O(3^p)` ; utiliser des générateurs (yield) pour éviter de tout stocker.

### Algo 3 — Chemins Log
- **Idée** : **Similiare a l'algo 2** on etudie les different chemins possibles mais au lieu de calculer des produit on maximise une **somme de logs**.
- - **Forces** : Utilisation de **programmation dynamique** pour optimiser encore plus la complexite algorithmique.
- **Complexité** : `O(p · |U|)`.

---




