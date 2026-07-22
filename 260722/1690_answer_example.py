"""
[강사용] 오늘 실습 답안 -- 정리 및 주석 보강 버전
=====================================================
원본 대비 바뀐 점:
    1) 'from pprint import pprint as print' 제거.
       -> 이 alias 때문에 모든 메시지가 '이상 없습니다.' 처럼 따옴표에 감싸여 출력됐다.
       -> 최종 결과 딕셔너리를 보기 좋게 볼 때만 pprint()를 따로 호출한다.
    2) 루프 첫 줄의 'user_info = {}' 삭제. (if를 통과하면 재할당, 못 하면 안 쓰임 = 죽은 코드)
    3) 그룹핑의 .get() 두 번 호출 -> 명시적 if/else 로 교체. (초보 가독성)
    4) 수집 로직을 collect_users() 함수로 묶어 책임을 분리하고, import 시 네트워크가
       실행되지 않도록 정리. (테스트/재사용 편의)

로직 흐름 (3단계):
    1단계 [수집]   API에서 유저 10명을 받아, 위경도 조건 통과자만 리스트에 쌓는다.
    2단계 [검열]   블랙리스트 소속이면 등록 거부(False), 아니면 통과(True).
    3단계 [그룹핑] 통과한 유저를 회사별로 묶어 {회사: [이름들]} 형태로 만든다.
"""

from pprint import pprint

import requests

# 등록을 거부할 블랙리스트 회사 목록
black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


# =============================================================================
# 1단계 [수집] -- API에서 유저를 받아, 조건 통과자만 리스트에 '쌓는다'
# =============================================================================
def collect_users():
    # 빈 리스트를 먼저 만든다 -> 조건을 통과한 유저를 여기에 쌓을 것이다
    dummy_data = []

    for i in range(1, 11):
        api_url = f'https://jsonplaceholder.typicode.com/users/{i}'
        response = requests.get(api_url).json()

        # 위도/경도는 문자열로 오므로 float으로 변환해서 비교한다
        lat = float(response['address']['geo']['lat'])
        lng = float(response['address']['geo']['lng'])

        # 조건: 위도와 경도가 모두 -80 ~ 80 범위일 때만 수집한다
        if -80 < lat < 80 and -80 < lng < 80:
            user_info = {
                'name': response['name'],
                'lat': response['address']['geo']['lat'],
                'lng': response['address']['geo']['lng'],
                'company': response['company']['name'],
            }
            dummy_data.append(user_info)  # 누적: 통과한 사람만 쌓기

    return dummy_data


# =============================================================================
# 2단계 [검열] -- 블랙리스트 소속이면 거부(False), 아니면 통과(True)
# =============================================================================
def censorship(user):
    if user['company'] in black_list:
        print(f'{user["company"]} 소속의 {user["name"]} 은/는 등록할 수 없습니다.')
        return False
    print('이상 없습니다.')
    return True


# =============================================================================
# 3단계 [그룹핑] -- 통과한 유저를 회사별로 묶는다 {회사: [이름, 이름, ...]}
# =============================================================================
def create_user(dummy_data):
    # 빈 딕셔너리를 먼저 만든다 -> {회사: [이름들]} 형태로 쌓는다
    grouped = {}

    for user in dummy_data:
        # 검열을 통과하지 못하면 건너뛴다 (early continue 로 중첩을 줄임)
        if not censorship(user):
            continue

        company = user['company']
        # 회사 key가 이미 있으면 이름만 추가, 없으면 새 리스트로 시작한다
        if company in grouped:
            grouped[company].append(user['name'])
        else:
            grouped[company] = [user['name']]

    return grouped


if __name__ == '__main__':
    users = collect_users()
    pprint(create_user(users))
