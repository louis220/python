# Set 연습
evens = {0, 2, 4, 6, 8} # 짝수 집합
odds = {1, 3, 5, 7, 9} # 홀수 집합
numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} # 전체 집합
mthree = {0, 3, 6, 9} # 3의 배수 집합

def define_set():
    """
    Set 정의 연습
    """
    """
    Set
    - 순서가 없고, 중복 허용 많음
    - 인덱싱 안되고, 슬라이싱도 불가
    - len, 포함 여부(in, not in) 정도만 사용 가능
    - 집합을 표현하는 자료형( 집합 연산 가능)
    """
    # 리터럴 기호 {}
    # {}-> set과 dict 양쪽에서 공유하므로
    # empty set을 만들때는 {} ->불가
    s = set() # Empty Set -> {} (X)
    s = set() # Empty Set ->{} (X)
    print("s:", type(s))

    # 길이와 포함 여부는 확인 할 수 있다
    print(numbers, "LENGTH:", len(numbers))
    #2가 각 집합에 포함되어 있는가?
    print(2 in numbers, 2 in evens, 2 in odds, 2 in mthree)
    # Set 객체 함수를 이용, 다른 순차 자료형을 set으로 캐스팅 할 수 있다
    s = "Python Programming"
    print(s, "LENGTH:", len(s))
    chars = set(s.upper())
    print(chars, "LENGTH:", len(chars))
    # 중복 허용하지 않는 특성
    # -> 리스트 등 자료형에서 중복을 제거할 때 유용
    lst = "Python Programming Java Programming R Programming". split()
    print(lst)
    lst = list(set(lst))
    print("중복 제거:", lst)

def set_methods():
    """
    Set의 메서드들
    """
    # 요소의 추가 : add
    numbers.add(10)
    print(numbers)

    print("evens:", evens)
    evens.add(2) # 중복 추가는 허용되지 않음 -> 집합
    print("evens:", evens)

    # 요소 삭제
    # discard :  요소 삭제 -> 요소가 없어도 오류는 내지 않는다
    # remove : 요소 삭제 -> 요소가 없으면 오류
    numbers.discard(10)
    print("numbers:", numbers)
    numbers.discard(10) # 요소가 없어도 오류 없음
    if 10 in numbers:
        numbers.remove(10) # 요소가 없으면 오류 발생
    else:
        print("삭제할 요소가 없음")
    evens.update({10, 12, 14, 16}) # 여러 요소를 한번에 업데이트
    print("evens:", evens)

    evens.clear() # 셋 비우기
    print("evens:", evens)

def set_oper():
    """
    집합 연산
    """
    # 합집합 : |, union 메서드
    print("짝수 합집합 홀수", evens.union(odds))
    print(evens.union(odds) == numbers)
    print(evens | odds == numbers)

    # 모집합, 부분집합의 판단 issuperset, issubset
    print(numbers.issuperset(evens), numbers.issuperset(odds))
    print(evens.issubset(numbers), odds.issubset(numbers))
    print(evens.issuperset(odds))

    # 교집합 : &, intersection 메서드
    print(evens.intersection(mthree) == {0, 6}) # 짝수와 3의 배수의 교집합
    print(odds & mthree == {3, 9}) # 홀수와 3의 배수의 교집합

    # 차집합 : -, difference메서드
    print(numbers.difference(evens) == odds) # 전체 수와 짝수의 차집합
    print(numbers - odds == evens) # 전체 수와 홀수의 차집합

def loop():
    """
    세트의 순회
    """
    print("numbers:", numbers)
    # 순회
    for item in numbers:
        print(item, end=" ")
    print()



if __name__ == "__main__":
    # define_set()
    # set_methods()
    # set_oper()
    loop()
















