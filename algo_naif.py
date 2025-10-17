           # EUR  USD    JP   CHF
matrix =[ [1   , 1.19, 1.33, 1.62], # EUR
          [0.84,    1, 1.12, 1.37], # USD
          [0.75, 0.89,    1, 1.22], # JP
          [0.62, 0.73, 0.82, 1   ]] # CHF


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
def find_biggest_path( limit : int):
    path = [0]
    counter = limit 
    while counter > 1:
        (idx, _ ) = get_biggest_link(path[-1])
        path.append(idx)
        counter -= 1
    path.append(0)
    return path


ALPHABET = ("0", "1", "2", "3")

def string_to_int_list(liste):
    path = []
    for i in liste:
        path.append(i)
    return path

def int_path_to_string(path):
    devises = ["EUR", "USD", "JP", "CHF"]
    chaine = [devises[i] for i in path]
    return "->".join(chaine)

if __name__ == "__main__":
    for p in range(2, 16):
        path = find_biggest_path(p)
        chaine = int_path_to_string(path)
        exch_values = links_of_path(path)
        gain = path_money(exch_values)
        print(f"taille: {p} \ngain: {gain:.6f} \nchemin: {chaine} ")
        print("-" * 50)
