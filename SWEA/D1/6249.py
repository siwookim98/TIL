# a = int(input())
# a = str(a)
# numbers = '0 1 2 3 4 5 6 7 8 9'
# count = [0] * 10

# for num in a:

#     for i in numbers:
        
#         if i == num:
#             count[int(i)] += 1
# print(numbers)
# print(*count)

a = int(input())
a = str(a)  # 자리 수 세려고 문자열로 변환

count = [a.count(str(i)) for i in range(10)]  # a 안에 str(i)가 몇 번 나오는지, 0~9 전부 리스트로

print('0 1 2 3 4 5 6 7 8 9')
print(*count)  # 리스트를 공백으로 풀어서 출력