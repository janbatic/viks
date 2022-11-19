import itertools
from main import fn_cezar


def fnLSFR(seme=None, odcepi=None):
    if odcepi is None:
        odcepi = []
    if seme is None:
        seme = []
    zaporedje = []
    zaporedje.append(seme[-1])
    racunano_seme = seme.copy()
    for i in range(pow(2, len(seme)) - 1):
        new_bit = 0
        odcep1 = racunano_seme[odcepi[0] - 1]
        odcep2 = racunano_seme[odcepi[1] - 1]
        for j in range(len(odcepi)):
            new_bit = new_bit ^ racunano_seme[odcepi[j]-1]
        racunano_seme[1:] = racunano_seme[:-1]
        racunano_seme[0] = new_bit
        if racunano_seme == seme:
            break
        zaporedje.append(racunano_seme[-1])
    return zaporedje, len(zaporedje)


if __name__ == '__main__':
    print(fnLSFR([1, 0, 1, 0], [2, 4]))
    seme = [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0]
    combinations = []
    stuff = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
    for L in range(len(stuff) + 1):
        for subset in itertools.combinations(stuff, L):
            combinations.append(list(subset))
    combinations.remove([])
    for combination in combinations:
        zaporedje, perioda = fnLSFR(seme, [*combination, 12])
        if perioda == 4095:
            combination.append(12)
            print(combination, perioda)
