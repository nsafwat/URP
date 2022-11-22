import tkinter
from  tkinter import *
import numpy as np
import mpl_toolkits.mplot3d.art3d as art3d
from PathLossTUAV2UAV_F import PathLossTUAV2UAV_F
from PathLossCell2UAV_F import PathLossCell2UAV_F
from plotRelay3D import plotRelay3D
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
root= Tk()
root.title("placemnt of UAV relay system")


# toolbar = NavigationToolbar2Tk(canvas, root)
# toolbar.update()
# canvas.get_tk_widget().grid(row=1,column=10,columnspan=10)

app_title=Label(root,text="3D palcemnt of UAV as a Relay station",bg='orange')
TUAV_UAV=Label(root,text="TUAV2UAV placement",bg='yellow')
#========================================================================
Env=['Dense Urban','Urban','Sub Urban']
variable = StringVar(root)
variable.set(Env[0]) 

variable_1 = StringVar(root)
variable_1.set(Env[0])  
#========================================================================
def TUAV2UAV_Run():
   TUAV2UAV_coverage_Raduis_I.insert(0,"                       ")
   TUAV2UAV_UAV_height_I.insert(0,"                       ")
   TUAV2UAV_TUAV_height_I.insert(0,"                       ")
   TUAV2UAV_distance_TUAV_UAV_I.insert(0,"                       ")
#=======================inputs===========================================
   env= int(Env.index(variable.get()))
   f=float(TUAV2UAV_frequency_I.get())*1000000000
   hms=float(TUAV2UAV_mobile_station_height_I.get())
   A2GTx=float(TUAV2UAV_A2G_Tx_power_I.get())
   A2GRx=float(TUAV2UAV_A2G_Rx_power_I.get())
   hB=float(TUAV2UAV_Building_height_I.get())
   L_r=float(TUAV2UAV_Reflection_coefficient_I.get())
   Go=float(TUAV2UAV_Antenna_Gain_I.get())
   seta3db=float(TUAV2UAV_seta_3dB_I.get())
   A2ATx=float(TUAV2UAV_A2A_Tx_power_I.get())
   A2ARx=float(TUAV2UAV_A2A_Rx_power_I.get())
   h_TUAV_max=float(TUAV2UAV_TUAV_height_max_I.get())
#=======================================placement================================            
   [R_A2G_1,h_UAV_1,h_TUAV,dist_TUAV_UAV]=PathLossTUAV2UAV_F(env,f,hms,A2GTx,A2GRx,hB,L_r,Go,seta3db,A2ATx,A2ARx,h_TUAV_max);
    #(R_A2G_c,h_UAV_c,h_TUAV_c,b,dist_TUAV_UAV_c)
    #=========================================output=============================
   print('coverage raduis=%.2f \nheight of UAV=%.2f \nheight of TUAV=%.2f\ndistance between TUAV and UAV=%.2f'%(R_A2G_1,h_UAV_1, h_TUAV, dist_TUAV_UAV))
   TUAV2UAV_coverage_Raduis_I.insert(0,str(round(float(R_A2G_1),2))) 
   TUAV2UAV_UAV_height_I.insert(0,str(round(float(h_UAV_1),2)))
   TUAV2UAV_TUAV_height_I.insert(0,str(round(float(h_TUAV),2)))
   TUAV2UAV_distance_TUAV_UAV_I.insert(0,str(round(float(dist_TUAV_UAV),2)))
      #==========================================plot===============================       
   plt=plotRelay3D(dist_TUAV_UAV,R_A2G_1,h_UAV_1,h_TUAV,'r')
   plt.suptitle("TUAV-UAV Relay system")
   canvas = FigureCanvasTkAgg(plt, master=root)  # A tk.DrawingArea.
   canvas.draw()
   canvas.get_tk_widget().grid(row=0,column=20,rowspan=20)
   # toolbarFrame = Frame(master=root)
   # toolbarFrame.grid(row=18,column=20)
   # toolbar = NavigationToolbar2TkAgg(canvas1, toolbarFrame)
 
