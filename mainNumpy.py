
# Programación Númerica y No Númerica DCN-501

# Jorge Polo
# C.I: V-18.587.447

# Gustavo Hernández
# C.I: V-28.317.635

# Jose Ojeda
# C.I: V-29.845.213

# Leonardo Yanez
# C.I: V-30.300.275
import matplotlib.pyplot as pp
import os
from numpy import linspace as lnsp


# funciones
def MuestraTitulo ():
    if os.name == "ce" or os.name == "nt" or os.name == "dos":
        var = "cls"       
    else:
        var = "clear"
    os.system(var)
    tittle = "___________                                  .__               \n\r\_   _____/_ __  ____             __________ |  |___  __ ____  \n\r |    __)|  |  \/    \   ______  /  ___/  _ \|  |\  \/ // __ \ \n\r |     \ |  |  /   |  \ /_____/  \___ (  <_> )  |_\   /\  ___/ \n\r \___  / |____/|___|  /         /____  >____/|____/\_/  \___  >\n\r     \/             \/               \/                     \/ \n\r"
    print(tittle)

def quadraticFunction(a,b,c):
    vertice = -(b)/(2*a)
    #print (vertice)
    verticeY= a*(vertice**2) + b * vertice + c
    print('ingrese el numero de puntos pos y neg a graficar a partir del vertice o presione enter para graficar 10')
    deltapos = input("tenga en cuenta que se grafica muy pocos puntos la grafica se vera mal >>> ")
    if deltapos == "":
        deltapos = 10
    else:
        deltapos = int(deltapos)
    MuestraTitulo ()
    print(f"el vertice de su funcion se encuentra en: ({vertice}, {verticeY})")
    input('Enter para ver la lista de pares y la grafica')
    MuestraTitulo ()


    poslim = int(vertice + deltapos)
    #print(poslim)
    neglim = int(vertice - deltapos)
    #print(neglim)


    x = list(range(neglim,poslim +1))
    y = list (map(lambda x : a*(x**2) + b * x + c, x))
    tabla = list(zip(x,y))
    for index, tupla in enumerate (tabla):
        alpha, epsilon = tupla
        print(f"{index+1}: X={alpha} Y={epsilon}")

    x = lnsp(neglim,poslim,100)
    def Fx(v):
        return a*(v**2) + b * v + c
    pp.plot(x, Fx(x))
    pp.xlabel("eje X")
    pp.ylabel('eje Y')
    pp.title("funcion cuadratica")
    pp.grid()
    print('cerrar grafica para terminar')
    pp.show()
    input('pulse enter para continuar')

def linearFunction(dependiente = 1, independiente = 0):
    x = list(range (-2, 3, 1))
    y = list (map(lambda x : (x* dependiente + independiente), x))
    tabla =  list(zip(x,y))
    MuestraTitulo()
    print('\nValores de coordenadas')
    for index, tupla in enumerate (tabla):
        a, b = tupla 
        print(f"{index+1}: X= {a} Y= {b}")
    
    pp.plot(x, y)
    pp.xlabel("eje X")
    pp.ylabel('eje Y')
    pp.title("funcion lineal")
    pp.grid()
    print('cerrar grafica para terminar')
    pp.show()
    input('pulse enter para continuar')

def MuestraMenu():
    menu = f"1: salir \n\r2: funcion lineal\n\r3: funcion cuadratica"
    print(menu)


# main

while (True):
    MuestraTitulo()
    MuestraMenu()

    option = input("==>  ")
    


    if option == '1':
        MuestraTitulo ()
        break
    elif option == '2':
        
        try:
            MuestraTitulo()
            a = int(input('favor de ingresar la variable dependiente:  '))
            b = int(input('favor de ingresar la variable independiente:  '))
            linearFunction(a, b)
        except:
            print('Sintax Err')
            input('enter para continuar')
    elif option == '3':
        try:
            MuestraTitulo()
            a = int(input('ingrese el termino a: '))
            b = int(input('ingrese el termino b: '))
            c = int(input('ingrese el termino c: '))
            MuestraTitulo ()
            quadraticFunction(a,b,c)
        except:
            print('Sintax Err')
            input('enter para continuar')
    else:
        print('Error')
        input('enter para continuar')