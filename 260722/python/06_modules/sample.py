import my_math

# from my_math import add 이줄이랑 밑에 주석줄이 세트

print(my_math.add(1, 2))
# print(add(1, 2)) 이줄


# 직접 만든 패키지 사용하기
from my_package.math import my_math
from my_package.statistics import tools

print(my_math.add(1, 2))  # 3
print(tools.mod(1, 2))  # 1
