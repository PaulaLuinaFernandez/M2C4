from decimal import Decimal
import math

# Exercise_1
my_list = ['Ana', 'María', 'Elena']
my_tuple = ('Ángel', 'Suárez')
my_float = 10.22
my_integer = 33
my_decimal = Decimal(10.1)
my_dictionary = {'Ana': 8,
              'María': 9,
              'Elena': 11}

exercise_2 = math.ceil(my_float)
exercise_3 = math.sqrt(my_float)
exercise_4 = list(my_dictionary.items())[0]
exercise_5 = my_tuple[1]

print(my_decimal)
print(exercise_2)
print(exercise_3)
print(exercise_4)
print(exercise_5)

#Exercise_6 
my_list.extend(['Lucía'])
print(my_list)

#Exercise_7
my_list[0]='Cristina'
print(my_list)

#Exercise_8
my_list.sort()
print(my_list)

#Exercise_9
my_tuple = my_tuple + ('Martínez',)
print(my_tuple)
