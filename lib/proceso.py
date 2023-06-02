class Proceso:

    def __init__(self, operacion, prioridad):
        self.operacion = operacion
        self.prioridad = prioridad
    
    def __str__(self):
        return  "Proceso: " + str(self.operacion) + "\nPrioridad\t: " + str(self.prioridad) + "\n"