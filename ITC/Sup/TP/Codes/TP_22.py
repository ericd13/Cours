# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.integrate import odeint
# from mpl_toolkits.mplot3d import Axes3D
# 
# def Euler(phi, y0, T):
#     n = len(T)
#     Y = [0]*n
#     Y[0] = y0
#     for k in range(n-1):
#         Y[k+1] = Y[k] + (T[k+1] - T[k])*phi(Y[k], T[k])
#     return Y
# 
# alpha = 1
# beta  = 2
# gamma = 0.001
# delta = 0.001

# # Proies-prédateurs
# 
# def phi(u, t):
#     p, q = u
#     vp = alpha*p - gamma*p*q
#     vq = -beta*q + delta*p*q
#     return np.array([vp, vq])
# 
# T = np.linspace(0, 20, 10000)
# 
# p0 = 6000
# q0 = 1000
# u0 = np.array([p0, q0])
# U = Euler(phi, u0, T)
# P = [u[0] for u in U]
# Q = [u[1] for u in U]
# plt.subplot(1, 2, 1)
# plt.plot(T, P)
# plt.plot(T, Q)
# plt.subplot(1, 2, 2)
# plt.plot(P, Q)
# plt.show()
# 
# for p0 in [2200, 2500, 3000, 4000, 6000, 10000]:
#     u0 = np.array([p0, q0])
#     U = odeint(phi, u0, T)
#     P = [u[0] for u in U]
#     Q = [u[1] for u in U]
#     plt.plot(P, Q)
# plt.show()
# 
# # SIR
# R0 = 3
# gamma = 0.2
# beta = R0*gamma
# 
# def phi(u, t):
#     s, i, r = u
#     return np.array([-beta*s*i, beta*s*i - gamma*i, gamma*i])
# 
# i0 = 1e-3
# CI = np.array([1-i0, i0, 0])
# 
# t_max = 100
# T = np.linspace(0, t_max, 10000)
# U = odeint(phi, CI, T)
# plt.plot(T,U)
# plt.show()
# 
# def phi(u, t):
#     if 10 < t < 40:
#         beta1 = beta/2
#     else:
#         beta1 = beta
#     s, i, r = u
#     return np.array([-beta1*s*i, beta1*s*i - gamma*i, gamma*i])
# 
# i0 = 1e-3
# CI = np.array([1-i0, i0, 0])
# t_max = 100
# T = np.linspace(0, t_max, 10000)
# U = odeint(phi, CI, T)
# plt.plot(T,U)
# plt.show()
# 
# Lorenz
# def lorenz(u, t):
#     sigma = 10
#     rho = 28
#     beta = 8/3
#     x, y, z = u
#     vx = sigma*(y - x)
#     vy = rho*x - y - x*z
#     vz = x*y - beta*z
#     return np.array([vx, vy, vz])
# 
# T = np.linspace(0, 30, 10000)
# y0 = np.array([0.1, 0.0, 0.1])
# U = odeint(lorenz, y0, T)
# X = [u[0] for u in U]
# Y = [u[1] for u in U]
# Z = [u[2] for u in U]
# 
# fig = plt.figure()
# mon_dessin = Axes3D(fig)
# # mon_dessin = Axes3D(fig, auto_add_to_figure = False)
# # fig.add_axes(mon_dessin)
# 
# 
# mon_dessin.plot(X, Y, Z) 
# plt.show()

