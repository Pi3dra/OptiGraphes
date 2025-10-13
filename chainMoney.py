           # EUR  USD    JP   CHF
matrix =[ [1   , 1.19, 1.33, 1.62], # EUR
          [0.84,    1, 1.12, 1.37], # USD
          [0.75, 0.89,    1, 1.22], # JP
          [0.62, 0.73, 0.82, 1   ]] # CHF

def links_of_path(path : list[int]):
    value_path = []
    for i in range(len(path)-1):
        value_path.append(matrix[path[i]][path[i+1]])
    return value_path
        
def path_money(path):
    collector = 1
    for i in path:
        collector *= i
    return collector


ALPHABET = ("0", "1", "2", "3")

def generate_chains(p):
    """
    Génère toutes les chaînes de longueur p:
      - commencent par 'E' et finissent par 'E'
      - sans deux caractères identiques consécutifs
    Retourne un générateur (itérer pour parcourir sans tout stocker).
    """
    if p < 2:
        return
    if p == 2:
        return
    if p == 3:
        for mid in ("1", "2", "3"):
            yield "0" + mid + "0"
        return

    # Positions 2..p-1 (p-2 positions internes)
    # On impose les contraintes localement pour éviter l'explosion combinatoire.
    def backtrack(prefix):
        i = len(prefix) # index 0..(p-1)
        if i == p:
            yield "".join(prefix)
            return

        if i == 0:
            choices = ("0",)
        elif i == p-1:
            choices = ("0",)
        else:
            prev = prefix[-1]
            choices = (c for c in ALPHABET if c != prev)

        for c in choices:
            if i > 0 and c == prefix[-1]:
                continue
            prefix.append(c)
            yield from backtrack(prefix)
            prefix.pop()

    yield from backtrack(prefix=[])


def list_chains(p):
    """Renvoie la liste (attention: peut être grande)."""
    return list(generate_chains(p))

def string_to_int_list(liste):
    path = []
    for i in liste:
        path.append(int(i))
    return path

if __name__ == "__main__":
    for p in range(3, 14):
        print(f"TAILLE {p}")
        chains = list_chains(p)
        print(f"TOTAL {len(chains)}")

        max_value = 0

        biggest = ()

        for chain in chains:
            corrected = string_to_int_list(chain)
            value = path_money(links_of_path(corrected))

            if value > max_value:
                max_value = value
                biggest = (corrected,value)
        print("BEST: ", biggest , "\n")
        