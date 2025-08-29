import numpy as np
import math
from scipy.optimize import minimize


def main():
    def objective(x):
        return  x[1] * (-1/8) * ((2**(x[0]-1) * (14-x[0])/x[1]) + (2**(x[2]-1) * (14-x[2])/x[3]) + (2**(x[4]-1) * (14-x[4])/x[5]) + (2**(x[6]-1) * (14-x[6])/x[7]) + (2**(x[8]-1) * (14-x[8])/x[9]) + (2**(x[10]-1) * (14-x[10])/x[11]) + (2**(x[12]-1) * (14-x[12])/x[13]) + (2**(x[14]-1) * (14-x[14])/x[15]))
    
    def constraint1(x):
        return x[0]-3

    def constraint2(x):
        return x[2]-3

    def constraint3(x):
        return x[4]-3

    def constraint4(x):
        return x[6]-3

    def constraint5(x):
        return x[8]-3

    def constraint6(x):
        return x[10]-3

    def constraint7(x):
        return x[12]-3

    def constraint8(x):
        return x[14]-3

    def constraint9(x):
        return math.gamma(x[0]+1)/(math.gamma(x[0]-2) * 6) - x[1]

    def constraint10(x):
        return math.gamma(x[2]+1)/(math.gamma(x[2]-2) * 6) - x[3]

    def constraint11(x):
        return math.gamma(x[4]+1)/(math.gamma(x[4]-2) * 6) - x[5]

    def constraint12(x):
        return math.gamma(x[6]+1)/(math.gamma(x[6]-2) * 6) - x[7]

    def constraint13(x):
        return math.gamma(x[8]+1)/(math.gamma(x[8]-2) * 6) - x[9]

    def constraint14(x):
        return math.gamma(x[10]+1)/(math.gamma(x[10]-2) * 6) - x[11]

    def constraint15(x):
        return math.gamma(x[12]+1)/(math.gamma(x[12]-2) * 6) - x[13]

    def constraint16(x):
        return math.gamma(x[14]+1)/(math.gamma(x[14]-2) * 6) - x[15]

    def constraint17(x):
        a = x[16]
        b = x[17]
        c = x[18]
        return 8*3 + a*4 + b*4 + c*4 - x[0] - x[2] - x[4] - x[6] - x[8] - x[10] - x[12] - x[14]
    
    def constraint18(x):
        return x[1] - x[3]
    
    def constraint19(x):
        return x[3] - x[5]
    
    def constraint20(x):
        return x[5] - x[7]
    
    def constraint21(x):
        return x[7] - x[9]
    
    def constraint22(x):
        return x[9] - x[11]
    
    def constraint23(x):
        return x[11] - x[13]
    
    def constraint24(x):
        return x[13] - x[15]

    # initial guesses
    n = 19
    x0 = np.zeros(n)
    x0[0] = 9.0
    x0[1] = 5.0
    x0[2] = 9.0
    x0[3] = 5.0
    x0[4] = 9.0
    x0[5] = 5.0
    x0[6] = 9.0
    x0[7] = 5.0
    x0[8] = 9.0
    x0[9] = 5.0
    x0[10] = 9.0
    x0[11] = 5.0
    x0[12] = 9.0
    x0[13] = 5.0
    x0[14] = 9.0
    x0[15] = 5.0

    #a,b,c
    x0[16] = 2.0
    x0[17] = 2.0
    x0[18] = 2.0

    # show initial objective
    print('Initial SSE Objective: ' + str(objective(x0)))

    # optimize
    b = (0,100)
    c = (1,1000)
    d = (0,100)

    bnds = (b, c, b, c, b, c, b, c, b, c, b, c, b, c, b, c, d, d, d)
    con1 = {'type': 'ineq', 'fun': constraint1}
    con2 = {'type': 'ineq', 'fun': constraint2}
    con3 = {'type': 'ineq', 'fun': constraint3}
    con4 = {'type': 'ineq', 'fun': constraint4}
    con5 = {'type': 'ineq', 'fun': constraint5}
    con6 = {'type': 'ineq', 'fun': constraint6}
    con7 = {'type': 'ineq', 'fun': constraint7}
    con8 = {'type': 'ineq', 'fun': constraint8}
    con9 = {'type': 'ineq', 'fun': constraint9}
    con10 = {'type': 'ineq', 'fun': constraint10}
    con11 = {'type': 'ineq', 'fun': constraint11}
    con12 = {'type': 'ineq', 'fun': constraint12}
    con13 = {'type': 'ineq', 'fun': constraint13}
    con14 = {'type': 'ineq', 'fun': constraint14}
    con15 = {'type': 'ineq', 'fun': constraint15}
    con16 = {'type': 'ineq', 'fun': constraint16}
    con17 = {'type': 'eq', 'fun': constraint17}
    con18 = {'type': 'ineq', 'fun': constraint18}
    con19 = {'type': 'ineq', 'fun': constraint19}
    con20 = {'type': 'ineq', 'fun': constraint20}
    con21 = {'type': 'ineq', 'fun': constraint21}
    con22 = {'type': 'ineq', 'fun': constraint22}
    con23 = {'type': 'ineq', 'fun': constraint23}
    con24 = {'type': 'ineq', 'fun': constraint24}
    cons = ([con1,con2,con3,con4,con5,con6,con7,con8,con9,con10,con11,con12,con13,con14,con15,con16,con17,con18,con19,con20,con21,con22,con23,con24])
    solution = minimize(objective,x0,method='SLSQP',\
                        bounds=bnds,constraints=cons)
    x = solution.x

    # show final objective
    print('Final SSE Objective: ' + str(objective(x)))

    # print solution
    print('Solution')
    print('x1 = ' + str(x[0]))
    print('x2 = ' + str(x[1]))
    print('x3 = ' + str(x[2]))
    print('x4 = ' + str(x[3]))
    print('x5 = ' + str(x[4]))
    print('x6 = ' + str(x[5]))
    print('x7 = ' + str(x[6]))
    print('x8 = ' + str(x[7]))
    print('x9 = ' + str(x[8]))
    print('x10 = ' + str(x[9]))
    print('x11 = ' + str(x[10]))
    print('x12 = ' + str(x[11]))
    print('x13 = ' + str(x[12]))
    print('x14 = ' + str(x[13]))
    print('x15 = ' + str(x[14]))
    print('x16 = ' + str(x[15]))
    print('a = ' + str(x[16]))
    print('b = ' + str(x[17]))
    print('c = ' + str(x[18]))

#test which family set gives maximum charge at end
main()
