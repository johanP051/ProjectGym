import numpy as np
import pandas as pd
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from getpass import getpass
import time
import sys
import os

from edad import edad
from imc import imc
from pago import *


user = input("Inserte su usuario: ")
passwd = getpass("Inserte su contraseña: ")

while True:
  try:
    nTelefono = abs(int(input("Inserte su número de teléfono: ")))
  except ValueError:
    print("Inserte un numero válido")
    continue
  else:
    break

switch = {
    1: "IMC",
    2: "Edad",
    3: "Pago Gym"
    }

def switcher(argument):
    switch
    return switch.get(argument)

print(f"\nA continuación se muestran las opciones {switch}\n")
argument = int(input("Inserta la opcion que deseas: "))
argument = switcher(argument)

if argument == "IMC":
    imc()
    time.sleep(3)
elif argument == "Edad":
    age = edad()
    print(f"\n{user}, usted tiene {age.years} años con {age.months} meses y {age.days} días\n")
    time.sleep(2)
else:
    option = lista_pago()
    mipago = Inscripcion(option)
    mipago.pago()
    time.sleep(3)

request = input("\n¿Desea continuar con alguna otra función del programa? (IMC, Edad o Pago Gym) [S/n]: ")
request = request[0].capitalize()

if request == "S":
    os.system(f"python3 {__file__}")
else:
    sys.exit("\nHasta la próxima")
