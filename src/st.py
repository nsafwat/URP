import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import mpl_toolkits.mplot3d.art3d as art3d
from PathLossTUAV2UAV_F import PathLossTUAV2UAV_F
from PathLossCell2UAV_F import PathLossCell2UAV_F
from plotRelay3D import plotRelay3D



selected = option_menu(None, ["TUAV To UAV system", "Cellular to UAV system"], 
        icons=['gear', 'gear'], 
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "20px", "text-align": "left", "margin":"5px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "red"},
        }
    )
# ============================TUAV2UAV Relay system==========================
#===================================inputs==================================
col_1,col_2=st.columns([10,.1])
cont1=st.container 
cont2=st.container
if selected=="TUAV To UAV system":
    with cont1():
        side=st.sidebar 
        with side:
            st.markdown('<h1 style="color:blue;font-size:300%;">Inputs</h1>',unsafe_allow_html=True)
            
            sel=st.selectbox('Environment type',('Sub Urban','Urban','Dense Urban'))
            if sel=='Sub Urban':
                env=2
            elif sel=='Urban':
                env=1
            else:
                env=0
                
            f=st.number_input('frequency in GHz',min_value=0.1, max_value=5.8,value=5.0)*1000000000
           
            st.markdown('<h2 style="color:green;font-size:100%;">A2G Paramters</h2>',unsafe_allow_html=True)
            hms=st.number_input('mobile station height in meters',min_value=1.5, max_value=3.0,value=2.0)
            A2GTx=st.number_input('A2G Tx power in dbm',min_value=20.0, max_value=100.0,value=20.0)
            A2GRx=st.number_input('A2G Rx power in dbm',min_value=-200.0, max_value=-80.0,value=-80.0)
            
            st.markdown('<h2 style="color:green;font-size:100%;">A2A Paramters</h2>',unsafe_allow_html=True)

            hB=st.number_input('Building height in meters',min_value=10.0, max_value=150.0,value=35.0)
            L_r=st.number_input('Reflection coefficient',min_value=0.0, max_value=1.0,value=0.3)
            Go=st.number_input('Antenna gain',min_value=0.0, max_value=10.0,value=2.15)
            seta3db=st.number_input('3dB Bandwidth in degree',min_value=0.0, max_value=90.0,value=67.0)
            A2ATx=st.number_input('A2A Tx powerin dbm',min_value=20.0, max_value=100.0,value=20.0)
            A2ARx=st.number_input('A2A Rx power in dbm',min_value=-200.0, max_value=-80.0,value=-80.0)
            h_TUAV_max=st.number_input('TUAV maximum height in meters',min_value=100.0, max_value=200.0,value=150.0)
            
        #=======================================placement================================            
            [R_A2G_1,h_UAV_1,h_TUAV,dist_TUAV_UAV]=PathLossTUAV2UAV_F(env,f,hms,A2GTx,A2GRx,hB,L_r,Go,seta3db,A2ATx,A2ARx,h_TUAV_max);
        #=========================================output=============================
        
                   
        #==========================================plot===============================       
            with col_1:
              st.markdown('<h1 style="color:red;">Outputs</h1>',unsafe_allow_html=True)
              st.markdown('---')
              st.write('**coverage raduis= %.2f m**'%(R_A2G_1))            
              st.write('**height of UAV=%.2f m**'%(h_UAV_1))     
              st.write('**TUAV height=%.2f m**'%(h_TUAV))
              st.write('**Distance between TUAV and UAV=%.2f m**'%(dist_TUAV_UAV))            
              st.markdown('---')
            with col_1:
              plt_1=plotRelay3D(dist_TUAV_UAV,R_A2G_1,h_UAV_1,h_TUAV,'r')
              plt_1.savefig('TU2U2G.png',dpi=300)
              st.write(plt_1)
                
            
else:
    with cont2():
        #====================================Cellular Relay system==================

        side1=st.sidebar  
        with side1:
         
            st.markdown('<h1 style="color:blue;font-size:300%;">Inputs</h1>',unsafe_allow_html=True)
            
            sel1=st.selectbox('Environment type',('Sub Urban','Urban','Dense Urban'))
            if sel1=='Sub Urban':
                env1=2
            elif sel1=='Urban':
                env1=1
            else:
                env1=0
                
            f1=st.number_input('frequency in GHz',min_value=0.1, max_value=5.8,value=5.0)*1000000000
            hms1=st.number_input('mobile station height in meters',min_value=1.5, max_value=3.0,value=2.0)
            
            st.markdown('<h2 style="color:green;font-size:100%;">A2G Paramters</h2>',unsafe_allow_html=True)

            A2GTx1=st.number_input('A2G Tx power in dbm',min_value=20.0, max_value=100.0,value=20.0)
            A2GRx1=st.number_input('A2G Rx power in dbm',min_value=-200.0, max_value=-80.0,value=-80.0)
           
            st.markdown('<h2 style="color:green;font-size:100%;">A2A Paramters</h2>',unsafe_allow_html=True)

            C2UTx=st.number_input('A2A Tx powerin dbm',min_value=20.0, max_value=100.0,value=40.0)
            C2URx=st.number_input('A2A Rx power in dbm',min_value=-200.0, max_value=-80.0,value=-80.0)
            hBS=st.number_input('Base station  in meters',min_value=10.0, max_value=200.0,value=35.0)
            
        #=======================================placement================================            
            [R_A2G_2,h_UAV_2,dist_C2U_C]=PathLossCell2UAV_F(env1,f1,hms1,A2GTx1,A2GRx1,C2UTx,C2URx,hBS)
        #=========================================output=============================
        
                   
        #==========================================plot===============================       
            with col_1:
              st.markdown('<h1 style="color:red;">Outputs</h1>',unsafe_allow_html=True)
              st.markdown('---')
              st.write('**coverage raduis=%.2f m**'%(R_A2G_2))            
              st.write('**height of UAV=%.2f m**'%(h_UAV_2))            
              st.write('**Distance between BS and UAV=%.2f m**'%(dist_C2U_C))            
              st.markdown('---')
            with col_1:
                
               plt_1=plotRelay3D(dist_C2U_C,R_A2G_2,h_UAV_2,hBS,'b')
               plt_1.savefig('TU2U2G.png',dpi=300)
               st.write(plt_1)
