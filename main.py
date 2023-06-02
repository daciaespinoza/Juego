from lib.proceso import Proceso
from lib.lib import Lib
from lib.nodo import Nodo

lib = Lib()

lib.AGREGAR_PROCESO("Suma", 3)
lib.AGREGAR_PROCESO("Resta", 4)
lib.AGREGAR_PROCESO("Multiplicacion", 5)
lib.AGREGAR_PROCESO("Division", 2)

print(lib.LISTAR_PROCESOS())

print(lib.CONTAR_PROCESOS())
