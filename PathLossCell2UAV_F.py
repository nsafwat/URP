import numpy as np
from A2G import A2G
from Cell2UAV import Cell2UAV
import scipy as sp 
from fun_1_2_1 import fun_1_2_1
from fun_1_2 import fun_1_2
from fun_1_3 import fun_1_3 
from fun_1_4 import fun_1_4
def PathLossCell2UAV_F(env = None,f = None,h_ms = None,A2G_Tx = None,A2G_Rx = None,C2U_Tx = None,C2U_Rx = None,h_BS = None): 
    #=========================================================================#
    
    a_A2G_val = np.array([15,11,5])
    b_A2G_val = np.array([0.18,0.16,0.3])
    eta_LOS_val = np.array([1.6,1,0.1])
    eta_NLOS_val = np.array([23,20,21])
    # parameter a _Porbability of LOS
    a = a_A2G_val[env]
    # parameter b _Porbability of LOS
    b = b_A2G_val[env]
    # eta_LOS
    eta_LOS = eta_LOS_val[env]
    #eta_NLOS
    eta_NLOS = eta_NLOS_val[env]
    #Freq
#f=5800000000;
#h_ms=1.5;
#A2G TX power
    Ptx = A2G_Tx
    #A2G Rx power
    Prx = A2G_Rx
    #C2U Rx power
    Px = C2U_Tx
    #C2U Tx power
    Pr = C2U_Rx
    #Pr={-80,-90,-100,-110,-120,-130};
#Pr={-70,-80,-90,-100,-110,-110};
#Pr={-80,-85,-90,-95,-100,-105};
    
    #Pr={-60,-75,-80,-85,-90,-95};
#Pr={-60,-65,-70,-75,-80,-80};
#Pr={-60,-65,-70,-75,-80,-80};
    
    #path loss exponent
    gam = np.array([3.5,3.2,3])
    gamma = gam[env]
    #gamma=3;
    
    A = - 23.61
    B = 4.14
    seta_o = - 3.61
    eta_o = 20.7
    #h_BS=35;
    PL = Px - Pr
    #=========================================================================#
#=========================================================================#
#Air to Ground PathLoss
#=========================================================================#
    Seta_A2G_opt,R_A2G,h_UAV_A2G = A2G(a,b,eta_LOS,eta_NLOS,f,h_ms,Ptx,Prx)
    #=========================================================================#
    
    #=========================================================================#
#=========================================================================#
#Cell to UAV PathLoss
#=========================================================================#
    seta_C2U_opt,dist_C2U_C = Cell2UAV(Px,Pr,f,gamma,A,B,seta_o,eta_o)
    #=========================================================================#
    h_UAV_C2U = dist_C2U_C * np.tan(3.14 / 180 * seta_C2U_opt) + h_BS
    #=========================================================================#
#=========================================================================#
#==============Recalculate UAV_h========================================#

    if (h_UAV_C2U == h_UAV_A2G):
        h_UAV = h_UAV_A2G
    else:
        if (h_UAV_C2U > h_UAV_A2G):
            h_UAV = h_UAV_A2G
            h_UAV_C2U = h_UAV
            R_A2G = (h_UAV - h_ms) / np.tan(3.14 / 180 * Seta_A2G_opt)
            #      syms eqn seta
            if h_UAV_C2U < h_BS:
                #      eqn=-PL+10*gamma*(log10(h_BS-h_UAV_C2U)-log10(tan(3.14/180*(-seta))))-147.5+20*log10(f)+A*((-seta)-seta_o)*exp(-((-seta)-seta_o)/B)+eta_o;
#      seta_C2U_C=vpasolve(eqn==0,seta,[-10,10]);
                seta_C2U_C = sp.optimize.fsolve(fun_1_2_1(PL,gamma,h_UAV_C2U,h_BS,f,A,seta_o,B,eta_o),- 1)
            else:
                #      eqn=-PL+10*gamma*(log10(h_UAV_C2Uh_BS)-log10(tan(3.14/180*(seta))))-147.5+20*log10(f)+A*((seta)-seta_o)*exp(-((seta)-seta_o)/B)+eta_o;
#      seta_C2U_C=vpasolve(eqn==0,seta,[-10,10]);
                seta_C2U_C = sp.optimize.fsolve(fun_1_2(PL,gamma,h_UAV_C2U,h_BS,f,A,seta_o,B,eta_o),1)

            dist_C2U_C = (h_UAV_C2U - h_BS) / np.tan(3.14 / 180 * seta_C2U_C)
        else:
            #      syms eqn h seta
#      eqn=-PL+10*gamma*(log10(h)-log10(tan(3.14/180*seta)))-147.5+20*log10(f)+A*(seta-seta_o)*exp(-(seta-seta_o)/B)+eta_o;
#      sol=diff(eqn,seta);
#      seta_C2U_C=vpasolve(sol==0,seta,[0,10]);
            seta_C2U_C = sp.optimize.fsolve(fun_1_4(gamma,A,seta_o,B),1)
            seta = (seta_C2U_C)
            #      syms eqn h
#      eqn=-PL+10*gamma*(log10(h)-log10(tan(3.14/180*seta)))-147.5+20*log10(f)+A*(seta-seta_o)*exp(-(seta-seta_o)/B)+eta_o;
#      h_UAV_C2U=vpasolve(eqn==0,h)+h_BS;
            h_UAV_C2U = sp.optimize.fsolve(fun_1_3(PL,gamma,seta,f,seta_o,A,B,eta_o),10) + h_BS
            if (h_UAV_C2U > h_UAV_A2G):
                h_UAV_C2U = h_UAV_A2G
            dist_C2U_C = (h_UAV_C2U - h_BS) / np.tan(3.14 / 180 * seta_C2U_C)
            h_UAV = h_UAV_C2U
            R_A2G = (h_UAV - h_ms) / np.tan(3.14 / 180 * Seta_A2G_opt)
    
    # plc(i,1)= double(dist_C2U_C);
# plc(i,2)= double(h_UAV);
# plc(i,3)= double(R_A2G);
    # dist_C2U_C = int(dist_C2U_C)
    # h_UAV = int(h_UAV)
    # R_A2G = int(R_A2G)
    return R_A2G,h_UAV,dist_C2U_C
    
