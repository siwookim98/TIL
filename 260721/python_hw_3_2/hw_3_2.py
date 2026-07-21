# 아래 함수를 수정하시오.
# def add_numbers():
#     pass


# 수정한 add_numbers() 함수를 호출하시오.
def add_numbers(num1, num2): # num1과 num2는 매개변수(parameter)
    return num1 + num2 # 두 매개변수를 더한값을 반환(return)

a = 3
b = 5

result = add_numbers(a, b) # a와 b는 인자(argument)
print(result) #함수 add_numbers에서 a, b 두 인자의 더한값을 반환 후 print함수로 출력