number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1
    return number_of_people

# increase_user()
# print(number_of_people)

def create_user(**name_age_address):
    increase_user()
    user_info = {}
    return 

print("현재 가입 된 유저 수 :", number_of_people)

