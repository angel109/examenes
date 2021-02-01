#Importar las librerias
import matplotlib.pyplot as plt
import numpy as np


plt.axis([0, 80, 0, 80])

plt.axis('on')
plt.grid(True)





xc=40
yc=40
r=5

P1=0*np.pi/180
p2=360*np.pi/180
dp=(p2-P1)/100

xlast=xc+r*np.cos(P1)
ylast=yc+r*np.sin(P1)

for p in np.arange(P1,p2+dp,dp):
    x=xc+r*np.cos(p)
    y=yc+r*np.sin(p)
    plt.plot([xlast,x],[ylast,y],color='purple',linewidth=2)
    xlast=x
    ylast=y

# Dibujamos el primer rectangulo
Ax = 40
Ay = 40
Bx = 30
By = 40
Cx = 30
Cy = 30
Dx = 40
Dy = 30

xp = [Ax, Bx, Cx, Dx, Ax]
yp = [Ay, By,  Cy, Dy, Ay]
plt.plot(xp, yp, color='g')

# Dibujamos circulo
Ax = 45
Ay = 45
Bx = 35
By = 45
Cx = 35
Cy = 35
Dx = 45
Dy = 35

xp = [Ax, Bx, Cx, Dx, Ax]
yp = [Ay, By,  Cy, Dy, Ay]
plt.plot(xp, yp, color='k')

    
plt.show()