import benchmarking as bm
import metodos_ordenamiento as mo
import benchmarking as bm
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
        