#====================================Cellular Relay system==================
def Cell2UAV_Run():
    Cell2UAV_coverage_Raduis_I.insert(0,"                       ")
    Cell2UAV_UAV_height_I.insert(0,"                       ")
    Cell2UAV_distance_Bs_UAV_I.insert(0,"                       ")
#=============================inputs=======================================    
    env1=int(Env.index(variable_1.get()))
    f=float(Cell2UAV_frequency_I.get())*1000000000;
    hms=float(Cell2UAV_mobile_station_height_I.get())
    A2GTx=float(Cell2UAV_A2G_Tx_power_I.get())
    A2GRx=float(Cell2UAV_A2G_Rx_power_I.get())
    C2UTx=float(Cell2UAV_A2A_Tx_power_I.get())
    C2URx=float(Cell2UAV_A2A_Rx_power_I.get())
    hBS=float(Cell2UAV_Bs_height_I.get())
    #=========================================placement============================           
    [R_A2G_2,h_UAV_2,dist_C2U_C]=PathLossCell2UAV_F(env1,f,hms,A2GTx,A2GRx,C2UTx,C2URx,hBS)
    #============================================output=========================
    print('coverage raduis=%.2f \nheight of UAV=%.2f\ndistance between Cellular Bs and UAV=%.2f'%(R_A2G_2,h_UAV_2,dist_C2U_C))
    Cell2UAV_coverage_Raduis_I.insert(0,str(round(float(R_A2G_2),2))) 
    Cell2UAV_UAV_height_I.insert(0,str(round(float(h_UAV_2),2)))
    Cell2UAV_distance_Bs_UAV_I.insert(0,str(round(float(dist_C2U_C),2)))
    #=========================================plot===============================
    plt2=plotRelay3D(dist_C2U_C,R_A2G_2,h_UAV_2,hBS,'b')
    plt2.suptitle("Cellular-UAV Relay system")
    canvas = FigureCanvasTkAgg(plt2, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=17,column=20,rowspan=40,columnspan=20)
#=========================================================================

#===============================GUI=======================================
#===============================inputs====================================
TUAV2UAV_Inputs=Label(root,text="Inputs",bg='green',fg="white")
TUAV2UAV_Run=Button(root,text="Run",bg="red",command=TUAV2UAV_Run)

#A2G parameters
TUAV2UAV_A2G_channel_parameters=Label(root,text="TUAV2UAV A2G channel parameters",bg='white')
TUAV2UAV_enviroment=Label(root,text="Enviroment")
TUAV2UAV_enviroment_I=OptionMenu(root,variable,*Env)



TUAV2UAV_frequency=Label(root,text="Frequency (GHz)")
TUAV2UAV_frequency_I=Entry(root,width=15,justify="center")
TUAV2UAV_frequency_I.insert(0,'2')

TUAV2UAV_mobile_station_height=Label(root,text="Mobile_station height(m)")
TUAV2UAV_mobile_station_height_I=Entry(root,width=15,justify="center")
TUAV2UAV_mobile_station_height_I.insert(0,'2')

TUAV2UAV_A2G_Tx_power=Label(root,text="A2G_Tx_power(dB)")
TUAV2UAV_A2G_Tx_power_I=Entry(root,width=15,justify="center")
TUAV2UAV_A2G_Tx_power_I.insert(0,'20')

TUAV2UAV_A2G_Rx_power=Label(root,text="A2G_Rx_power(dB)")
TUAV2UAV_A2G_Rx_power_I=Entry(root,width=15,justify="center")
TUAV2UAV_A2G_Rx_power_I.insert(0,'-80')

#TUAV2UAV parameters
TUAV2UAV_A2A_channel_parameters=Label(root,text="TUAV2UAV A2A channel parameters",bg='white')

