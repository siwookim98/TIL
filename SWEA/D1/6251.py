# for i in range(1,6):
#     print(' ' * (5 - i) + '*' * i)

star = ['*', '*', '*', '*', '*']
for i, single_star in enumerate(star, 1):
    print(' ' * (5 - i) + single_star * i)