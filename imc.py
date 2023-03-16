import numpy as np
import pandas as pd
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from getpass import getpass
import time
import sys

#Haciendo un bucle para que si el usuario indica unidades, vuelva a ingresar los datos bien
def imc():
    while True:
      try:
        peso = abs(float(input("\nIngrese su peso en Kilogramos: ")))
        estatura = abs(float(input("\nIngrese su estatura en metros: ")))

      except ValueError:
        print("Inserte únicamente el número, no indique unidades")
        continue

      else:
        break

    IMC = peso / estatura**2

    print("\nA continuación se muestra la tabla del IMC")

    data = {
        "Clasificación del IMC": ["Delgadez muy severa", "Delgadez severa", "Delgadez", "Peso saludable", "Sobrepeso", "Obesidad moderada", "Obesidad severa", "Obesidad muy severa"],
        "Valor en intervalo": ["[0, 15)", "[15, 16)", "[16, 18.5)", "[18.5, 25)", "[25, 30)", "[30, 35)", "[35, 40)", "Mayor o igual a 40"] 
    }

    df = pd.DataFrame(data)


    print(f"\n{df}\n")

    print(f"\nSu índice de masa corporal es: {IMC} Kg/m^2")

    if IMC < 15:
        print("\nNo está dentro de los límites recomendados. Usted tiene Delgadez muy severa")
    elif IMC >=15 and IMC < 16:
        print("\nNo está dentro de los límites recomendados. Usted tiene Delgadez severa")
    elif IMC >=16 and IMC < 18.5:
        print("\nNo está dentro de los límites recomendados. Usted tiene Delgadez")
    elif IMC >= 18.5 and IMC < 25:
        print("\nEstá dentro de los límites recomendados. Usted tiene un peso saludable!!")
    elif IMC >= 25 and IMC < 30:
        print("\nNo está dentro de los límites recomendados. Usted tiene sobrepeso")
    elif IMC >= 30 and IMC < 35:
        print("\nNo está dentro de los límites recomendados. Usted tiene obesidad moderada")
    elif IMC >= 35 and IMC < 40:
        print("\n¡¡No está dentro de los límites recomendados. Usted tiene obesidad severa")
    else:
        print("\nNo está dentro de los límites recomendados. Usted tiene obesidad muy severa")