TUAV2UAV_A2A_Tx_power=Label(root,text="A2A_Tx_power")
TUAV2UAV_A2A_Tx_power_I=Entry(root,width=15,justify="center")
TUAV2UAV_A2A_Tx_power_I.insert(0,'20')

TUAV2UAV_A2A_Rx_power=Label(root,text="A2A_Rx_power")
TUAV2UAV_A2A_Rx_power_I=Entry(root,width=15,justify="center")
TUAV2UAV_A2A_Rx_power_I.insert(0,'-80')

TUAV2UAV_TUAV_height_max=Label(root,text="TUAV height max (m)")
TUAV2UAV_TUAV_height_max_I=Entry(root,width=15,justify="center")
TUAV2UAV_TUAV_height_max_I.insert(0,"150")

TUAV2UAV_Building_height=Label(root,text="Building height (m)")
TUAV2UAV_Building_height_I=Entry(root,width=15,justify="center")
TUAV2UAV_Building_height_I.insert(0,"35")

TUAV2UAV_Reflection_coefficient=Label(root,text="Reflection coefficient")
TUAV2UAV_Reflection_coefficient_I=Entry(root,width=15,justify="center")
TUAV2UAV_Reflection_coefficient_I.insert(0,".3")

TUAV2UAV_Antenna_Gain=Label(root,text="Antenna Gain(Go) (dBi)")
TUAV2UAV_Antenna_Gain_I=Entry(root,width=15,justify="center")
TUAV2UAV_Antenna_Gain_I.insert(0,"2.15")

TUAV2UAV_seta_3dB=Label(root,text="seta 3dB (degree)")
TUAV2UAV_seta_3dB_I=Entry(root,width=15,justify="center")
TUAV2UAV_seta_3dB_I.insert(0,"67")

#TUAV2UAV output
TUAV2UAV_Outputs=Label(root,text="Outputs",bg='blue',fg="white")

TUAV2UAV_coverage_Raduis=Label(root,text="coverage Raduis (m)")
TUAV2UAV_coverage_Raduis_I=Entry(root,width=15,justify="center")

TUAV2UAV_UAV_height=Label(root,text="UAV height (m)")
TUAV2UAV_UAV_height_I=Entry(root,width=15,justify="center")

TUAV2UAV_TUAV_height=Label(root,text="TUAV height (m)")
TUAV2UAV_TUAV_height_I=Entry(root,width=15,justify="center")

TUAV2UAV_distance_TUAV_UAV=Label(root,text="distance between TUAV & UAV (m)")
TUAV2UAV_distance_TUAV_UAV_I=Entry(root,width=15,justify="center")


app_title.grid(row=0,column=0,columnspan=7)
TUAV_UAV.grid(row=1,column=0,columnspan=2)
TUAV2UAV_Inputs.grid(row=2,column=0,columnspan=1)
TUAV2UAV_Run.grid(row=2,column=1)
#A2G
TUAV2UAV_A2G_channel_parameters.grid(row=3,column=0,columnspan=2)

TUAV2UAV_enviroment.grid(row=4,column=0,columnspan=1)
TUAV2UAV_enviroment_I.grid(row=4,column=1,columnspan=1)

TUAV2UAV_frequency.grid(row=5,column=0,columnspan=1)
TUAV2UAV_frequency_I.grid(row=5,column=1,columnspan=1)

TUAV2UAV_mobile_station_height.grid(row=6,column=0,columnspan=1)
TUAV2UAV_mobile_station_height_I.grid(row=6,column=1,columnspan=1)

TUAV2UAV_A2G_Tx_power.grid(row=7,column=0,columnspan=1)
TUAV2UAV_A2G_Tx_power_I.grid(row=7,column=1,columnspan=1)

TUAV2UAV_A2G_Rx_power.grid(row=8,column=0,columnspan=1)
TUAV2UAV_A2G_Rx_power_I.grid(row=8,column=1,columnspan=1)

#A2A
TUAV2UAV_A2A_channel_parameters.grid(row=9,column=0,columnspan=2)


