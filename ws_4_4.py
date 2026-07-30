import requests

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


def create_user(user_list):
    censored_user_list = {}

    for user in user_list:
        name = user['name']
        company = user['company']

        if censorship(company, name):
            censored_user_list.setdefault(company, []).append(name)

    return censored_user_list


def censorship(company, name):
    if company in black_list:
        print(f'{company} 소속의 {name} 은/는 등록할 수 없습니다.')
        return False

    print('이상 없습니다.')
    return True


# 다수의 사용자 정보를 담을 리스트
dummy_data = []

# 1부터 10까지 총 10명의 사용자 정보 요청
for user_id in range(1, 11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(API_URL)
    parsed_data = response.json()

    lat = float(parsed_data['address']['geo']['lat'])
    lng = float(parsed_data['address']['geo']['lng'])

    if -80 < lat < 80 and -80 < lng < 80:
        user = {
            'name': parsed_data['name'],
            'lat': parsed_data['address']['geo']['lat'],
            'lng': parsed_data['address']['geo']['lng'],
            'company': parsed_data['company']['name'],
        }
        dummy_data.append(user)

# 사용자 목록을 등록 처리하고, 결과 딕셔너리를 출력
censored_user_list = create_user(dummy_data)
print(censored_user_list)

# 문제
# 도서관 사용자 관리 서비스 - 데이터 처리 문제에서 작성한 코드로 수집한 사용자들을 등록하는 함수를 작성하고자 한다. 
# 단, 특정 회사에 재직중인 사용자는 제외하고 등록하여야 한다. 제시된 black_list에 포함된 company 소속이 아닌 사용자만 등록할 수 있도록 코드를 작성하시오.

# 실행결과
# 이상 없습니다.
# 이상 없습니다.
# Keebler LLC 소속의 Chelsey Dietrich 은/는 등록할 수 없습니다.
# 이상 없습니다.
# Johns Group 소속의 Kurtis Weissnat 은/는 등록할 수 없습니다.
# Hoeger LLC 소속의 Clementina DuBuque 은/는 등록할 수 없습니다.
# {'Deckow-Crist': ['Ervin Howell'], 'Romaguera-Jacobson': ['Clementine Bauch'], 'Considine-Lockman': ['Mrs. Dennis Schulist']}

# 요구사항
# 1. create_user 함수에 사용자 목록을 인자로 넘겨 순회하는 코드를 작성하시오.
# 2. create_user 함수는 넘겨받은 리스트를 순회하여, company 이름을 key로, 사용자 이름을 value로 갖는 딕셔너리 censored_user_list를 생성한다.
# 2-1. 이 때, value는 리스트로 구성한다.
# 3. create_user 함수를 통해 사용자 목록을 순회하면서, 각 사용자 정보를 censorship 함수에 인자로 넘겨, black_list에 포함 되어 있는지 확인한다.
# 4. censorship 함수는 넘겨받은 회사 명이 black_list에 포함되어 있으면 '{회사명} 소속의 {사용자명} 은/는 등록할 수 없습니다.' 문구를 출력하고, False를 반환한다. 포함되어 있지 않다면 '이상 없습니다.' 문구를 출력하고 True를 반환한다.
# 5. censorship 함수의 반환 값을 기준으로 사용자 정보를 딕셔너리 censored_user_list에 담을 것인지 판단한다.
# 6. create_user는 작성 완료된 딕셔너리 censored_user_list를 반환한다.
# 7. 반환 받은 censored_user_list를 출력한다.