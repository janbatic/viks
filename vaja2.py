
def fnAnaliza(niz):
    statistica ={}
    for char in niz:
        if char in statistica.keys():
            statistica[char] += 1
        else:
            statistica[char] = 1
    bigrami = {}
    for i in range(len(niz)-1):
        if niz[i:i+2] in bigrami.keys():
            bigrami[niz[i:i+2]] += 1
        else:
            bigrami[niz[i:i+2]]=1
    trigrami = {}
    for i in range(len(niz)-1):
        if niz[i:i+3] in trigrami.keys():
            trigrami[niz[i:i+3]] += 1
        else:
            trigrami[niz[i:i+3]] = 1
    monogrami = {k: v for k, v in sorted(statistica.items(), key=lambda item: item[1])}
    bigrami2 = {x: y for x, y in sorted(bigrami.items(), key=lambda item: item[1])}
    trigrami2 = {a: b for a, b in sorted(trigrami.items(), key=lambda item: item[1])}
    return monogrami,

def fn_substitucija(cistopis, smer=True):
    kljuc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    abeceda = 'L _S_BAIVMCYUDGNWTO_FRX_HPE'
    if cistopis.islower():
        kljuc = kljuc.lower()
        abeceda = abeceda.lower()
    sifropis=''
    for i, char in enumerate(cistopis):
        if char in ['_', ',', '.']:
            sifropis += char
        elif smer:
            sifropis += kljuc[abeceda.index(char)]
        else:
            sifropis += abeceda[kljuc.index(char)]

    return sifropis

if __name__ == '__main__':
    niz = 'HPBKVLZRSOVGZYLBGBDMFDRHRMRHSPBKHZY VBHDBGBJ RYSNBSUB PKSNHPOBFLBQYHKYBMPHRDBSUBZAGHPR WRBGV BV ZAGK NBQHRYBKHZY VR WRBGKKSVNHPOBRSBGBV OMAGVBDLDR JBRY BMPHRDBJGLBF BDHPOA BA RR VDBRY BJSDRBKSJJSPBZGHVDBSUBA RR VDBRVHZA RDBSUBA RR VDBJHWRMV DBSUBRY BGFSI BGPNBDSBUSVRYBRY BV K HI VBN KHZY VDBRY BR WRBFLBZ VUSVJHPOBGPBHPI VD BDMFDRHRMRHSP'
    print(fnAnaliza(niz))
    print(fn_substitucija(niz, False))
    cankar = open("Na_klancu.txt").read().upper()
    list = ["!", ".", ".","'",'*','—','?','„','“',';','8','6','~','Π','\n','-','/']
    for x in list:
        cankar = cankar.replace(x,"")
    x=1
    print(fnAnaliza(cankar))