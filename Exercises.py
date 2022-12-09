# def function(): # Don't be confused, we use 'def()' to create a function. 
#                 # You will see it in the next lessons.
#     """
# Hi, I am the docstring of this code. 
# If you need any information about this function or module, read me. 
# It can help you understand how the module or function works.
#     """
# print(function.__doc__)

# print(print.__doc__)
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

# Prints the values to a stream, or to sys.stdout by default.
# Optional keyword arguments:
# file:  a file-like object (stream); defaults to the current sys.stdout.
# sep:   string inserted between values, default a space.
# end:   string appended after the last value, default a newline.
# flush: whether to forcibly flush the stream.


# a = 36.5
# b = '30'
# c = '3.5'
# d = ' F is enough for room temperature.'

# print(str(a+int(b)+float(c))+d)

# a = "cet"
# b = "al"
# # print(a,b) default boşluk olur
# print(a, b, sep="/")   cet/al yazar

# num1 = 5
# num2 = 5.18
# print(type(num1)) //int
# print(type(num2))  //float

# print(int(False)) //0

# x = "55"
# y = 3
# print(x * 3) //555555 başka operatörde TypeError verir

# city = "corum"
# print(city[2:5:2]) 
# print(city[-5:-2]) 
# print(city[-2:-5:-1])  -2 deb başlar -5 de biter ama almaz -1 atlayarak
# print(city[::]) tamamını alır

# a = "cet"
# print(a*3) //cetcetcet

# year = 4
# language = 'Python'

# print('I knew {} for {} years')

# asd = "osman"
# print(asd.split()) //['osman']

# number = 123145
# print(str(number).startswith('1')) // true
# print(str(number).startswith('3', 2)) // true

# print(1 and 0) //0

# print(3 and not False or []) // True

# set_1 = set("washingthon")
# set_2 = set("wellingthon")
# print(set_1.union(set_2))
# print(set_1.difference(set_2))
# print(set_1.intersection(set_2))

# score = int(input('Enter your scroe:'))

# if score >= 90:
#     if score >= 95:
#         print('A+')
#     else:
#         print('A')
# else score >= 80:
#     if score >= 85:
#         print('B+')
#     else:
#         print('B-')     
           
# age = input('Enter your age:')

# while not age.isdigit():  # girilen rakamın 0-9 mu diye bakar
#     print('Please enter correct data')
#     age = input('Enter your age:')

#     print(f'Your age is {age}')


# my_number = 15
# while True: # while is_true:
#     your_number = int(input)('Enter your number: ')

#     if your_number > my_number:
#         print('Please reduce you number')
#     elif your_number < my_number:
#         print('Please increase your number') 
#     else:
#         print("You win")
#         break

# a = 'istanbul, ankara, corum'
# word_list = a.split(', ')

# i = 0
# longest = 0
# while i< len(word_list):
#     if len(word_list[i]) > longest:
#         longest = len(word_list[i])
#     i +=1
#         print(longest)
