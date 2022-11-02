var = []

print(isinstance(var, list))  # Проверка принадлежности к классу

my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]

my_list1.extend(my_list2)  # Конкатенация листов

print(my_list1)
print(my_list1.index(4))
my_list1.insert(0, 'sdasdsd')
print(my_list1)
print(my_list1[1:6:2])

a = ['декабрь', 'январь', 'февраль']
a.sort()
print(a)
print(ord('a'))  # Узнать код символа
print(chr(1103))  # Узнать символ по коду
a_str = ',,,'.join(a)
print(a_str)