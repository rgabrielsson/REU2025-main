import math

#get charge on a given 0-ving based on formula
def calc_charge(val,fams):
    charge = 2**(val-1) * (14-val)
    charge = charge / fams
    return charge

#get every possible family
def get_families():
    families = [(a, b, c) for a in range(25) for b in range(a, 25) for c in range(b, 25) if a + b + c <= 25]    
    return families         


def families():
    families = get_families()
    worst_charge = 0
    pairings = []

    #iterate over families to find the ones with highest charge
    for family in families:
        a = family[0]
        b = family[1]
        c = family[2]
        vis = (math.comb(a+3, 3), math.comb(b+3, 3), math.comb(c+3, 3), math.comb(a+b+3, 3), math.comb(a+c+3, 3), math.comb(b+c+3, 3), math.comb(a+b+c+3, 3))
        c3 = calc_charge(3, 1)
        ca = calc_charge(a+3, vis[0])
        cb = calc_charge(b+3, vis[1])
        cc = calc_charge(c+3, vis[2])
        cab = calc_charge(a+b+3, vis[3])
        cac = calc_charge(a+c+3, vis[4])
        ccb = calc_charge(b+c+3, vis[5])
        cabc = calc_charge(a+b+c+3, vis[6])
        charges = [c3, ca, cb, cc, cab, cac, ccb, cabc]
        total = sum(charges) / len(charges)
        pairings.append((total * max(vis), max(vis), total,(a,b,c)))

        #identify highest possible total charge
        if total * c >= worst_charge:
            worst_charge = total * c
    
    outfile = open("famstest.txt","w")

    #find all families that give the worst possible charge
    pairings.sort()
    for pairing in pairings:
        print(pairing,file = outfile)
    
    outfile.close

families()