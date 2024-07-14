# 1.Функция с параметрами по умолчанию:

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(a=1, b=25, c=True)
print_params(a=1, b="строка", c=[1, 2, 3])


# 2.Распаковка параметров:

values_list = ["привет"]
values_dict = {"b": 1, "c": True}


def print_params(a, b, c):
    print(a, b, c)


print_params(*values_list, **values_dict)

# 3.Распаковка + отдельные параметры:

values_list_2 = [56, False]


def print_params(a, b, c=[4, 5]):
    print(a, b, c)


print_params(*values_list_2, [4, 5])


