# Manual

Hay que tener en cuenta primero que menu.py importa el código de los archivos ```edad.py```, ```imc.py``` y ```pago.py```

![image](https://user-images.githubusercontent.com/64292875/227674665-18cdd1ae-1331-4f52-9030-7f8b15519d7a.png)

Para empezar hay que tener en cuenta que en los módulos **pago.py** e **imc.py** usa la librería **pandas** para mostrar una tabla de datos organizada (DataFrame)



Una vez ejecutado el archivo principal **menu.py**:
Se le pide al usuario, su nombre de usuario, su contraseña y su numero de teléfono.

Para esto se define:

* La variable **user** y se pide un input (entrada del teclado)
* la variable **passwd** hace uso de la libreria getpass(la cual solicita un input pero no muestra la contraseña en pantalla por seguridad)

#### Codigo:
![image](https://user-images.githubusercontent.com/64292875/227673113-de358b3e-0fe4-404a-9112-90f958bf31aa.png)

#### Ejecución:
![image](https://user-images.githubusercontent.com/64292875/227672371-9990008a-1b91-4429-809c-a913d8189cb8.png)


* La variable nTelefono (**input**) la cual esta dentro de un bucle ```while True``` que siempre se ejecutará hasta que el usuario digite un numero entero válido (```try``` and ```except```)

#### Codigo:
![image](https://user-images.githubusercontent.com/64292875/227674638-b301f0e2-d7b4-47ad-8c18-9f678eeb1aa7.png)

#### Ejecución:
![image](https://user-images.githubusercontent.com/64292875/227672602-ac154440-4e98-440c-9138-323ff64fc200.png)


Se definen las opciones a elegir en un diccionario (switch) por parte del usuario, con sus claves y respectivos valores:
* 1: IMC, 2: Edad y 2: Pago Gym
* Se define la funcion switcher(argument) (def : definicion de funcion) la cual toma un argumento del usuario que le indicará la ocion a elegir (switch.get(argument))
* el valor que retorna la funcion (switcher) se guarda en una variable argument

#### Codigo:
![image](https://user-images.githubusercontent.com/64292875/227675383-9746a052-499d-4207-abcc-c50990acd29e.png)

#### Ejecución:
![image](https://user-images.githubusercontent.com/64292875/227675446-79201681-e8f0-434e-b185-94ca132e8e1c.png)

A continuación se evaluan las posibles opciones que el usuario pudo haber escogido:

(Explicacion de los condicionales, **if**: Si *Condicion a evaluar*; **elif**: si no se cumple el if, entonces evalua otra condicion; **else**: sino, si ninguna condicion se cumple, hacer algo)

* if argument == "IMC": llama a la funcion importada al inicio del archivo y ejecuta todo su codigo (el cual basicamente pide al usuario altura y peso y en base a eso lo calcula, le da indicaciones sobre su salud corporal por medio de intervalos definidos en el archivo ```imc.py``` con condicionales: if, elif, else)

#### Código
![image](https://user-images.githubusercontent.com/64292875/227676742-94009be9-3d6f-4961-885a-95201d8648bd.png)

#### Ejecución:
![image](https://user-images.githubusercontent.com/64292875/227677614-da54dfca-54eb-466c-9238-1187c958e25c.png)


* elif argument == "Edad": guarda y ejecuta la funcion importada ```edad()``` en una variable age, como age es un objeto, despues en el print se muestra con formato sus atributos que son los años (age.years), dias (age.days) y meses vividos (age.months). (La edad se calcula con la libreria relativedelta a partir del formato de fecha que toma del input)

#### Código
![image](https://user-images.githubusercontent.com/64292875/227678238-86dba4f7-662f-47a4-be96-f41623603e54.png)

#### Ejecución
![image](https://user-images.githubusercontent.com/64292875/227678278-1de06ccb-8c44-4d10-901b-7fd26103d050.png)


* else (no se cumplieron las condiciones anteriores): se guarda y ejecuta la funcion importada ```lista_pago()``` en una variable option (lista_pago contiene la opcion (Diariamente o Mensualmente)), despues se instancia la clase importada **Incripcion** que recibe como atributo la opcion elegida y de acuerdo a ello ejecuta su codigo (que basicamente dependiendo si escoge diariamente o mensualmente, calcula el monto a pagar)

#### Código:
![image](https://user-images.githubusercontent.com/64292875/227678931-8ddcd606-ed44-464c-bc8d-e78465321ce9.png)


#### Ejecución:
![image](https://user-images.githubusercontent.com/64292875/227678435-d857e00e-3dc4-401e-b225-00c3db78090b.png)


```time.sleep()``` añade un intervalo de espera para que el codigo no se ejecute tan rapido


Al final por medio de un input se le pregunta al usuario si quiere continuar con la ejecucion del programa:

* Si es es S, entonces se ejecuta otra vez por ```os.system(python3 __file__)```
* Si es n entonces hace un ```sys.exit()``` y despide al usuario.

#### Código:
![image](https://user-images.githubusercontent.com/64292875/227679087-e1d19cfb-81f2-4579-a479-a3994266c9c6.png)

#### Ejecución:
![image](https://user-images.githubusercontent.com/64292875/227679111-b6da7b36-88ad-4fdf-a841-58b1b1118047.png)


Realizado por: Johan Posada and Julián Colorado
