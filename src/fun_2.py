import numpy as np
    
def fun_2(PL = None,f = None,Go = None,h_B = None,h_UAV = None,L_r = None,a_A2A = None,b_A2A = None): 
    #FUN_2
#    EQN_3 = FUN_2(DIST_TUAV_UAV,PL,F,GO,SETA_3DB,H_B,H_UAV,L_R,A_A2A,B_A2A)
    
    #    This function was generated by the Symbolic Math Toolbox version 8.1.
#    06-Jan-2021 16:33:46
    
    t2 = np.log(10.0)
    t3 = 1.0 / t2
    t4 = np.multiply(a_A2A,b_A2A)
    t5 = np.exp(t4)
    t6 = np.multiply(a_A2A,t5)
    t7 = t6 + 1.0
    t8 = 1.0 / t7
    t9 = np.log(f)
    eqn_3 = lambda dist_TUAV_UAV = None: np.multiply(Go,- 2.0) - PL + np.multiply(np.multiply(t3,np.log(t8 - np.multiply(10.0 ** (np.multiply(np.multiply(t3,np.log(np.multiply(np.sqrt(2.0),1.0) / L_r ** 2 + 1.0)),(- 1.0 / 2.0)) + np.multiply(np.multiply(t3,t9),(1.0 / 2.0)) + np.multiply(np.multiply(t3,np.log(h_B - h_UAV)),(1.0 / 2.0)) - 86.0 / 25.0),(t8 - 1.0)))),20.0) + np.multiply(np.multiply(t3,t9),20.0) + np.multiply(np.multiply(t3,np.log(dist_TUAV_UAV)),20.0) - 295.0 / 2.0
    return eqn_3