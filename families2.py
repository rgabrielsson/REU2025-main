"""
How many triangles?

The membership keeps increasing

There must be a rule

Ta + Tb <= Tab


Steps:
1. Get total charge for each member
2. Get charge divided by membership
3. Average based on number of contributions

Goal: minimize x, where x is at most charge_v * membership_v for each member

Linear programming




Variables: 
- membership of each family member
- charge of each family member
- visibility of each family member



Path 1:
- enumerate all cases
- use linear programming for each separately
- will take more cases and more time, but less effort
- solve for every possible visibility

Path 2:
- use code that solves for every case at once using variables
- seems smarter
- visibility charge(4) <= certain amount


Note:
- variables are not integers
- ignore for now, it will probably not matter






Worst case:
- 7 things have maximum charge = 7 * 4096
- smallest visiblity such that charge(p) * visibility(p) >= 7 * 4096
- happens really quick, at like 23

"""



"""
Notes:

- For each family member, determine how many different families it can contribute to.
- Then, give an equal share of the total charge to each family (and for each possible case)
- Now, calculate the total charge on each family in every one of these cases
- Finally, give a weighted amount of charge back to each family member based on their contribution to the families they are part of.

Thus, for each member,


visibility
cont_fams <= vis choose 3 (very naive bound, find a better one later)
charge = total charge / cont_fams ?



Goal: minimize x, where x is at most charge_v * membership_v for each member

Put in format:
Minimize :  x = charge_v * membership_v
Subject to the constraints: 
T = 3
Ta, Tb, Tc >= 3
Ta + Tb - 3 <= Tab
Ta + Tc - 3 <= Tac
Tc + Tb - 3 <= Tbc
Ta + Tb + Tc - 6 <= Tabc
d = a+b+c+3

f <= math.comb(T,3)
fa <= math.comb(Ta,3)
fb <= math.comb(Tb,3)
fc <= math.comb(Tc,3)
fab <= math.comb(Tab,3)
fac <= math.comb(Tac,3)
fbc <= math.comb(Tbc,3)
fabc <= math.comb(Tabc,3)

"""




"""
from itertools import combinations
import math
from scipy.optimize import linprog





# import the library pulp as p
import pulp as p

# Create a LP Minimization problem
Lp_prob = p.LpProblem('Problem', p.LpMaximize) 

# Create problem Variables 
T = p.LpVariable("T", lowBound = 3)   # Create a variable T == 3 
Ta = p.LpVariable("Ta", lowBound = 3)   # Create a variable Ta >= 3
Tb = p.LpVariable("Tb", lowBound = 3)   # Create a variable Tb >= 3
Tc = p.LpVariable("Tc", lowBound = 3)   # Create a variable Tc >= 3
Tab = p.LpVariable("Tab", lowBound = 3)   # Create a variable Tab >= 3
Tac = p.LpVariable("Tac", lowBound = 3)   # Create a variable Tac >= 3
Tbc = p.LpVariable("Tbc", lowBound = 3)   # Create a variable Tbc >= 3
Tabc = p.LpVariable("Tabc", lowBound = 3)   # Create a variable Tabc >= 3

f = p.LpVariable("f", lowBound = 1)   # Create a variable Tabc >= 3

# Objective Function
Lp_prob += 1024/3 * T / f

# Constraints:
Lp_prob += T == 3
Lp_prob += Ta, Tb, Tc >= 3
Lp_prob += Tab >= Ta + Tb - 3
Lp_prob += Tac >= Ta + Tc - 3
Lp_prob += Tbc >= Tc + Tb - 3
Lp_prob += Tabc >= Ta + Tb + Tc - 6

Lp_prob += f <= math.comb(T,3)
Lp_prob += fa <= math.comb(Ta,3)
Lp_prob += fb <= math.comb(Tb,3)
Lp_prob += fc <= math.comb(Tc,3)
Lp_prob += fab <= math.comb(Tab,3)
Lp_prob += fac <= math.comb(Tac,3)
Lp_prob += fbc <= math.comb(Tbc,3)
Lp_prob += fabc <= math.comb(Tabc,3)

# Display the problem
print(Lp_prob)

status = Lp_prob.solve()   # Solver
print(p.LpStatus[status])   # The solution status

# Printing the final solution
print(p.value(x), p.value(y), p.value(Lp_prob.objective))  







#Imagine you know a,b,c
#enumerate all cases

def get_families():
    families = [(a, b, c) for a in range(25) for b in range(a, 25) for c in range(b, 25) if a + b + c <= 40]    
    return families 

families = get_families()



for family in families:
    a = family[0]
    b = family[1]
    c = family[2]
    T = 3
    Ta = a + 3
    Tb = b + 3
    Tc = c + 3
    Tab = a + b + 3
    Tac = a + c + 3
    Tbc = b + c + 3
    Tabc = a + b + c + 3

    f = math.comb(T, 3)
    
"""



import pulp as p
# Create a LP Minimization problem
Lp_prob = p.LpProblem('Problem', p.LpMaximize) 

# Create problem Variables 
fams_v = p.LpVariable("fams_v", lowBound=1)   # Create a variable for the total number of families that v can be in
vis_v = p.LpVariable("vis_v", lowBound=3)   # Create a variable for the visibility of v
charge_v = p.LpVariable("charge_v", lowBound=0)   # Create a variable for the charge on v

# Objective Function
Lp_prob += charge_v * fams_v

# Constraints:
Lp_prob += fams_v <= 30 * vis_v    # there cannot be more families than the number of different ways to triangulate the shape with vis vertices, since it must always be in a triangle, and that triangle must be part of a triangulation
Lp_prob += charge_v <= (1024/3 * 7 + 44)/8    # limit for the averaged charge on a family (with partial charges)


# Display the problem
print(Lp_prob)

status = Lp_prob.solve()   # Solver
print(p.LpStatus[status])   # The solution status

# Printing the final solution
print(p.value(x), p.value(y), p.value(Lp_prob.objective))  

