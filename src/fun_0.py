import numpy as np
    
def fun_0(PL = None,f = None,Go = None): 
    #FUN
#    EQN_3 = FUN_0(DIST_TUAV_UAV,PL,F,GO)
    
    #    This function was generated by the Symbolic Math Toolbox version 8.1.
#    06-Jan-2021 16:11:41
    
    t2 = np.log(10.0)
    t3 = 1.0 / t2
    eqn_3 = lambda dist_TUAV_UAV = None: np.multiply(Go,- 2.0) - PL + np.multiply(np.multiply(t3,np.log(dist_TUAV_UAV)),20.0) + np.multiply(np.multiply(t3,np.log(f)),20.0) - 295.0 / 2.0
    return eqn_3