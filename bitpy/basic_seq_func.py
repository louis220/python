# 순차 보조 자료형
def using_range():

    """
    range
    - 순차 자료형
    - len, in, not in
    - 인덱싱, 슬라이싱 가능하지만 슬라이싱 활용
    - 치환, 삭제는 불가하다
    """

    # 범위의 생성 : 인자가 1개일 때 to 값
    seq = range(10) # 0부터 10 "이전"까지 간격 1
    print(seq, type(seq))

    # 인자가 2개일 때 : 시작값, 끝경계
    seq2 = range(2, 10)
    print(seq2, type(seq2))
    # range 자료형은 범위 내부의 모든 값을 미리 만들어 두는 것이 아니라
    # 필요할 때 그때 생성 -> 효율적이다
    print("Contents of seq", list(seq2))

    # 인자가 3개 : 시작값, 끝값, 간격값
    seq3 = range(2, 10, 2)
    print(seq3, list(seq3))
    # 간격이 음수일 경우 큰 값 -> 작은 값으로 내려간다

    # range는 그 자체로 효율적인 순차자료형
    seq4 = range(1, 100, 2) # 홀수들
    # 길이 산정 가능
    print(seq4, "LENGTH:", len(seq4))
    # 포함 여부 확인 가능 :in, not in
    print("10 in seq4?", 10 in seq4)
    print("11 in seq4?", 11 in seq4)
    # 인덱싱과 슬라이싱
    print(seq4[0], seq4[1], seq4[2]) # 정방향 인덱싱
    print(seq4[-1], seq4[-2], seq4[-3]) # 역방향 인덱싱
    # 내부 데이터 번경은 불가
    # seq4[10] = "something" ->Error
    print("Slicing:", seq4[:5])

    # range 객체를 순회
    for num in range(2, 10):
        print(num, end=" ")
    print()

def using_enumerate():
    """
    enumerate 함수
    - 순차형 loop 순회시 인덱스가 필요할 경우 enumerate 함수를 사용
    - (인덱스, 요소) 쌍튜플을 반환
    """
    words = "life is too short tou need python".upper().split()
    print("words:", words)

    for word in words:
        print("word:", word)
     # 루프를 돌면서 인덱스가 필요할 경우 enumerous함수로 묶어준다
    print("=====using enumerate")
    for index, word in enumerate(words):
        print(index, "번째의 word:", word)

def using_zip():
    """
    zip 객체의 사용
    - 두 개 이상의 순차 자료형을 하나로 묶어
    - 같은 위치에 있는 요소들을 튜플로 묶는다
    - 길이가 다를 경우 가장 짧은 순차자료형의 길이에 맞춘다
    """

    # 영어 단어의 목록과 한글 단어의 목록이 있을 경우,
    # 쌍으로 묶어 봅니다
    english = "Sunday", "Monday", "Tuesday", "Wednesday"
    korean = "일요일", "월요일", "화요일", "수요일", "목요일"
    # 두 순차자료형을 하나로 묶어봅니다
    engkor = zip(english, korean)
    print(engkor, type(engkor))

    # loop 돌리기
    for item in engkor:
        print(item)
    # zip 객체는 순회를 돌고 나면 비어버린다
    engkor = zip(english, korean)
    for eng, kor in engkor:
        print(eng, "->", kor)

    # 여러 순차형을 loop 돌릴 때 인덱스도 필요할 경우
    # enumerate로 묶어 준다
    engkor = zip(english, korean)
    for  index, (eng, kor) in enumerate(engkor):
        print(index, "번째 단어", eng, "->", kor)

    # zip 객체로 키 목록과 값 목록을 묶어주고 dict 함수에 넣어주면
    # dict 작성할 수 있다
    print(dict(zip(english, korean)))




if __name__ == "__main__":
    # using_range()
    # using_enumerate()
    using_zip()








































