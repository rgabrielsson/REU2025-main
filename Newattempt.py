# V - list of charge by visibility

def charge_dict():
    dict = {i:2**(i-1) * (14 - i) for i in range(40)}
    return dict


#ch1 <= V(visibility_i + 3)/membership_i
#total = ch1+ch2+ch3+ch4+ch5+ch6+ch7+ch8
#r_i = recieved charge of i
#M = max charge

#We have 8 inequalities of the form
#M > membership(i) * r_i
#total = sum of r_i
# 1 <= membership(i) <= ??
#Goal: minimize M




#ch1 <= V(visibility_i)/membership_i

def calc_charge(visibility, membership):
    chargeDict = charge_dict()
    charge_initial_i = chargeDict[visibility] / membership
    return charge_initial_i


#total = ch1+ch2+ch3+ch4+ch5+ch6+ch7+ch8
#r_i = recieved charge of i
#M = max charge

#We have 8 inequalities of the form
#M > membership(i) * r_i
#new_total = sum of r_i
# 1 <= membership(i) <= (visibility(i) choose 3)
#Goal: minimize M


#dictionary of maximum number of families for each visibility
#Finish this with list from notebook (ends after 9)
max_fams = {3:1, 4:2,5:5, 6:8, 7:14, 8:23, 9:30, 10:120, 11:165, 12:220, 13:286, 14:364, 15:455, 16:560, 17:680, 18:816, 19:969, 20:1140, 21:1330, 22:1540, 23:1771, 24:2024, 25:2300, 26:2600, 27:2925, 28:3276, 29:3654, 30:4060}


#step 1: divide charge of v by membership of v
#this requires an iterator through all possible memberships (1 < m < max_fams[i])

# #vis is the visibility of a given vertex v
# def main():
#     for vis in range(3,15):
#         #memb is the number of families that v is in
#         for memb in range(3, max_fams[vis]):
#             charge_v_given = calc_charge(vis, memb)


#step 2: figure out what charges each family was given by its 8 members and sum them up
# define a,b,c for a family and then calculate what the charge would be for each of its members


def main():
    returned_charges = []
    #list every possible family
    fam_options = [(a,b,c) for a in range(10) for b in range(a,10) for c in range(b,10)]

    #for each family, calculate the possible visibilies of each member and get their contributed charges from that
    for family in fam_options:
        a,b,c = family
        #calculate the visibilities of each member and put them in a list
        visibilities = [3, 3+a, 3+b, 3+c, 3+a+b, 3+a+c, 3+b+c, 3+a+b+c]

        charge_options = {}
        #for each member, get every possible charge it could contribute and match it to its membership
        for vis in visibilities:
            #for each visibility, get the contributed charge for every possible membership
            for memb in range(1, max_fams[vis]+1):
                charge_contributed = calc_charge(vis, memb)
                if vis not in charge_options:
                    charge_options[vis] = (charge_contributed, memb)
                else:
                    charge_options[vis] = max(charge_options[vis], (charge_contributed, memb))
        #now charge_options has the maximum charge that could be contributed by each member given its visibility and membership
        total_charge = sum([charge_options[vis][0] for vis in visibilities])

        charge_returned = total_charge / 8

        returned_charges.append(charge_returned)
    
    print(max(returned_charges))


        
                
            #get charge contributed by this member given its visibility and membership


main()

#step 3: figure out the maximum charge given to any family










# opt >= charge_returned * membership(original_vertex)