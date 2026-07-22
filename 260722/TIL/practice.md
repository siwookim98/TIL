2217. 대여 불가 도서 구분하기Lv2
보유 중인 도서 리스트 list_of_book과 대여 예정 도서 리스트 rental_list가 주어진다.
반복문을 사용하여 rental_list 요소 중,보유 중인 도서 리스트 list_of_book에 포함되지 않은 요소를 발견하면 
{도서 명}은/는 보유하고 있지 않습니다. 문구를 출력한다.
보유하고 있지 않은 도서가 있다면, 위와 문구를 출력한 후, 반복문을 종료한다. 
만약 모든 도서를 보유하고 있다면, 모든 도서가 대여 가능한 상태입니다.를 출력한다.

내가 작성하던 코드
for i in range(len(rental_list)): #대여 예정 도서 리스트의 객체 길이의 갯수만큼의 연속된 정수 범위를 변수i에 저장
    target_book = rental_list[i] #추적중인 도서를 target_book변수에 저장해서 리스트 생성
    for j in range(len(list_of_book)): #보유 중인 도서 리스트의 객체 길이의 갯수만큼의 연속된 정수 범위를  변수j에 저장
        if target_book == target_book[j]:

정원님 코드
if book in list_of_book:
        continue

    else:
        print(f'{book} 은/는 보유하고 있지 않습니다')
        break