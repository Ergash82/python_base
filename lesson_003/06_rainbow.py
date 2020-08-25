# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

sd.resolution = (450, 500)

def lines (sp):
    x = 5
    for i in range(0, sp):
        x += 5
        sd.line(start_point=sd.get_point(50+x, 50), end_point=sd.get_point(350+x, 450), width=4, color=rainbow_colors[i])

sp = 7
lines(sp)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

'''sd.resolution = (420, 420)
point = sd.get_point(300, -60)

def rainbow(point,step):
    i = 0
    radius = 325
    for i in range(0, step):
        radius += 15
        sd.circle(center_position=point,radius=radius,color=rainbow_colors[i],width=15)


step = 7
rainbow(point,step)'''

sd.pause()
