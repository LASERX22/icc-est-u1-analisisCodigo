import metodos_ordenamiento as mo
import random
import time
class Benchmarking:

    #public
    def __init__(self):
        self.mO=mo.MetodosOrdenamiento
        print("Benchmarking instanciado")

    def medir_tiempo(self,metodo, arreglo):
        inicio=time.perf_counter()
        metodo(arreglo)
        fin=time.perf_counter()
        return fin-inicio

        # arreglo=self.build_arreglo(50000)
        # # tarea=()->
        # tarea=lambda: self.mO.burbuja(self, arreglo)
        # #mili=self.contar_con_current_time_milles(tarea)
        # #print(mili)
        # nano=self.contar_con_nano_time(tarea)
        # print(nano)

        # tarea2=lambda:self.mO.sort_burbuja_mejorado_optimizado(self,arreglo)
        # nano2=self.contar_con_nano_time(tarea2)
        # print(nano2)
        # tarea3=lambda:self.mO.sort_Seleccion(self,arreglo)
        # nano3=self.contar_con_nano_time(tarea3)
        # print(nano3)

    def build_arreglo(self,tamano):
        arreglo=[]
        for i in range(tamano):
            numero=random.randint(0,999999)
            arreglo.append(numero)
        return arreglo

    #Import time
    #Milisegundos en segundos con # X=time.time()
    #Nanosegundos con #X=time.time_ns()
    #Ejecutar es tarea()
    def contar_con_current_time_milles(self,tarea):
        x=time.time()
        tarea()
        fin=time.time()
        tiempo_segundos=fin-x
        return f"Tiempo en milisegundos={tiempo_segundos}"


    def contar_con_nano_time(self,tarea):
        x=time.time_ns()
        tarea()
        fin=time.time_ns()
        tiempo_nano_segundos=(fin-x)/1_000_000_000.0
        return f"Tiempo en nanosegundos={tiempo_nano_segundos}"