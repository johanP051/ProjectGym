import numpy as np
import pandas as pd
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from getpass import getpass
import time
import sys


### Menú de opciones para incripción en el gimnasio

valorDiario = 5000
valorMensual = 120000

class Inscripcion:
    
    def __init__(self, tiempo):
        self.tiempo = tiempo

    def continuar(self):
        answer = input("¿Desea continuar con el pago? S/N: ")
        answer = answer[0].capitalize()

        if answer == "S":
            print("Okay, cancela en caja")
        else:
            sys.exit("Okay, Nos vemos pronto, Adiós.")

    def pago(self):
        print(f"\nPerfecto, vemos que ha escogido {self.tiempo}")
        
        if self.tiempo == "Diariamente":
            cantidad = int(input("\nInserte la cantidad de días que piensa pagar: "))
            print(f"\nEl valor total a pagar sería de {cantidad * valorDiario} COP por {cantidad} días")
            self.continuar()

        else:
            cantidad = int(input("\nInserte la cantidad de meses que piensa pagar: "))
            if cantidad == 3:
               descuento = (cantidad * valorMensual)*0.05
               print(f"\nEl valor total a pagar sería de {cantidad * valorMensual - descuento} COP por {cantidad} meses")
               self.continuar()
               
            elif cantidad == 6:
               descuento = (cantidad * valorMensual)*0.1
               print(f"\nEl valor total a pagar sería de {cantidad * valorMensual - descuento} COP por {cantidad} meses")
               self.continuar()
            elif cantidad == 12:
               descuento = (cantidad * valorMensual)*0.3
               print(f"\nEl valor total a pagar sería de {cantidad * valorMensual - descuento} COP por {cantidad} meses")
               self.continuar()

            else:
               print(f"\nEl valor total a pagar sería de {cantidad * valorMensual} COP por {cantidad} meses")
               self.continuar()

def lista_pago():
    dataPago = {
        "Pago": ["Diariamente", "Mensualmente"],
        "Valor (COP)": [valorDiario, valorMensual]
    }
                
    df2 = pd.DataFrame(dataPago, index=[1, 2])
    df2.index.name = "Numero de opción"
    print(f"\nA continuación se muestran las opciones para pagar el gimnasio: \n\n{df2}\n")
    print("Recuerde que si escoge 6 meses, obtendrá un descuento del 10%")
    print("Si escoge 3 meses, obtendrá un descuento del 5%")
    print("Si escoge 1 año tendrá un descuento del 30%\n")

    while True:
        try: 
            option = int(input("Inserte el número de la opción que desea escoger: "))
        except ValueError:
            print("Inserte un valor entero")
            continue
        if option not in range(1, 3):
            print("Debe escoger la opción 1 o 2")
            continue
        else:
            break

    option = df2.loc[df2.index[option-1], "Pago"]
    return option           

#option = lista_pago()
    