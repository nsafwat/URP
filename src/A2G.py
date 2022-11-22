
from fun_7 import fun_7
from fun_8 import fun_8
import numpy as np
import scipy as sp
    
def A2G(a = None,b = None,eta_LOS = None,eta_NLOS = None,f = None,h_ms = None,Ptx = None,Prx = None): 
    #parameter A
    A = eta_LOS - eta_NLOS
    #parameter B
    B = - 147.55 + 20 * np.log10(f) + eta_NLOS
    #pathloss
    PL = Ptx - Prx
    #========calculate seta optm==============================================#
#==== dR/d(seta) =0====================#
# syms eqn_1 seta_A2G
# eqn_1=pi()*tan(pi()/180*seta_A2G)/(9*2.3)+ (a*b*A*exp(-b*(seta_A2G-a)))/...
#      (a*exp(-b*(seta_A2G-a))+1)^2;
#     #======optm elvation angle=============#
# Seta_A2G_opt=double(vpasolve(eqn_1,seta_A2G,[0 89]));
    
    ##function fun_7
    Seta_A2G_opt = sp.optimize.fsolve(fun_7(a,b,A),89)
    #=========================================================================#
#====calculate pathloss at seta-optm======================================#
    seta_A2G_C = Seta_A2G_opt
    #  syms   eqn_0 R
#     #===PL equation==========================#
#     eqn_0=-PL+(A/(a*exp(-b*(seta_A2G_C-a))+1))+...
#           20*log10(R/cos(pi()/180*seta_A2G_C))+B;
#     #======coverage Raduis===================#
#     R_A2G=double(vpasolve(eqn_0==0,R));
    
    ##function fun_8
    R_A2G = sp.optimize.fsolve(fun_8(PL,A,a,b,seta_A2G_C,B),100)
    #======UAV height========================#
    h_UAV = R_A2G * np.tan(3.14 / 180 * seta_A2G_C) + h_ms
    #=========================================================================#
    return Seta_A2G_opt,R_A2G,h_UAV