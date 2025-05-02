class MetodosOrdenamiento:
    def burbuja(self, array):
        arreglo=array.copy()
        n=len(arreglo)
        for i in range(n):
            for j in range(i+1,n):
                if arreglo[i]>arreglo[j]:
                    arreglo[i],arreglo[j]=arreglo[j],arreglo[i]
        return arreglo
    
    def sort_burbuja_mejorado_optimizado(self,array):
        arreglo=array.copy()
        n=len(arreglo)
        for i in range(n):
            for j in range(i+1,n-1-i):
                if arreglo[j]>arreglo[j+1]:
                    arreglo[j],arreglo[j+1]=arreglo[j+1],arreglo[j]
        return arreglo
    
    def sort_Seleccion(self,array):
        arreglo=array.copy()
        n=len(arreglo)
        for i in range(n-1):
            minimo=i
            for j in range(i+1,n):
                if arreglo[j] < arreglo[minimo]:
                    minimo=j
            bajo=arreglo[minimo]
            arreglo[minimo]=arreglo[i]
            bajo=arreglo[i]
        return arreglo
    
    def sort_Insercion(self,array):
        arreglo=array.copy()
        n=len(arreglo)
        for i in range(1,n):
            clave=arreglo[i]
            j=i-1
            while j>=0 and arreglo[j]>clave:
                arreglo[j+1]=arreglo[j]
                j-=1
            arreglo[j+1]=clave
        return arreglo
    
    def sort_Shell(self,array):
        arreglo=array.copy()
        n=len(arreglo)
        intervalo=n//2
        while intervalo>0:
            for i in range(intervalo,n):
                temp=arreglo[i]
                j=i
                while j>=intervalo and arreglo[j-intervalo]>temp:
                    arreglo[j]=arreglo[j-intervalo]
                    j-=intervalo
                arreglo[j]=temp
            intervalo//=2
        return arreglo
