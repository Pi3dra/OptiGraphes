

           # EUR  USD    JP   CHF
matrix =[ [1   , 1.19, 1.33, 1.62], # EUR
          [0.84,    1, 1.12, 1.37], # USD
          [0.75, 0.89,    1, 1.22], # JP
          [0.62, 0.73, 0.82, 1   ]] # CHF



def index_to_string(index : int):
    match index:
        case 0: "EUR"
        case 1: "USD"
        case 2: "JP"
        case 3: "CHF"

def get_biggest_link(index: int):
    max = 0
    final_index = 0
    for (idx, elt) in enumerate(matrix[index]):
        if  elt > max:
            max = elt
            if idx != index:
                final_index = idx

    return (final_index, max)

def links_of_path(path : list[int]):
    value_path = []
    for i in range(len(path)-1):
        value_path.append( matrix[int(path[i])][int(path[i+1])])
    return value_path
        
def path_money(path):
    collector = 1
    for i in path:
        collector *= i
    return collector

# Biggest path approach

def path_money2(path):
    collector = 1
    for i in path:
        collector *= i
    return collector

def find_biggest_path( limit : int):
    path = [0]
    counter = limit 
    while counter > 1:
        (idx, _ ) = get_biggest_link(path[-1])
        path.append(idx)
        counter -= 1
    path.append(0)
    return path

# Path enumeration

    


#for i in range(10):
#    path = find_biggest_path(i*5)
#    edges =  links_of_path(path)
#    print(path_money(edges))
               


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
        path.append(i)
    return path

if __name__ == "__main__":
    for p in range(2, 14):
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
        
        #print(f"p={p}: {len(chains)} chaînes, formule={count_chains_closed_form(p)}")
        # Affiche un aperçu pour p petit
        #if len(chains) <= 30:
        #print(chains)
        #print("-" * 40)


