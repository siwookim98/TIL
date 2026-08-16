# 1. 원본 데이터 리스트 생성
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2. filter 함수와 lambda를 사용하여 짝수만 추출
#    - filter(함수, 반복가능객체): 함수의 리턴값이 True인 요소만 남김
#    - x % 2 == 0 : x를 2로 나눈 나머지가 0이면 짝수라는 뜻
#    - filter()의 결과는 filter 객체(제너레이터 유사)이므로 list()로 감싸서 리스트로 변환
even_list = list(filter(lambda x: x % 2 == 0, numbers))
# even_list = [2, 4, 6, 8, 10]

# 3. map()과 lambda를 사용해 짝수 리스트의 각 요소를 제곱
#    - map(함수, 반복가능객체): 각 요소에 함수를 적용한 결과들을 반환
#    - x ** 2 : x의 제곱
#    - map()의 결과도 map 객체이므로 list()로 감싸서 리스트로 변환
square_even_list = list(map(lambda x: x ** 2, even_list))
# square_even_list = [4, 16, 36, 64, 100]

print(square_even_list) # 출력: [4, 16, 36, 64, 100]