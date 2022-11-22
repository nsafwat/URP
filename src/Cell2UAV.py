import scipy as sp 
from fun_1_0 import fun_1_0 
from fun_1_1 import fun_1_1
def Cell2UAV(Px = None,Pr = None,f = None,gamma = None,A = None,B = None,seta_o = None,eta_o = None): 
    PL = Px - Pr
    # syms  eqn_2 seta_C2U
# eqn_2=A*exp(-(seta_C2U-seta_o)/B)*(1-(seta_C2U-seta_o)/B);
# seta_C2U_opt=vpasolve(eqn_2,seta_C2U);
##function fun_1_0
    seta_C2U_opt = sp.optimize.fsolve(fun_1_0(A,B,seta_o),0.1)
    seta_C2U_C = seta_C2U_opt
    #===============================================#
# syms eqn_1  dist_C2U
# eqn_1=-PL+10*gamma*log10(dist_C2U)-147.5+20*log10(f)+A*(seta_C2U_C-seta_o)*exp(-(seta_C2U_C-seta_o)/B)+eta_o;
# #eqn_1=-PL+10*gamma*log10(dist_C2U)+A*(seta_C2U_C-seta_o)*exp(-(seta_C2U_C-seta_o)/B)+eta_o;
    
    # dist_C2U_C=vpasolve(eqn_1==0,dist_C2U);
##function fun_1_1
    dist_C2U_C = sp.optimize.fsolve(fun_1_1(PL,gamma,f,seta_C2U_C,seta_o,A,B,eta_o),100)
    return seta_C2U_opt,dist_C2U_C