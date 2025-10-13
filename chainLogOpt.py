from math import log, exp
from typing import List, Tuple

# Indices: 0=EUR, 1=USD, 2=JP, 3=CHF
matrix = [
    [1.00, 1.19, 1.33, 1.62],  # EUR ->
    [0.84, 1.00, 1.12, 1.37],  # USD ->
    [0.75, 0.89, 1.00, 1.22],  # JP  ->
    [0.62, 0.73, 0.82, 1.00],  # CHF ->
]

CODES = ["EUR", "USD", "JP", "CHF"]  # pour affichage

def best_path_max_product(p: int) -> Tuple[List[int], float]:
    """
    Retourne (chemin_optimal, produit_max) pour une chaîne de longueur p (p symboles),
    début EUR (0) et fin EUR (0), sans répétition immédiate.

    Complexité: O(p * 4 * 4).
    """
    if p < 2:
        # Longueurs < 2 n'ont pas de sens ici
        return [], 0.0
    L = p - 1  # nombre d'échanges

    # On travaille en log pour la stabilité numérique:
    # log(0) n'arrive pas ici (les taux sont >0). On interdit u==v en mettant -inf.
    NEG_INF = float("-inf")
    logM = [[NEG_INF]*4 for _ in range(4)]
    for u in range(4):
        for v in range(4):
            if u != v:
                logM[u][v] = log(matrix[u][v])

    # dp[t][v] = meilleur log-produit pour t échanges et fin au noeud v
    dp = [[NEG_INF]*4 for _ in range(L+1)]
    prev = [[-1]*4 for _ in range(L+1)]

    # Départ: 0 échange, on est à EUR (0) avec log-produit = 0
    dp[0][0] = 0.0

    for t in range(1, L+1):
        for v in range(4):
            # Interdit de rester en place: u != v
            best_val = NEG_INF
            best_u = -1
            for u in range(4):
                if u == v:
                    continue
                cand = dp[t-1][u] + logM[u][v]
                if cand > best_val:
                    best_val = cand
                    best_u = u
            dp[t][v] = best_val
            prev[t][v] = best_u

    # On doit finir à EUR (0) après L échanges
    best_log = dp[L][0]
    if best_log == NEG_INF:
        return [], 0.0  # pas de chemin (ne devrait pas arriver avec ce graphe)

    # Reconstruction du chemin de longueur p (p noeuds)
    path = [0] * p
    v = 0
    t = L
    while t >= 0:
        path[t] = v
        v = prev[t][v] if t > 0 else v
        t -= 1

    return path, exp(best_log)


# --------- Exemple d’usage ----------
if __name__ == "__main__":
    for p in [3, 4, 5, 10, 16, 24, 128]:
        path, gain = best_path_max_product(p)
        if path:
            labels = [CODES[x] for x in path]
            print(f"p={p}  gain max = {gain:.6f}")
            print("chemin:", path, " / ", " -> ".join(labels))
            print("-"*50)
