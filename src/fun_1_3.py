import numpy as np
    
def fun_1_3(PL = None,gamma = None,seta = None,f = None,seta_o = None,A = None,B = None,eta_o = None): 
    #FUN_1_3
#    EQN = FUN_1_3(H,PL,GAMMA,SETA,F,SETA_O,A,B,ETA_O)
    
    #    This function was generated by the Symbolic Math Toolbox version 8.1.
#    09-Jan-2021 01:45:00
    
    t2 = np.log(10.0)
    t3 = 1.0 / t2
    t4 = seta - seta_o
    eqn = lambda h = None: - PL + eta_o - np.multiply(np.multiply(gamma,(np.multiply(t3,np.log(np.tan(np.multiply(seta,0.01744444444444444)))) - np.multiply(t3,np.log(h)))),10.0) + np.multiply(np.multiply(t3,np.log(f)),20.0) + np.multiply(np.multiply(A,t4),np.exp(- t4 / B)) - 295.0 / 2.0
    return eqn