############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_user_data_valid(user_data):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 매개변수 user_data의 키값을 반복
    for x in user_data:  
        # 저장할 result값 초기화
        result = ""  
        # 만약 value값이 빈문자열이면
        if user_data[x] == '':    
            result = False 
            # 하나라도 빈문자열이 발견되면 반복문 탈출
            break  

        else:
            # 루프를 다 돌았을때 문자열이 있으면 출력
            result = True 

    return result  
    
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': '',
    'password': '1q2w3e4r',
}
# print(is_user_data_valid(user_data1)) # False 


user_data2 = {
    'id': 'jungssafy',
    'password': '1q2w3e4r',
}
# print(is_user_data_valid(user_data2)) # True
#####################################################

print(is_user_data_valid(user_data1))
print(is_user_data_valid(user_data2))



a = ''

a = True