
import numpy as np
from A2G import A2G
from abcal import abcal
from TUAV2UAV import TUAV2UAV
from delta_h import delta_h
import scipy as sp 
from fun_0 import fun_0
from fun_1 import fun_1
from fun_2 import fun_2
from fun_3 import fun_3
    
def PathLossTUAV2UAV_F(env = None,f = None,h_ms = None,A2G_Tx = None,A2G_Rx = None,h_B = None,L_r = None,Go = None,seta_3db = None,A2A_Tx = None,A2A_Rx = None,h_TUAV_max = None): 
    #=========================================================================#
    
    a_A2G_val = np.array([15,11,5])
    b_A2G_val = np.array([0.18,0.16,0.3])
    eta_LOS_val = np.array([1.6,1,0.1])
    eta_NLOS_val = np.array([23,20,21])
    # parameter a _Porbability of LOS
    a_A2A = 0
    a_A2G = a_A2G_val[env]
    # parameter b _Porbability of LOS
    b_A2A = 0
    b_A2G = b_A2G_val[env]
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
    #Building height
#h_B=60;
#antenna gain
#Go=1.7;
# reflection coefficient
#L_r=.6;
#TUAV2UAV Rx power
    Px = A2A_Tx
    #TUAV2UAV Tx power
    Pr = A2A_Rx
    #antena pattern 3db angle
#seta_3db=67;
#maximum TUAV height
#h_TUAV_max_v=100;
#=========================================================================#
#=========================================================================#
#Air to Ground PathLoss
#=========================================================================#
    Seta_A2G_opt,R_A2G,h_UAV = A2G(a_A2G,b_A2G,eta_LOS,eta_NLOS,f,h_ms,Ptx,Prx)
    #=========================================================================#
    
    if (h_UAV > h_B):
        a_A2A = 0
        b_A2A = 0
    else:
        a_A2A,b_A2A = abcal(env,h_TUAV_max,h_UAV)
    
    #=========================================================================#
#=========================================================================#
#TUAV to UAV PathLoss
#=========================================================================#
    seta_TUAV2UAV_otp,seta_TUAV2UAV_C,h_dlta_TUAV_UAV_MAX = TUAV2UAV(a_A2A,b_A2A,Go,seta_3db,L_r,h_TUAV_max,h_B,h_UAV,f,Px,Pr)
    #=========================================================================#
    
    #=========================================================================#
#=========================================================================#
#==============Recalculate delta_h========================================#
    h_dlta_TUAV_UAV,h_UAV_c,h_TUAV_c = delta_h(h_UAV,h_TUAV_max,h_B,h_dlta_TUAV_UAV_MAX)
    #=========================================================================#
#recalcualte distance between TUAV and UAV================================#
    PL = Px - Pr
    #=========================in case of LOS==================================#
    if (h_UAV > h_B):
        if (h_dlta_TUAV_UAV_MAX == 0):
            #         syms eqn_3  dist_TUAV_UAV
#         eqn_3=-PL-147.5+20*log10(f)+20*log10(dist_TUAV_UAV)-2*Go+...
#           +20*log10(1);
#        dist_TUAV_UAV_c=vpasolve(eqn_3==0,dist_TUAV_UAV);
            ##function fun_0
            dist_TUAV_UAV_c = sp.optimize.fsolve(fun_0(PL,f,Go),1000)
        else:
            #         syms eqn_3 seta_TUAV2UAV
#         eqn_3=-PL-147.5+20*log10(f)+20*log10(h_dlta_TUAV_UAV)-20*...
#                   log10(sin(pi()/180*seta_TUAV2UAV))-2*Go+...
#                   24*(seta_TUAV2UAV/seta_3db)^2+20*log10(1);
#         seta_TUAV2UAV_R=vpasolve(eqn_3==0,seta_TUAV2UAV,[90 0]);
            ##function fun_1
            seta_TUAV2UAV_R = sp.optimize.fsolve(fun_1(PL,f,h_dlta_TUAV_UAV,seta_3db,Go),1)
            dist_TUAV_UAV_c = h_dlta_TUAV_UAV / np.tan(3.14 / 180 * seta_TUAV2UAV_R)
            #           dist_TUAV_UAV_c=h_dlta_TUAV_UAV/tan(3.14/180*seta_TUAV2UAV_C);
        #====in case of NLOS=================================#
    else:
        #      if(h_dlta_TUAV_UAV_MAX>0 &&h_dlta_TUAV_UAV_MAX<1)
        if (h_dlta_TUAV_UAV_MAX == 0):
            #         eqn_3=-PL-147.5+20*log10(f)+20*log10(dist_TUAV_UAV)-2*Go+...
