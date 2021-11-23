# for name in names['Elbek', 'Zakir']:
#     pass                               #pass = #пропусти


# []- list (mutable) изменяемый
# ()- tuple (immutable) неизменяемый

#ELBEK
# #print('Elbek'.upper)


# name = 'Elbek'                  #upper - заглавленные буквы
# print = name.upper()
# print(name)

# name = 'Elbek'
# name = name.upper()           #del - 
# name[0] = 'A'

# name = 'Elbek'                 #lower - все символы маленькие
# name = name.lower()

# name = 'Elbek is mentor'                 #islower - true(если бугвы заглавленные ), false 
# name = name.lower()

# name = 'Elbek is mentor'                 #найди и скажи номер индекс
# name = (name.index('s'))

                                             #peremennyy.isalpha() -- 
# name = ('elBek is             mentor                       ')
# print = name.isalpha()                            # .count('') -- считает по заданному 
# print = name.find('e')
# name = name.rstrip()                       #справа убирает пробелы
# name = name.lstrip()                       #слева убирает пробелы
# print(name)

# i = 0
# str = ''
# for ltr in 'Elbek':
#     if i % 2 == 0:
#         str = str + ltr.lower()
#     else:
#         str = str + ltr.upper()
#     i += 1
# print(str)
            
'''
i = 0
str = ''
for ltr in '':
    if i % 2 == 0:
        str = str + ltr.upper()
    else:
        str = str + ltr
    i += 1
print(str)
           ''' 

# i = 0
# str = ''
# for letter in "Hi, he's name is Elbek":
#     if i % 2 == 0:  str += letter.upper()
#     else: str += letter
#     i += 1
# print(str)


                                                                 #a,b = (2,3)
# str = ''
# for i, letter in enumerate("Hi, he's name is Elbek",0):           #enumarate
#     if i % 2 == 0:  str += letter.upper()
#     else: str += letter
# print(str) 


# str = ''
# for i, letter in enumerate("Hi, he's name is Elbek"):           циклы #enumarate ()[]
                                                                 # range()[]
#     if i % 2 == 0:  str += letter.upper()
#     else: str += letter
# print(str) 

              
                         # обратный порядок

# str = "Hi, he's name is Elbek"
# str2 = ''
# for ltr in str:
#     str2 = ltr + str2
# print (str2)


# str = "Hi, he's name is Elbek"
# str2 = ''
# for i in range(len(str)-1, -1, -1):
#     str2 += str 
#     print (str[i])

# str = "Hi, he's name is Elbek"
# str2 = ''
# for ltr in str:
#     str2 = ltr + str2
# print (str2)

# namelist = list('Elbek')                        # list = строка; list = строка; tuple = строка
# namelist.reverse()
# str = '*'.join(namelist)
# print(str)

# nums = [1, 2, 3]
# t = tuple(nums)                 #tuple превращает [] в ()
# print(t)



# print([elem for elem in range(10)])

# print([elem % 2 for elem in range(10)])


# print([elem for elem in range(10) if elem % 2 == 0])






#random
# from random import random
# from random import randint
# print(int(random() * 255))
# print(randint(0, 255))

# print(int(100 + random() * (500 - 100)))
# print(round(100 + random() * (500 - 100)))



from datetime import datetime as d, date
print(d.now())                    #datetime = d
