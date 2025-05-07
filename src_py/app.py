import benchmarking as bm
import metodos_ordenamiento as mo
import benchmarking as bm
import matplotlib.pyplot as plt
from datetime import datetime
# Archivo principal o main
if __name__=="__main__":
    print("Hola Mundo")
    brench=bm.Benchmarking()
    metodos=mo.MetodosOrdenamiento()

    #tam=10000
    tamanios=[5000, 10000, 10500]
    resultados=[]

    for tam in tamanios:
        arreglo_base=brench.build_arreglo(tam)

        metodos_dic={
            "Burbuja": metodos.burbuja,
            "Burbuja Mejorado": metodos.sort_burbuja_mejorado_optimizado,
            "Seleccion": metodos.sort_Seleccion,
            "Insercion": metodos.sort_Insercion,
            "Shell": metodos.sort_Shell,
        }
        for nombre, metodo in metodos_dic.items():
            #print(f"Ejecutando {nombre}...")
            tiempo_resultado = brench.medir_tiempo(metodo, arreglo_base)
            tupla_resultado = (tam,nombre, tiempo_resultado)
            resultados.append(tupla_resultado)

    for tam,nombre,tiempo in resultados:
        print(f"Tamano: {tam}, Metodo: {nombre}, Tiempo: {tiempo:.6f} segundos")

    #Prepara datos para ser graficos
    #1 Crear un diccionario o map para almacenar los resultados por metodos
    tiempos_by_metodo = {
        "Burbuja": [],
        "Burbuja Mejorado": [],
        "Seleccion": [],
        "Insercion": [],
        "Shell": [],
    }
    for tam,nombre,tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)

    plt.figure(figsize=(10, 6))

    #Graficar los tiempos de ejecucion para cada metodo
    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label=nombre, marker='o')

    #Agregar parametros\
    plt.title("JOEY DIAZ 06/05/2025 20:43:03")
    plt.suptitle('Tiempos de Ejecucion de Metodos de Ordenamiento')
    plt.xlabel('Tamanio del Arreglo')
    plt.ylabel('Tiempo (segundos)')

    plt.legend()

    plt.show()