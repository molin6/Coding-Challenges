import sys
import itertools

list = [
[1,2,3],
[4,5],
(1,0)
]

format_list = ''.join([str(elem) for elem in list])
stripped_string = format_list.replace("[","").replace("]","").replace("'","").replace(",","").replace("(","").replace(")","").replace(" ","")



x = stripped_string.isdigit()

element1 = []
if x is False: print(-1)
else:
    for element in itertools.product(*list[:2]):
        element1.append(element)
    x_value = int(stripped_string[-2])
    y_value = int(stripped_string[-1]) + int(3)
    combo = int(stripped_string[x_value]), int(stripped_string[y_value])

    print(element1.index(combo))


