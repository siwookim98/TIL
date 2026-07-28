############## 주의 ##############

def is_user_data_valid(user_data):
    

    for x in user_data:  

        result = ""  

        if user_data[x] == '':  
            result = False 
            break  

        else:
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