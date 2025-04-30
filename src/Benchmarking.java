import java.util.Random;

public class Benchmarking {

    private MetodosOrdenamiento metodosOrdenamiento;
    
    public Benchmarking(){

        long currentMills=System.currentTimeMillis(); //Sacar la fecha, milisegundos desde 1970
        long currentNano=System.nanoTime();
        

        System.out.println(currentMills);
        System.out.println(currentNano);

        metodosOrdenamiento=new MetodosOrdenamiento();
        int[] arreglo=generarArregloAleatorio(1000000);
        Runnable tarea=()-> metodosOrdenamiento.burbujaTradicional(arreglo);

        double tiempoDuracionMills=medirConCurrentTimeMiles(tarea);
        double tiempoDuracionNano=medirConNanoTime(tarea);

        System.out.println("Tiempo en milisegundos: "+tiempoDuracionMills);
        System.out.println("Tiempo en Nanosegundos: "+tiempoDuracionNano);
    }

    private int[] generarArregloAleatorio(int tamano){
        int[] numeros=new int[tamano];
        Random random=new Random();
        for(int i=0;i<tamano;i++){
            numeros[i]=random.nextInt(1000);
        }
        return numeros;
    }

    public double medirConCurrentTimeMiles(Runnable tarea){
        long inicio= System.currentTimeMillis();
        tarea.run();
        long fin=System.currentTimeMillis();
        double tiempoSegundos=(fin-inicio)/1000.0;
        return tiempoSegundos;
    }

    public double medirConNanoTime(Runnable tarea){
        long inicio= System.nanoTime();
        tarea.run();
        long fin=System.nanoTime();
        double tiempoNanoSegundos=(fin-inicio)/1_000_000_000.0;
        return tiempoNanoSegundos;
    }
}
