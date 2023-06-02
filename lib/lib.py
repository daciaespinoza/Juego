from lib.nodo import Nodo
from lib.proceso import Proceso

class Lib:

    def __init__(self):
        self.raiz = Nodo(Proceso("raiz_nodo", 3))
        self.contador = 1

    def AGREGAR_PROCESO(self, operacion, prioridad):

        proceso = Proceso(operacion, prioridad)

        self.raiz = self.__agregar(self.raiz, proceso)


    def __agregar(self, raiz, proceso):

        if proceso.prioridad not in range(0,6):
            print("fuera del rango")
            return raiz

        if raiz == None:
            raiz = Nodo(proceso)
            self.contador += 1
        else:

            if proceso.prioridad < self.raiz.dato.prioridad:
                 raiz.izq = self.__agregar(raiz.izq, proceso)
            else:
                raiz.der = self.__agregar(raiz.der, proceso)  
        return raiz
    
    def LISTAR_PROCESOS(self):
        return self.__pre_orden(self.raiz)
    
    def __pre_orden(self, raiz):

        if raiz != None:

            print(raiz.dato.__str__())

            self.__pre_orden(raiz.izq)
            self.__pre_orden(raiz.der)

    def CONTAR_PROCESOS(self):
        
        return self.contador
        