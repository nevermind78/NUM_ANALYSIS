# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 00:40:36 2015

@author: never
"""
from pylab import *
from scipy.integrate import quad #c'est une bibliothèque pour qu'on peut calculer l'integrale
import numpy as np #abréviation du bibliothèque numpy pour être facile à utiliser
class Rectangle(object): #class rectange 
    def __init__(self, a, b, n, f):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
    def integrate(self,f):
        x=self.x# contiens les xi
        y=f(x)#les yi 
        h = float(x[1] - x[0])
        s = sum(y[0:-1])
        return h * s
    def Graph(self,f,resolution=1001):
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace(self.a, self.b, resolution)
        for i in range(self.n):
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] # abscisses des sommets
            y_rect = [0   , yl[i], yl[i]  , 0     , 0   ] # ordonnees des sommets
            plot(x_rect, y_rect,"g")
        yflist_fine = f(xlist_fine)
        plt.plot(xlist_fine, yflist_fine)
        plt.plot(xl, yl,"rd")
  
        plt.ylabel('f(x)')
        plt.title('Rectangle')
      #  text(0.5*(self.a+self.b), f(self.b), '$I_{%s}$ =%12.4f' % (self.n,self.integrate(f)), fontsize=15)
        
class Milieu(object): #class rectange 
    def __init__(self, a, b, n, f):#initialiser les paramètres du classe
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
    def integrate(self,f):
        x=self.x# contiens les xi
        h = float(x[1] - x[0])
        s=0
        for i in range(self.n):
            s=s+f((x[i]+x[i+1])*0.5)
        return h*s
       
    def Graph(self,f,resolution=1001):
        xl = self.x
        yl=f(xl);
        xlist_fine=np.linspace(self.a, self.b, resolution)
        
        for i in range(self.n):
            
            m=(xl[i]+xl[i+1])/2
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] # abscisses des sommets
            y_rect = [0   , f(m), f(m)  , 0     , 0   ] # ordonnees des sommets
            plot(x_rect, y_rect,"b")
            yflist_fine = f(xlist_fine)
            plt.plot(xlist_fine, yflist_fine)
            plt.plot(m,f(m),"y*")
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title('Milieu')
          #  text(0.5*(self.a+self.b), f(self.b), '$I_{%s}$ =%12.4f' % (self.n,self.integrate(f)), fontsize=15)        

class Trapezoidal(object):
    def __init__(self, a, b, n, f):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
    def integrate(self,f):
        x=self.x
        y=f(x)
        h = float(x[1] - x[0])
        s = y[0] + y[-1] + 2.0*sum(y[1:-1])
        return h * s / 2.0
    def Graph(self,f,resolution=1001):
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace(self.a, self.b, resolution)
        for i in range(self.n):
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] # abscisses des sommets
            y_rect = [0   , yl[i], yl[i+1]  , 0     , 0   ] # ordonnees des sommets
            plot(x_rect, y_rect,"m")
        yflist_fine = f(xlist_fine)
        plt.plot(xlist_fine, yflist_fine)#plot de f(x)
        plt.plot(xl, yl,"cs")#point support
        plt.ylabel('f(x)')
        
        
      #  text(0.5*(self.a+self.b), 0.5, '$I_{%s}$ =%12.4f' % (self.n,self.integrate(f)), fontsize=15)
        
class Simpson(object):
    def __init__(self, a, b, n, f): #initialiser les paramètres du classe
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)#les pts supports
        self.f = f
        self.n = n #nombre de subdivision

    def integrate(self,f):#calculer la somme ((b-a)/6*n)*[f(a)+2*sum(xi)+4*sum(mi)+f(b)]
        x=self.x #les points supports xi #x(0)=a-->x(n)=b
        y=f(x) #yi variable local y(o)=f(xo)-->y(n)
        h = float(x[1] - x[0])#pas h=(b-a)/2*n
        n = len(x) - 1#nombre subdivision
        if n % 2 == 1:#si le reste de la division =1 impaire
            n -= 1#☺nombre de sub ywali paire
        s = y[0] + y[n] + 4.0 * sum(y[1:-1:2]) + 2.0 * sum(y[2:-2:2])
        #y[1:-1:2] min impaire loulla m0 lil 9bal likhrania 5ater 3anna deja y(n) par pas de 2== mi
        #calculer la somme
        #T(-1] dernier valeur dans le tableau)
        return h * s / 3.0
    def Graph(self,f,resolution=1001):#1000 points 1001 résolution juste pour dessiner f
        xl = self.x #pt support
        yl = f(x) #yi
        xlist_fine=np.linspace(self.a, self.b, resolution)
        # pour le graph de la fonction f #intervalle ab subdiviser en 1000 poitns
        for i in range(self.n):#range intervalle 0 à n
            xx=np.linspace(x[i], x[i+1], resolution)
            #pour chaque subdivisuion  on doit dessiner polynome dnc on doit aussi le subdiviser
            m=(xl[i]+xl[i+1])/2#pt milieu
            a=xl[i]#borne gauche
            b=xl[i+1]#borne droite
            l0 = (xx-m)/(a-m)*(xx-b)/(a-b)
            l1 = (xx-a)/(m-a)*(xx-b)/(m-b)
            l2 = (xx-a)/(b-a)*(xx-m)/(b-m)
            P = f(a)*l0 + f(m)*l1 + f(b)*l2#fonction dde polynome
            plot(xx,P,'m')#dessiner polynome d'interpolation
        yflist_fine = f(xlist_fine)#fontion f
        plt.plot(xlist_fine, yflist_fine,'g')
        plt.plot(xl, yl,'wp')#point support en bleu rond
        
        plt.ylabel('f(x)')
        plt.title('Simpson')
     #   text(0.2*(self.a+self.b), 0.25*f(self.b), '$I_{%s} =\int_{a}^{b}f(x)dx$=%12.4f' % (self.n,self.integrate(f)), fontsize=15)   
        #pour une position bien determiner ++tiré bas indice In+++ int inetrgrale de a jusqu'a b
#########################################
#-------->>>>> classe point milieux    
######
if __name__ == '__main__':
        
    a = 0.0
    b = 0.5*pi
    n =4#le nombre de subdivision 
    x = np.linspace(a, b, n+1)
    def f(x):
        return sin(x)
    
    T = Trapezoidal(a, b, n, f)
    S = Simpson(a, b, n, f)
    R = Rectangle(a, b, n, f)
    M=Milieu(a,b,n,f)
    
    I,r =quad(f, a, b)#calcule d'integrale exacte
    
    print("Integral Exacte    = %12.4f" % (I) )
    print ("------------------------------------------")
    print ("Integral Trapèze   = %12.4f" % (T.integrate(f)))
    print ("Erreur Trapèze     = %12.4f" % (I-T.integrate(f)))#affichage d'erreur pour la méthode Trapèze
    print ("------------------------------------------")
    print ("Integral Simpson   = %12.4f" % (S.integrate(f)))
    print ("Erreur Simpson     = %12.4f" % (I-S.integrate(f)))
    print ("------------------------------------------")
    print ("Integral Rectangle = %12.4f" % (R.integrate(f)))
    print ("Erreur Rectangle   = %12.4f" % (I-R.integrate(f)))
    print ("------------------------------------------")
    print ("Integral Milieu    = %12.4f" % (M.integrate(f)))
    print ("Erreur Milieu      = %12.4f" % (I-M.integrate(f)))
    
    
   
    
    fig = plt.figure()
    ax = fig.add_subplot(221) 
    grid()#grid on
    T.Graph(f) 
    
    ax = fig.add_subplot(222)
    grid()
    S.Graph(f)
    
    ax = fig.add_subplot(223)
    grid()
    R.Graph(f)
    
    ax = fig.add_subplot(224)
    M.Graph(f)
    grid()
    ###M.Graph(f)
    
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
