# M2C4

1 ¿Cuál es la diferencia entre una lista y una tupla en Python?
	
La diferencia más importante está en que las listas son mutables, mientras que las tuplas son inmutables.
Esto significa que funciones como la de ordenar alfabéticamente, por ejemplo, darían un error en el caso de las tuplas.
Así nos aseguramos de que los elementos permanezcan como en el estado original (inmutable).
	
En cuanto a la representación, los elementos de la lista van entre corchetes [], y los de las tuplas van entre paréntesis ().

Las listas son estructuras de datos que pueden almacenar cualquier otro tipo de dato, inclusive una lista puede contener otra lista, además, la cantidad de elementos de una lista se puede modificar removiendo o añadiendo elementos. Para definir una lista se utilizan los corchetes, dentro de estos se colocan todos los elementos separados por comas.Las listas son iterables y por tanto se puede acceder a sus elementos mediante indexación. Se tiene la posibilidad de agregar elementos a una lista mediante el método append. El método remove elimina un elemento de una lista.

Las tuplas son secuencias de elementos similares a las listas, la diferencia principal es que las tuplas no pueden ser modificadas directamente, es decir, una tupla no dispone de los métodos como append o insert que modifican los elementos de una lista.
Para definir una tupla, los elementos se separan con comas y se encierran entre paréntesis. Las tuplas al ser iterables pueden accederse mediante la notación de corchetes e índice. Si intentamos modificar alguno de los elementos de la tupla Python nos devolverá un error.

2 ¿Cuál es el orden de las operaciones?
	
(PEMDAS = Please excuse my dear aunt Sally)
Paréntesis, exponencial, multiplicación, división, suma (addition) y resta (subtraction).
	
El orden de la multiplicación y división se pueden intercambiar entre sí porque no altera el resultado, y lo mismo sucedería con la suma y la resta. Es decir, si seguimos el orden: paréntesis, exponencial, división, multiplicación, resta y suma, obtenemos el mismo resultado. Por lo tanto, también podemos utilizar la "palabra" PEDMAS para recordar el orden de los operadores.


 
3 ¿Qué es un diccionario Python?

Es una variable que almacena datos relacionados con una clave. Como ocurre con un diccionario real, podemos asociar a cada clave un valor (significado), o varios. La sintaxis que se utiliza en este caso son llaves {}.

Ejemplo:

	capitales = {
		'España': 'Madrid',
		'Francia': 'París',
		'Italia': 'Roma',
	}

	apellidos = {
		'Ángel': ['Suárez', 'Martínez'],
		'Rubén': ['Pérez', 'Rodríguez'],
		'Sara': ['Ruiz', 'López'],
	}

Con los diccionarios podremos consultar cuál es el valor de una clave (ejemplo 1), cuáles son las claves que estamos utilizando (ejemplo 2), cuáles los valores que obtenemos (ejemplo 3), o ambos (ejemplo 4).

Ejemplo 1

	capital_1 = capitales['España']
	print(capital_1) >>> Madrid

Ejemplo 2

	print(capitales.keys()) >>> dict_keys(['España', 'Francia', 'Italia'])

Ejemplo 3

	print(capitales.values()) >>> dict_values(['Madrid', 'París', 'Roma'])

Ejemplo 4

	print(capitales.items()) >>> dict_items([('España','Madrid'), ('Francia', 'París'), ('Italia', 'Roma')])

Las claves deben ser objetos inmutables y los valores pueden ser de cualquier tipo. Necesariamente las claves deben ser únicas en cada diccionario, no así los valores.
Algunas propiedades de los diccionario en Python son las siguientes:

Son dinámicos, pueden crecer o decrecer, se pueden añadir o eliminar elementos.
Son indexados, los elementos del diccionario son accesibles a través del key.
Y son anidados, un diccionario puede contener a otro diccionario en su campo value.

4 ¿Cuál es la diferencia entre el método ordenado y la función de ordenación?

Con sort() se modifica directamente la lista, se ordena. Si intentamos almacenarlo en una nueva variable para no modificar la lista original, obtenemos un error (None).

Ejemplo:

	nombres = ['Ana', 'María', 'Elena']
	nombres.sort()
	
	print(nombres) >>> ['Ana', 'Elena', 'María']

Sin embargo con sorted(), sí podemos almacenarla en una nueva variable, y así no modificamos la lista original.

Ejemplo:

	nombres = ['Ana', 'María', 'Elena']
	nombres_ordenados = sorted(nombres)

	print(nombres) >>> ['Ana', 'María', 'Elena']
	print(nombres_ordenados) >>> ['Ana', 'Elena', 'María']

En ambos casos se sigue el criterio de orden alfabético, o de menor a mayor si se trata de números. Si queremos invertir este orden, habría que añadir reverse=True.

	nombres = ['Ana', 'María', 'Elena']
	nombres.sort(reverse=True)
	print(nombres) >>> ['María', 'Elena', 'Ana']

	nombres = ['Ana', 'María', 'Elena']
	nombres_ordenados = sorted(nombres, reverse=True)
	print(nombres_ordenados) >>> ['María', 'Elena', 'Ana']


En el caso de las tuplas, al ser éstas inmutables, sólo podemos utilizar sorted().




5 ¿Qué es un operador de reasignación?

Es un operador que permite reasignar a una variable existente, su valor inicial modificado por otro elemento.
	
Ejemplos:

	total += num_1   equivale a   total = total + num_1	Asigna un valor a una variable y luego le suma el valor a la derecha del igual.
	total -= num_1   equivale a   total = total - num_1	Asigna un valor a una variable y luego le resta el valor a la derecha del igual. 
	total *= num_1   equivale a   total = total * num_1	Asigna un valor a una variable y luego lo multiplica por el valor a la derecha del igual. 
	total /= num_1   equivale a   total = total / num_1	Asigna un valor a una variable y luego lo divide entre el valor a la derecha del igual. 

	lista_1 += ['Sara']      equivale a     lista_1 = lista_1 + ['Sara']
	tupla_1 += ('España',)   equivale a     tupla_1 = tupla_1 + ('España',)
