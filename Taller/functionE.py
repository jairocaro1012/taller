'''
*Universidad Sergio Arboleda
*Autores: Jairo Antonio Caro Vanegas
Fecha:Mayo 2021
Computación Paralela y Distribuida
Correo:jairo.caro01@correo.usa.edu.co
'''
from math import exp
import numpy as np

def rbf_network(X, beta, theta):

    N = X.shape[0]
    D = X.shape[1]
    Y = np.zeros(N)

    for i in range(N):
        for j in range(N):
            r = 0
            for d in range(D):
                r += (X[j, d] - X[i, d]) ** 2
            r = r**0.5
            Y[i] += beta[j] * exp(-(r * theta)**2)

    return Y