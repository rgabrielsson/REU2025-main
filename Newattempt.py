# V - list of charge by visibility

def charge_dict():
    dict = {}
    for i in range(15):
        dict[i] = 2**(i-1) * (14 - i)
    return dict

V = charge_dict()



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
    V = charge_dict()
    charge_initial_i = V[visibility] / membership
    return charge_initial_i


#total = ch1+ch2+ch3+ch4+ch5+ch6+ch7+ch8
#r_i = recieved charge of i
#M = max charge

#We have 8 inequalities of the form
#M > membership(i) * r_i
#new_total = sum of r_i
# 1 <= membership(i) <= (visibility(i) choose 3)
#Goal: minimize M

