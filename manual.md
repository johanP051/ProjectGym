# Manual

Hay que tener en cuenta primero que menu.py importa el código de los archivos edad.py, imc.py y pago.py

Para empezar hay que tener en cuenta que en los módulos pago.py e imc.py usa la librería pandas para mostrar una tabla de datos organizada (DataFrame)

Una vez ejecutado el archivo principal menu.py:
Se le pide al usuario, su nombre de usuario, su contraseña y su numero de teléfono.

Para esto se define:

* La variable user y se pide un input (entrada del teclado)
* la variable passwd hace uso de la libreria getpass(la cual solicita un input pero no muestra la contraseña en pantalla por seguridad)
* La variable nTelefono (input) la cual esta dentro de un bucle while True que siempre se ejecutará hasta que el usuario digite un numero entero válido (try and except)

Se definen las opciones a elegir en un diccionario por parte del usuario:
* IMC, Edad y Pago Gym
* Se defina la funcion switcher(argument) (def : definicion de funcion) la cual toma un argumento del usuario que le indicará la ocion a elegir (switcher.get(argument))
* el valor que retorna la funcion (switcher) se guarda en una variable argument

A continuación se evaluan las posibles opciones que el usuario pudo haber escogido:

(Explicacion de los condicionales, if: Si *Condicion a evaluar*; elif: si no se cumple el if, entonces evalua otra condicion; else: sino, si ninguna condicion se cumple, hacer algo)
* if argument == "IMC": llama a la funcion importada al inicio del archivo y ejecuta todo su codigo (el cual basicamente pide al usuario altura y peso y en base a eso lo calcula, le da indicaciones por medio de condicionales: if, elif, else)
* elif argument == "Edad": guarda y ejecuta la funcion importada edad() en una variable age, como age es un objeto, despues en el print se muestra con formato los años, dias y meses vividos.
* else: se guarda y ejecuta la funcion importada lista_pago() en una variable option (lista_pago contiene la opcion (Diaremente o Mensualmente)), despues se instancia la clase importada Incripcion que recibe como atributo la opcion elegida y de acuedo a ello ejecuta su codigo (que basicamente de acuerdo a la opcion calcula el monto a pagar)

time.sleep añade un intervalo de espera para que el codigo no se ejecute tan rapido


al final por medio de un input se le pregunta al usuario si quiere continuar con la ejecucion del programa:

* Si es es S, entonces se ejecuta otra vez por os.system(python3 __file__)
* Si es n entonces hace un sys.exit() y despide al usuario.