TUAV2UAV_A2A_Tx_power.grid(row=10,column=0,columnspan=1)
TUAV2UAV_A2A_Tx_power_I.grid(row=10,column=1,columnspan=1)

TUAV2UAV_A2A_Rx_power.grid(row=11,column=0,columnspan=1)
TUAV2UAV_A2A_Rx_power_I.grid(row=11,column=1,columnspan=1)

TUAV2UAV_TUAV_height_max.grid(row=12,column=0,columnspan=1)
TUAV2UAV_TUAV_height_max_I.grid(row=12,column=1,columnspan=1)

TUAV2UAV_Building_height.grid(row=13,column=0,columnspan=1)
TUAV2UAV_Building_height_I.grid(row=13,column=1,columnspan=1)

TUAV2UAV_Reflection_coefficient.grid(row=14,column=0,columnspan=1)
TUAV2UAV_Reflection_coefficient_I.grid(row=14,column=1,columnspan=1)

TUAV2UAV_Antenna_Gain.grid(row=15,column=0,columnspan=1)
TUAV2UAV_Antenna_Gain_I.grid(row=15,column=1,columnspan=1)

TUAV2UAV_seta_3dB.grid(row=16,column=0,columnspan=1)
TUAV2UAV_seta_3dB_I.grid(row=16,column=1,columnspan=1)

#output
TUAV2UAV_Outputs.grid(row=17,column=0,columnspan=1)

TUAV2UAV_coverage_Raduis.grid(row=18,column=0,columnspan=1)
TUAV2UAV_coverage_Raduis_I.grid(row=18,column=1,columnspan=1)

TUAV2UAV_UAV_height.grid(row=19,column=0,columnspan=1)
TUAV2UAV_UAV_height_I.grid(row=19,column=1,columnspan=1)

TUAV2UAV_TUAV_height.grid(row=20,column=0,columnspan=1)
TUAV2UAV_TUAV_height_I.grid(row=20,column=1,columnspan=1)

TUAV2UAV_distance_TUAV_UAV.grid(row=21,column=0,columnspan=1)
TUAV2UAV_distance_TUAV_UAV_I.grid(row=21,column=1,columnspan=1,padx=10,pady=10)
#===================cell2UAV==========================

Cell2UAV=Label(root,text="Cell2UAV placement",bg='yellow')
Cell2UAV_Inputs=Label(root,text="Inputs",bg='green',fg="white")
Cell2UAV_Run=Button(root,text="Run",bg="red",command=Cell2UAV_Run)

#A2G parameters
Cell2UAV_A2G_channel_parameters=Label(root,text="Cell2UAV A2G channel parameters",bg='white')

Cell2UAV_enviroment=Label(root,text="Enviroment")
Cell2UAV_enviroment_I=OptionMenu(root,variable_1,*Env)

Cell2UAV_frequency=Label(root,text="Frequency (GHz)")
Cell2UAV_frequency_I=Entry(root,width=15,justify="center")
Cell2UAV_frequency_I.insert(0,"2")

Cell2UAV_mobile_station_height=Label(root,text="Mobile_station height(m)")
Cell2UAV_mobile_station_height_I=Entry(root,width=15,justify="center")
Cell2UAV_mobile_station_height_I.insert(0,'2')

Cell2UAV_A2G_Tx_power=Label(root,text="A2G_Tx_power(dB)")
Cell2UAV_A2G_Tx_power_I=Entry(root,width=15,justify="center")
Cell2UAV_A2G_Tx_power_I.insert(0,'20')

Cell2UAV_A2G_Rx_power=Label(root,text="A2G_Rx_power(dB)")
Cell2UAV_A2G_Rx_power_I=Entry(root,width=15,justify="center")
Cell2UAV_A2G_Rx_power_I.insert(0,'-80')

#Cell2UAV parameters
Cell2UAV_A2A_channel_parameters=Label(root,text="Cell2UAV A2A channel parameters",bg='white')

