import numpy as np
    
def fun_1_4(gamma = None,A = None,seta_o = None,B = None): 
    #FUN_1_4
#    EQN = FUN_1_4(SETA,PL,GAMMA,F,A,SETA_O,B,ETA_O)
    
    #    This function was generated by the Symbolic Math Toolbox version 8.1.
#    09-Jan-2021 12:53:32
    
    # t2 = seta.*1.744444444444444e-2;
# t3 = tan(seta.*1.744444444444444e-2);
    t4 = 1.0 / B
    # t5 = seta-seta_o;
# t6 = exp(-(1.0./B).*(seta-seta_o));
    eqn = lambda seta = None: np.multiply(A,(np.exp(np.multiply(- (1.0 / B),(seta - seta_o))))) - (np.multiply(np.multiply(gamma,((np.tan(np.multiply(seta,0.01744444444444444))) ** 2.0 * 0.01744444444444444 + 0.01744444444444444)),4.342944819032518)) / (np.tan(np.multiply(seta,0.01744444444444444))) - np.multiply(np.multiply(np.multiply(A,t4),(seta - seta_o)),(np.exp(np.multiply(- (1.0 / B),(seta - seta_o)))))
    return eqn