def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
#1.Функция с параметрами по умолчанию:
print_params(b = 25)
print_params(c = [1,2,3])
#2.Распаковка параметров:
values_list = ['Evgeniy', 25, False]
values_dict = {'a':1980, 'b':True, 'c':'Lev'}
print_params(*values_list)
print_params(**values_dict)
#Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