Cell2UAV_A2A_Tx_power=Label(root,text="A2A_Tx_power")
Cell2UAV_A2A_Tx_power_I=Entry(root,width=15,justify="center")
Cell2UAV_A2A_Tx_power_I.insert(0,'40')

Cell2UAV_A2A_Rx_power=Label(root,text="A2A_Rx_power")
Cell2UAV_A2A_Rx_power_I=Entry(root,width=15,justify="center")
Cell2UAV_A2A_Rx_power_I.insert(0,'-80')

Cell2UAV_Bs_height=Label(root,text="Cellular BS height  (m)")
Cell2UAV_Bs_height_I=Entry(root,width=15,justify="center")
Cell2UAV_Bs_height_I.insert(0,'35')


#Cell2UAV output
Cell2UAV_Outputs=Label(root,text="Outputs",bg='blue',fg="white")

Cell2UAV_coverage_Raduis=Label(root,text="coverage Raduis (m)")
Cell2UAV_coverage_Raduis_I=Entry(root,width=15,justify="center")

Cell2UAV_UAV_height=Label(root,text="UAV height (m)")
Cell2UAV_UAV_height_I=Entry(root,width=15,justify="center")

Cell2UAV_distance_Bs_UAV=Label(root,text="distance between Bs & UAV (m)")
Cell2UAV_distance_Bs_UAV_I=Entry(root,width=15,justify="center")


Cell2UAV.grid(row=1,column=4,columnspan=3)
Cell2UAV_Inputs.grid(row=2,column=4,columnspan=1)
Cell2UAV_Run.grid(row=2,column=5,columnspan=1)
#A2G
Cell2UAV_A2G_channel_parameters.grid(row=3,column=4,columnspan=2)

Cell2UAV_enviroment.grid(row=4,column=4,columnspan=1)
Cell2UAV_enviroment_I.grid(row=4,column=5,columnspan=1)

Cell2UAV_frequency.grid(row=5,column=4,columnspan=1)
Cell2UAV_frequency_I.grid(row=5,column=5,columnspan=1)

Cell2UAV_mobile_station_height.grid(row=6,column=4,columnspan=1)
Cell2UAV_mobile_station_height_I.grid(row=6,column=5,columnspan=1)

Cell2UAV_A2G_Tx_power.grid(row=7,column=4,columnspan=1)
Cell2UAV_A2G_Tx_power_I.grid(row=7,column=5,columnspan=1)

Cell2UAV_A2G_Rx_power.grid(row=8,column=4,columnspan=1)
Cell2UAV_A2G_Rx_power_I.grid(row=8,column=5,columnspan=1)

#A2A
Cell2UAV_A2A_channel_parameters.grid(row=9,column=4,columnspan=2)


Cell2UAV_A2A_Tx_power.grid(row=10,column=4,columnspan=1)
Cell2UAV_A2A_Tx_power_I.grid(row=10,column=5,columnspan=1)

Cell2UAV_A2A_Rx_power.grid(row=11,column=4,columnspan=1)
Cell2UAV_A2A_Rx_power_I.grid(row=11,column=5,columnspan=1)

Cell2UAV_Bs_height.grid(row=12,column=4,columnspan=1)
Cell2UAV_Bs_height_I.grid(row=12,column=5,columnspan=1)


#output
Cell2UAV_Outputs.grid(row=17,column=4,columnspan=1)

Cell2UAV_coverage_Raduis.grid(row=18,column=4,columnspan=1)
Cell2UAV_coverage_Raduis_I.grid(row=18,column=5,columnspan=1,padx=10)

Cell2UAV_UAV_height.grid(row=19,column=4,columnspan=1)
Cell2UAV_UAV_height_I.grid(row=19,column=5,columnspan=1)

Cell2UAV_distance_Bs_UAV.grid(row=21,column=4,columnspan=1)
Cell2UAV_distance_Bs_UAV_I.grid(row=21,column=5,columnspan=1)
root.mainloop()