#           +24*(0/seta_3db)^2+....
#             20*log10((10^((-68.8+10*log10(f)+10*log10(h_B-h_UAV)+...
#             20*log10(cos(pi()*0/180))-...
#             10*log10(1+sqrt(2)/(L_r^2 )))/20)*...
#             (1-(1/(a_A2A*exp(-b_A2A*(0-a_A2A))+1))))+ ...
#             (1*(1/(a_A2A*exp(-b_A2A*(0-a_A2A))+1))));
#        dist_TUAV_UAV_c=vpasolve(eqn_3==0,dist_TUAV_UAV);
            ##function fun_2
            dist_TUAV_UAV_c = sp.optimize.fsolve(fun_2(PL,f,Go,h_B,h_UAV,L_r,a_A2A,b_A2A),1)
        else:
            #          syms eqn_3 seta_TUAV2UAV
#          eqn_3=-PL+(-147.5+20*log10(f)+20*log10(h_dlta_TUAV_UAV)-...
#             20*log10(sin(pi()/180*seta_TUAV2UAV)))-2*Go+...
#             24*(seta_TUAV2UAV/seta_3db)^2+....
#             20*log10((10^((-68.8+10*log10(f)+10*log10(h_B-h_UAV)+...
#             20*log10(cos(pi()*seta_TUAV2UAV/180))-...
#             10*log10(1+sqrt(2)/(L_r^2 )))/20)*...
#             (1-(1/(a_A2A*exp(-b_A2A*(seta_TUAV2UAV-a_A2A))+1))))+ ...
#             (1*(1/(a_A2A*exp(-b_A2A*(seta_TUAV2UAV-a_A2A))+1))));
#         seta_TUAV2UAV_R=double(vpasolve(eqn_3==0,seta_TUAV2UAV,[0 89]));
            ##function fun_3
#  opts = optimoptions('fsolve', 'TolFun',.0001, 'TolX', .00001,'StepTolerance',1);
            seta_TUAV2UAV_R = sp.optimize.fsolve(fun_3(PL,f,int(h_dlta_TUAV_UAV),Go,seta_3db,int(h_B),int(h_UAV),L_r,a_A2A,b_A2A),1)
            dist_TUAV_UAV_c = h_dlta_TUAV_UAV / np.tan(3.14 / 180 * seta_TUAV2UAV_R)
    
    #dist_TUAV_to_UAV = h_dlta_TUAV_UAV / np.tan(3.14 / 180 * seta_TUAV2UAV_C)
    #=========================================================================#
#==recalculate coverage radius============================================#
    R_A2G_c = (h_UAV_c - h_ms) / np.tan(3.14 / 180 * Seta_A2G_opt)
    #=========================================================================#
#==path loss recalculed value=============================================#
#parameter A
   # A = eta_LOS - eta_NLOS
    #parameter B
   # B = - 147.55 + 20 * np.log10(f) + eta_NLOS
    #PathLoss PL
    #PL_A2G = (A / (a_A2G * np.exp(- b_A2G * (Seta_A2G_opt - a_A2G)) + 1)) + 20 * np.log10(R_A2G_c / np.cos(3.14 / 180 * Seta_A2G_opt)) + B
    #=========================================================================#
    # dist_TUAV_UAV_c = float(dist_TUAV_UAV_c)
    # h_UAV_c = float(h_UAV_c)
    # R_A2G_c = float(R_A2G_c)
    # h_TUAV_c = float(h_TUAV_c)
    return R_A2G_c,h_UAV_c,h_TUAV_c,dist_TUAV_UAV_c
    
