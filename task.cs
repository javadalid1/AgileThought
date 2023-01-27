using System;
using System.Collections.Generic;

class CambioOptimo
{

	// Variables necesarias para la función del cambio
	static int contador = 0;
	// Creación de diccionario (cambio)
	static Dictionary<string, int> cambio = new Dictionary<string, int>();

    static void cambioMinimo(double[]dinero, double pago, double costo)
    {
        // Comparación con truncado de decimales
		if (Math.Round(pago, 5) == costo){
		    imprimeCambio();
            Environment.Exit(0);
		}
		// Evaluación de casos base para evitar errores
        if (pago <= 0 && contador == 0){
			throw new InvalidOperationException("La cantidad ingresada no puede ser menor o igual a 0");
		}
		else if (pago < costo && contador == 0){
			throw new InvalidOperationException("La cantidad pagada no alcanza a cubrir el costo total");
		}
		for (int i = 0; i < dinero.Length; i++){
			if (dinero[i] <= Math.Round(pago - costo, 5)){
				contador ++;
				if(Math.Round(pago,5) != costo){
					try{
						cambio[dinero[i].ToString()] = cambio[dinero[i].ToString()] += 1;
					}
					catch (KeyNotFoundException){
						cambio.Add(dinero[i].ToString(), 1);
					}
					cambioMinimo(dinero, Math.Round(pago - dinero[i], 5), costo);
				}
			}
		}
    }

	// Método Main
	public static void Main()
    {
		// Definición de monedas o billetes
        double []dinero = {100,50,20,10,5,3,1};
		//Entrada de datos por teclado y conversión a double
		Console.WriteLine("Introduzca el costo total: ");
      	double costo;
      	costo=Convert.ToDouble(Console.ReadLine());
		Console.WriteLine("Introduzca el pago: ");
        double pago;
		pago=Convert.ToDouble(Console.ReadLine());
		cambioMinimo(dinero,pago,costo);
    }

	// Función para imprimir el diccionario del cambio
	static void imprimeCambio(){
        foreach (KeyValuePair<string, int> par in cambio) {
            Console.WriteLine("Monedas/Billetes de: " + par.Key + " Requerimos: " + par.Value);
        }
    }
}