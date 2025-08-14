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
        vis_dividers = [(d, e, f, g, h, i, j) for d in range(1, 30*(a+3)) for e in range(1, 30*(b+3)) for f in range(1, 30*(c+3)) for g in range(1, 30*(a+b+3)) for h in range(1, 30*(a+c+3)) for i in range(1, 30*(b+c+3)) for j in range(1, 30*(a+b+c+3))]
        for vis in vis_dividers:
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
            pairings.append((total * max(vis), total,(a,b,c)))

            #identify highest possible total charge
            if total >= worst_charge:
                worst_charge = total
    
    outfile = open("famstest.txt","w")

    #find all families that give the worst possible charge
    pairings.sort()
    for pairing in pairings:
        print(pairing,file = outfile)
    
    outfile.close

families()
