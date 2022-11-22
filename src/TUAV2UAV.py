import scipy as sp 
from fun_4 import fun_4 
from fun_5 import fun_5
from fun_6 import fun_6
from fun_6_1 import fun_6_1   
def TUAV2UAV(a = None,b = None,Go = None,seta_3db = None,L_r = None,h_TUAV_max = None,h_B = None,h_UAV = None,f = None,Px = None,Pr = None): 
    #=========================================================================#
    PL = Px - Pr
    # syms eqn_4  seta_TUAV2UAV
#==calculate opt elevation angle==========================================#
#==in case of LOS=========================================================#
    if (h_UAV > h_B):
        seta_TUAV2UAV_otp = 0
    else:
        #==in case of NLOS=========================================================#
# eqn_4=-PL+(-147.5+20*log10(f)-20*log10(cos(pi()/180*seta_TUAV2UAV)))-2*Go+....
#         24*(seta_TUAV2UAV/seta_3db)^2+....
#         20*log10((10^((-68.8+10*log10(f)+10*log10(h_B-h_UAV)+...
#         20*log10(cos(pi()*seta_TUAV2UAV/180))-...
#         10*log10(1+sqrt(2)/(L_r^2 )))/20)*...
#         (1-(1/(a*exp(-b*(seta_TUAV2UAV-a))+1))))+ ...
#         (1*(1/(a*exp(-b*(seta_TUAV2UAV-a))+1))));
#  x=diff(eqn_4, seta_TUAV2UAV);
# seta_TUAV2UAV_otp=vpasolve(x==0,seta_TUAV2UAV,[90 0]);
        ##function fun_4
        seta_TUAV2UAV_otp = sp.optimize.fsolve(fun_4(f,seta_3db,h_B,h_UAV,L_r,a,b),1)
    
    #=========================================================================#
    seta_TUAV2UAV_C = seta_TUAV2UAV_otp
    #==============in case of LOS=============================================#
#=in case TUAV heigher than building and  UAV heigher than TUAV max height#
    
    if (h_UAV > h_B):
        if (h_TUAV_max < h_UAV):
            #============calculate angle for max delta_h================#
#             syms eqn_6 seta_h
#             eqn_6=(48*seta_h/seta_3db^2)-(3.14/tan(pi()/180*seta_h)/(9*2.3));
#             seta_h_max=vpasolve(eqn_6==0,seta_h,[0 89]);
            ##function fun_5
            seta_h_max = sp.optimize.fsolve(fun_5(seta_3db),1)
            seta_TUAV2UAV_C = seta_h_max
            #=============calculate max delta_h==========================#
#=============PL equation===================================#
#             syms eqn_3 h_dlta
#            eqn_3=-PL-147.5+20*log10(f)+20*log10(h_dlta)-20*...
#                   log10(sin(pi()/180*seta_TUAV2UAV_C))-2*Go+...
#                   24*(seta_TUAV2UAV_C/seta_3db)^2+20*log10(1);
#            h_dlta_TUAV_UAV_MAX=vpasolve(eqn_3==0,h_dlta);
            ##function fun_6
            h_dlta_TUAV_UAV_MAX = sp.optimize.fsolve(fun_6(PL,f,seta_TUAV2UAV_C,Go,seta_3db),100)
        else:
            #in case TUAV hgher than blding and UAV lower or equal than TUAV max hght#
#=============PL equation===================================#
#eqn_3=-PL-147.5+20*log10(f)+20*log10(dist_UAV_UAV)-2*Go+...
#       +20*log10(1);
#============calculate angle for max delta_h================#
            seta_TUAV2UAV_C = seta_TUAV2UAV_otp
            #=============calculate max delta_h==========================#
            h_dlta_TUAV_UAV_MAX = 0
    else:
        #================== in case of NLOS=======================================#
        if (seta_TUAV2UAV_otp == 0):
            seta_TUAV2UAV_C = seta_TUAV2UAV_otp
            #=============calculate max delta_h==========================#
            h_dlta_TUAV_UAV_MAX = 0
        else:
            #==========================================================#
#        syms eqn_3 h_dlta
#        eqn_3=-PL+(-147.5+20*log10(f)+20*log10(h_dlta)-...
#             20*log10(sin(pi()/180*seta_TUAV2UAV_C)))-2*Go+...
#             24*(seta_TUAV2UAV_C/seta_3db)^2+....
#             20*log10((10^((-68.8+10*log10(f)+10*log10(h_B-h_UAV)+...
#             20*log10(cos(pi()*seta_TUAV2UAV_C/180))-...
#             10*log10(1+sqrt(2)/(L_r^2 )))/20)*...
#             (1-(1/(a*exp(-b*(seta_TUAV2UAV_C-a))+1))))+ ...
#             (1*(1/(a*exp(-b*(seta_TUAV2UAV_C-a))+1))));
            #        #=============calculate max delta_h==========================#
#         h_dlta_TUAV_UAV_MAX=double(vpasolve(eqn_3==0,h_dlta));
#         display(h_dlta_TUAV_UAV_MAX)
#==========================================================#
            # #function fun_6_1
            h_dlta_TUAV_UAV_MAX = (sp.optimize.fsolve(fun_6_1(PL,f,seta_TUAV2UAV_C,Go,seta_3db,h_B,h_UAV,L_r,a,b),100))
    
    return seta_TUAV2UAV_otp,seta_TUAV2UAV_C,h_dlta_TUAV_UAV_MAX