import numpy as np
import mpl_toolkits.mplot3d.art3d as art3d
from PathLossTUAV2UAV_F import PathLossTUAV2UAV_F
from PathLossCell2UAV_F import PathLossCell2UAV_F
from plotRelay3D import plotRelay3D

# ============================TUAV2UAV Relay system==========================
#===================================inputs==================================
env=1
f=2*1000000000
hms=2
A2GTx=20
A2GRx=-100
hB=35
L_r=.3
Go=2.15
seta3db=67
A2ATx=20
A2ARx=-80
h_TUAV_max=150

#=======================================placement================================            
[R_A2G_1,h_UAV_1,h_TUAV,dist_TUAV_UAV]=PathLossTUAV2UAV_F(env,f,hms,A2GTx,A2GRx,hB,L_r,Go,seta3db,A2ATx,A2ARx,h_TUAV_max);
#(R_A2G_c,h_UAV_c,h_TUAV_c,b,dist_TUAV_UAV_c)
#=========================================output=============================
print('coverage raduis=%.2f \nheight of UAV=%.2f \nheight of TUAV=%.2f\ndistance between TUAV and UAV=%.2f'%(R_A2G_1,h_UAV_1, h_TUAV, dist_TUAV_UAV))
           
#==========================================plot===============================       
plotRelay3D(dist_TUAV_UAV,R_A2G_1,h_UAV_1,h_TUAV,'r')

            
#             text(ax,(dist_TUAV_UAV_c+R_A2G_c),0,0,[ ' \leftarrow R(UAV)T = ',app.UAV_R.Value],'color','r');
#             stem3(ax,dist_TUAV_UAV_c,0,h_UAV_c,'Color',[0 0 0]);
#             text(ax,dist_TUAV_UAV_c,0,h_UAV_c,['  \leftarrow h(UAVT) = ',app.UAV_h.Value],'color','[0 0 0]');
#             stem3(ax,0,0,h_TUAV_c,'Color',[0 0 1]);
#             text(ax,0,0,h_TUAV_c,['  \leftarrowh(TUAV) = ',app.TUAV_h.Value],'color','[0 0 1]');
#             hold(ax);
      # % hObject    handle to pushbutton2 (see GCBO)
      #       % eventdata  reserved - to be defined in a future version of MATLAB
      #       % handles    structure with handles and user data (see GUIDATA)
#====================================Cellular Relay system==================
#===========================================inputs===========================
env1=1
f=2*1000000000;
hms=2
A2GTx=20
A2GRx=-80
C2UTx=20
C2URx=-80
hBS=35
#=========================================placement============================           
[R_A2G_2,h_UAV_2,dist_C2U_C]=PathLossCell2UAV_F(env1,f,hms,A2GTx,A2GRx,C2UTx,C2URx,hBS)
#============================================output=========================
print('coverage raduis=%.2f \nheight of UAV=%.2f\ndistance between Cellular Bs and UAV=%.2f'%(R_A2G_2,h_UAV_2,dist_C2U_C))
#=========================================plot===============================
plotRelay3D(dist_C2U_C,R_A2G_2,h_UAV_2,hBS,'b')

      #                    %(R_A2G_c,h_UAV_c,h_TUAV_c,b,dist_TUAV_UAV_c)
      #       app.UAV_R1.Value=num2str(R_A2G);
      #       app.UAV_h1.Value=num2str(h_UAV);
      #       app.CELL_UAV_d.Value=num2str(dist_C2U_C);
      #       ax=app.axes1;
      #       hold(ax);
      #       view(ax,3);
            
      #       plotCircle3DAx1(ax,[dist_C2U_C 0 0],[0 0 0],R_A2G);
      #       grid(ax, 'on')
      #       set(ax, 'xcolor', 'r')
      #       set(ax, 'ycolor', 'b')
      #       set(ax, 'zcolor', 'k')
            
      #       text(ax,(dist_C2U_C+R_A2G),0,0,[ ' \leftarrow R_U_A_VC = ',app.UAV_R1.Value],'color','[.9 .6 .1');
      #       stem3(ax,dist_C2U_C,0,h_UAV,'Color',[1 0 1]);
      #       text(ax,dist_C2U_C,0,h_UAV,[' \leftarrowh_U_A_VC = ',app.UAV_h1.Value],'color','[1 0 1]');
      #       stem3(ax,0,0,hBS,'Color',[0 1 0]);
      #       text(ax,0,0,hBS,['  \leftarrowh_B_S = ',num2str(35)],'color','g');
      #       hold(ax);