# # Erreurs
# def phi(u, t):
#     y, v = u
#     a = 2*y
#     return np.array([v, a])
# 
# T = np.linspace(0, 30, 10000)
# u0 = np.array([1, -2**0.5])
# U = odeint(phi, u0, T)
# Y = [u[0] for u in U]
# plt.plot(T, Y)
# plt.ylim([-10, 2])
# plt.show()
# 
# # pendule asymétrique
# R = 0.05  #m
# l = 0.5   #m
# m = 0.1   #kg
# g = 9.81  #m.s^{-2}
# 
# 
# N = 10000
# tmin = 0
# tmax = 5
# 
# CI = np.array([0, 0])
# T = np.linspace(tmin, tmax, N)
# liste_M = [0.65,  0.70, 0.72, 0.73]
# for M in liste_M:
#     def phi(u, t):
#         y, v = u
#         a = (M*g*R - m*g*l*np.sin(y)) / (m*l**2 + M*R**2)
#         return np.array([v, a])
#     U = odeint(phi, CI, T)
#     Y = [u[0] for u in U]
#     plt.plot(T, Y, label = "Position pour M={}".format(M))
# plt.ylim([-5, 15])
# plt.legend()
# plt.show()
# 
# tmax = 2.5
# CI = np.array([0, 0])
# T = np.linspace(tmin, tmax, N)
# liste_M = [0.65, 0.72, 0.74]
# liste_M = [0.65, 0.70, 0.72, 0.73]
# for M in liste_M:
#     U = odeint(phi, CI, T)
#     Y = [u[0] for u in U]
#     V = [u[1] for u in U]
#     plt.plot(Y, V, label = "Portrait de phase pour M={}".format(M))
# 
# plt.legend()
# plt.show()
# 
# # Van der Pol
# epsilon = 1
# omega0 = 1
# 
# def phi(u, t):
#     y, v = u
#     a = epsilon*omega0*(1-y**2)*v -omega0**2*y
#     return np.array([v, a])
# 
# T = np.linspace(0, 20, 10000)
# for y0 in [1, 3, 5]:
#     for v0 in [-3, 0, 3]:
#         u0 = np.array([y0, v0])
#         U = odeint(phi, u0, T)
#         Y = [u[0] for u in U]
#         V = [u[1] for u in U]
#         plt.plot(Y, V)
# plt.show()

# # Zeeman
# 
# m = 9.1e-31    #kg, masse de l'électron
# e = 1.6e-19    #C, charge de l'électron
# w0 = 4.34e15   #rad/s pulsation propre du rappel du noyau
# B = 1000       #T, intensité du champ magnétique
# w = (e*B)/(2*m)
# a = 5.3e-11    #m
# 
# def zeeman(u, t):
#     x, y, vx, vy = u
#     ax = -2*w*vy-w0**2*x
#     ay = 2*w*vx-w0**2*y
#     return np.array([vx, vy, ax, ay])
# 
# t_max = 5e-14
# T = np.linspace(0, t_max, 10000)
# 
# r0x = 0
# r0y = 0
# v0x = a*w0
# v0y = 0
# CI = np.array([r0x, r0y, v0x, v0y])
# 
# 
# U = odeint(zeeman, CI, T)
# X = [u[0] for u in U]
# Y = [u[1] for u in U]
# VX = [u[2] for u in U]
# VY = [u[3] for u in U]
# 
# plt.plot(T, X, label = "$x(t)$")
# plt.plot(T, Y, label = "$y(t)$")
# #plt.title("Tracés de $x(t)$ et de $y(t)$")
# plt.legend()
# plt.show()
# 
# plt.plot(X, VX)
# #plt.title("Portrait de phase de $x(t)$")
# plt.show()
# 
# # Van Halen
# 
# q0 = 1.6e-19  # C, charge du proton
# m0 = 1.67e-27 # kg, masse du proton
# mu0 = 1.0e-7 # mu_0/4*pi
# RT = 6.4e6    # m, rayon de la terre
# c = 3.0e8     # m/s**2, vitesse de la lumière
# mu = np.array([0.0, 0.0, 7.7e22]) # moment magnétique terrestre
# 
# def B(M): # champ magnétique en M
#     r = np.dot(M, M)**0.5 
#     u = (1/r)*M
#     return mu0*(3*np.dot(mu,u)*u -mu)/(r**3)
# 
# def phi(u, t):
#     M = u[0:3]
#     V = u[3:6]
#     derivee = np.zeros(6)
#     derivee[0:3] = V
#     derivee[3:6] = q0*np.cross(V, B(M))/m0
#     return derivee
# 
# T = np.linspace(0, 5, 10000)
# d = 2*RT
# u0 = np.array([0, 2*RT, 0, 0, 0.25*c, 0.1*c])
# 
# U= odeint(phi, u0, T)
# X = U[ : , 0]
# Y = U[ : , 1]
# Z = U[ : , 2]
# 
# fig=plt.figure()
# ax=Axes3D(fig, auto_add_to_figure = False)
# fig.add_axes(ax)
# ax.plot(X, Y, Z)
# 
# r = np.linspace(0, RT, 30)
# phi = np.linspace(0, 2*np.pi, 20)
# R, Phi = np.meshgrid(r, phi)
# X1 = R*np.cos(Phi)
# Y1 = R*np.sin(Phi)
# Z1 = (RT**2 - R**2)**0.5
# ax.plot_wireframe(X1, Y1, Z1, color = "gray")
# ax.plot_wireframe(X1, Y1, -Z1, color = "gray")
# plt.show()

def abs(x):
    if x :
        return 1
    else:
        return -1