# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (900, 600)

def rectang (left_bottom,right_top):

        sd.rectangle(left_bottom=left_bottom,right_top=right_top,color=sd.COLOR_DARK_ORANGE,width=2,)

i=1
z=0
for _ in range(1,13):
    z+=50
    x=0
    i += 1
    for _ in range(0, 7):
        x += 150
        if i%2==0:
            right_top = sd.get_point(x+75, z)
            left_bottom = sd.get_point(x - 75, z-50)
        else:
            right_top = sd.get_point(x, z)
            left_bottom = sd.get_point(x - 150, z - 50)
        rectang(left_bottom, right_top)
        print(f'{i} кирпичей {z}')


# sd.pause()
