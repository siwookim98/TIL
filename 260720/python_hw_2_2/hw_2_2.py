book = '1'
total = 10
guide = '현재 보유 중인 총 책의 수는 다음과 같습니다.'
print(guide)
print(int(book) * total) #변수 book이 string 변수라서 int()함수로 정수로 명시적 형변환함.

changes = '그 중, 대여중인 책을 제외한 책의 수는 다음과 같습니다.'
rental = 3.0
print(changes)
print(total - int(rental)) #변수 rental이 float 변수라서 int()함수로 정수로 명시적 형변환함.
