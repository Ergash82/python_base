#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['I', 'My_Wife', 'Firs_Son','Second_Son', 'Daughter','GrandFather', 'GrandMother']

# список списков приблизителного роста членов вашей семьи
my_family_height = [['I', 1.72],
                    ['My_Wife', 1.70],
                    ['Firs_Son', 1.2],
                    ['Second_Son', .8],
                    ['Daughter', 1.60],
                    ['GrandFather', 1.70],
                    ['GrandMother', 1.60]]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print(my_family_height[5][0], int(my_family_height[5][1]*100),'см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
SumHeights = my_family_height[0][1] + \
            my_family_height[1][1] + \
            my_family_height[2][1] + \
            my_family_height[3][1] + \
            my_family_height[4][1] + \
            my_family_height[5][1] + \
            my_family_height[6][1]

print(int(SumHeights)*100,'см')