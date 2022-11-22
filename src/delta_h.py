import numpy as np
    
def delta_h(h_UAV = None,h_TUAV_max = None,h_B = None,h_dlta_TUAV_UAV_MAX = None): 
    if (h_dlta_TUAV_UAV_MAX >= np.abs(h_UAV - h_TUAV_max)):
        h_dlta_TUAV_UAV = int(np.abs(h_UAV - h_TUAV_max))
        h_TUAV_c = h_TUAV_max
        h_UAV_c = h_UAV
    else:
        h_dlta_TUAV_UAV = int(h_dlta_TUAV_UAV_MAX)
        #====================incase of LOS=======================================#
        if (h_UAV > h_B):
            if (h_dlta_TUAV_UAV_MAX == 0):
                h_TUAV_c = h_UAV
                h_UAV_c = h_UAV
            else:
                h_UAV_c = h_TUAV_max + h_dlta_TUAV_UAV_MAX
                h_TUAV_c = h_TUAV_max
            #====================incase of LOS=======================================#
        else:
            h_TUAV_c = h_UAV + h_dlta_TUAV_UAV
            h_UAV_c = h_UAV
    
    #=====hUAV heigher than h_TUAV_max=============#
    return h_dlta_TUAV_UAV,h_UAV_c,h_TUAV_c
    
    #  if(h_UAV>h_B)
#     #===hUAV lower than or equal h_TUAV_max==========#
#     if(h_dlta_TUAV_UAV_MAX==0)
#             h_TUAV_c=h_UAV;
#             h_UAV_c=h_UAV;
#           h_dlta_TUAV_UAV=  h_dlta_TUAV_UAV_MAX;
#     elseif (h_dlta_TUAV_UAV_MAX<abs(h_UAV-h_TUAV_max))
    
    #         #=====hUAV heigher than h_TUAV_max=============#
#         h_dlta_TUAV_UAV=h_dlta_TUAV_UAV_MAX ;
#         h_UAV_c=h_TUAV_max+h_dlta_TUAV_UAV_MAX;
#         h_TUAV_c=h_TUAV_max;
#      else
#          h_dlta_TUAV_UAV=abs(h_UAV-h_TUAV_max);
#          h_TUAV_c=h_TUAV_max;
#          h_UAV_c=h_UAV;
#      end
# else
# #====in case of NLOS======================================================#
#      if(h_dlta_TUAV_UAV_MAX<abs(h_UAV-h_TUAV_max))
#          h_dlta_TUAV_UAV=h_dlta_TUAV_UAV_MAX;
#          h_TUAV_c=h_UAV+h_dlta_TUAV_UAV;
#          h_UAV_c=h_UAV;
#      else
#          h_dlta_TUAV_UAV=abs(h_UAV-h_TUAV_max);
#          h_TUAV_c=h_TUAV_max;
#          h_UAV_c=h_UAV;
#      end
#  end
    return h_dlta_TUAV_UAV,h_UAV_c,h_TUAV_c