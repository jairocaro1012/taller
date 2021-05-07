'''
*Universidad Sergio Arboleda
*Autores: Jairo Antonio Caro Vanegas
Fecha:Mayo 2021
Computación Paralela y Distribuida
Correo:jairo.caro01@correo.usa.edu.co
'''
from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize('Cy_functionE.pyx'))

setup(ext_modules=exts)