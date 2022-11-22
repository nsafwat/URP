import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import mpl_toolkits.mplot3d.art3d as art3d
    
def plotRelay3D(center = None,radius = None ,h_UAV=None,Bs=None,clr=None): 
    # theta = np.arange(0,2 * np.pi+0.01,0.01)
    # v = null(normal)
    # points = np.matlib.repmat(np.transpose(center),1,theta.shape[2-1]) + radius * (v(:,1) * np.cos(theta) + v(:,2) * np.sin(theta))
    # plot3(Axes,points(1,:),points(2,:),points(3,:),'r-')
    


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Draw a circle on the x=0 'wall'
    p = plt.Circle((0,center),radius,color=clr,fill=False)
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=0, zdir="z")
    
    ax.stem([0],center,h_UAV,linefmt=clr, markerfmt='o'+clr)
    ax.stem([0],[0],[Bs],linefmt=clr, markerfmt='o'+clr)
    ax.text(0,center,h_UAV,'UAV height=%.2f'%h_UAV+'m')
    ax.text(0,0,Bs,'BS height=%.2f'%Bs+'m')

    ax.set_xlim(-radius, radius)
    ax.set_ylim(0, center+radius)
    ax.set_zlim(0, max(h_UAV,Bs))
    ax.set_xlabel('UAV covergae R(m)')
    ax.set_ylabel('UAV covergae R=%.2f'%center+'(m)')
    ax.set_zlabel('height (m)')
    plt.show()
    return fig
    