### Bucle for
number = [1,2,3]
# Primero se escribe la variable donde ira guardando los resultados y despues el nombre de la lista
for num in number:
    print(num)

animals = ['dog', 'cat', 'snake', 'lion']
for animal in animals:
    print("*")
    print(f"A {animal.title()} would make a great pet. \n")

print('Any of these animals would make excellent pets.')


pizzas = ['barbecue', 'spicy', 'four cheese'] # Lista
for pizza in pizzas: # Bucle
    print(f"I love {pizza.title()} pizza") # Mensaje en cada iteracion

print("\n\tI love pizza!!!") # Mensaje fuera del bucle

### Bucles con numeros
# Utilizando la funcion range(primer_valor, ultimo_valor_no_incluido)
for value in range(1,11): # El numero 11 NO lo imprimira
    print(value) # Imprimira del 1 al 10

# Tambien se puede utilizar la funcion range(pasando_solo_el_numero_hasta_el_que_se_quiere_contar_mas_1)
for value in range(6):
    print(value)

### Usar range() para hacer una lista de numeros
numbers = list(range(1, 5)) # Con el metodo list() creamos una lista de numeros del 1 al 4
print(numbers)

### Lista con los numeros pares
even_numbers = list(range(2, 11, 2)) # El tercer valor en range() suma 2 hasta alcanzar o superar el valor final en este caso 11
print(even_numbers)

### Sacar los numeros cuadrados del 1 al 10
squares = [] # Creamos una lista vacia
for value in range(1, 11): # Recorremos los numeros del 1 al 10 utilizando un bucle for y el metodo range()
    square = value ** 2 # Creamos una variable donde vamos pasando los numeros y elevandolos a 2
    squares.append(square) # Con el metodo append() vamos añadiendo cada valor a la lista

print(squares) # Imprimimos la lista con todos los valores

### Sacar los numeros cuadrados del 1 al 10, forma mas corta
squares = [] # Creamos una lista vacia
for value in range(1, 11): # Recorremos los numeros del 1 al 10 utilizando un bucle for y el metodo range()
    squares.append(value ** 2) # Con el metodo append() vamos añadiendo cada valor elevado a la lista

print(squares) # Imprimimos la lista con todos los valores

### Estadistica sencilla con una lista de numeros
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits)) # Numero minimo utilizando el metodo min()
print(max(digits)) # Numero maximo utilizando el metodo max()
print(sum(digits)) # Suma de todos los numeros que contiene la lista utilizando el metodo sum()

### Listas por comprension
squares = [value ** 2 for value in range(1, 11)] # Crea la lista de numeros cuadrados pero utilizando una lista por comprension
print(squares)

### Contar hasta 20
for number in range(1, 21):
    print(number)

### Un millon
millon = [value for value in range(1, 1_000_001)]
print(sum(millon))
print(min(millon))
print(max(millon))

### Numeros impares
odds = [value for value in range(1, 21, 2)] # Creo una lista de numeros impares del 1 al 20 utilizando el tercer parametro del metodo range()
for odd in odds: # Recorro la lista
    print(odd) # Imprimo los numeros impares

### Treses
multiples = list(range(3,31,3))
for value in multiples:
    print(value)

### Compresion Cubos
cubes = [value ** 3 for value in range(1, 11)]
for cube in cubes:
    print(cube)

### Partir una lista ###
number_list = [1,2,3,4,5,6,7]
print(number_list[0:3]) # Muestra los 3 primeros elementos de la lista
print(number_list[2:5]) # Muestra  los elementos desde el 3 hasta el 5
print(number_list[:3]) # Si se omite el indice inicial, python comienza desde el principio de la lista
print(number_list[4:]) # Omitiendo el indice final, comenzara desde el indice inicial hasta el final
print(number_list[-2:]) # Devolvera los 2 ultimos elementos de la lista

players = ['Antonio', 'Chula', 'Arya', 'Patricia', 'Nala', 'Francisca']
print("Here are the first three players on my team:")
for player in players[:3]: # El bucle solo pasa por los 3 primeros elementos de la lista
    print(player.title())

### Copiar un lista ###
my_martial_arts = ["boxing", "muay-thai", "krav maga", "jiu-jitsu"]
friend_martial_arts = my_martial_arts[:] # Para copiar la lista asignamos la lista que queremos copiar y dentro de los corchetes lo indicamos con 2 puntos [:]

my_martial_arts.append("sambo") # Añado un nuevo elemento al final de la lista
friend_martial_arts.append("judo") # Añado un nuevo elemento al final de la lista

print("My favorite martial arts:")
print(my_martial_arts)

print("\nMy friend´s favorite martial arts:")
print(friend_martial_arts)

# Trozos
for martial_art in my_martial_arts[:3]: # Recorro los 3 primeros elementos de la lista
    print(martial_art.title())

print(my_martial_arts[0:3]) # Muestro los 3 primeros elementos de la lista

print(my_martial_arts[1:4]) # Muestro los elementos del medio

print(my_martial_arts[-3:]) # Muestro los 3 ultimos elementos de la lista