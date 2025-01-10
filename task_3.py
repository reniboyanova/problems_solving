# Function Output Clarification

from copy import copy, deepcopy


def try_muttable(obj):
    if isinstance(obj, list):
        obj.append(4)
    elif isinstance(obj, dict):
        obj[4] = "four"
    elif isinstance(obj, set):
        obj.add(4)

def try_imuttable(obj):
    if isinstance(obj, (str, int, float, tuple)):
        print(f"I am imuttable: {type(obj)}")
        obj += "str"
        return obj
    
dict_to_try = {"123": 123, "456": 456}
set_to_try = {1, 2, 3}
list_to_try = [1, 2, 3]
str_a = "I am Reni :)"
int_a = 123
float_a = 123.123
bool_a = True 

   
try_muttable(dict_to_try)
print(dict_to_try)

print('-----------')

try_muttable(set_to_try)
print(set_to_try)

print('-----------')

try_muttable(list_to_try)
print(list_to_try)

try_imuttable(str_a)
print(str_a)

copied_obj = copy(str_a)
str_a += " I am new"
print(f"This is copied_obj after copy {copied_obj}")
print(f"This is str_a copy {str_a}")

str_b = "Hello to KBC :)"
deep_copy_obj = deepcopy(str_b)
deep_copy_obj += ":) :) :)"
print(f"This is deep_copy_obj after deepcopy {deep_copy_obj}")
print(f"This is str_b deepcopy {str_b}")

    
    