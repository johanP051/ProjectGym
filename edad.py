import numpy as np
import pandas as pd
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from getpass import getpass
import time
import sys


#Obteniendo la fecha de hoy
def edad():
  now = date.today()

  while True:
    try:
      fechaNacimiento = input("\nInserte su fecha de nacimiento siguiendo el formato DD/MM/AAAA: ")
      fechaNacimiento = datetime.strptime(fechaNacimiento, "%d/%m/%Y")

    except ValueError:
       print("Inserte bien su fecha")
       continue
    else:
      break
  
  #Calculando la edad restando las fechas
  age = relativedelta(now, fechaNacimiento)
  return age

