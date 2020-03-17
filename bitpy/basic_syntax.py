# .py 파일 한 개는 하나의 모듈이다
# 파일면 자체가 모듈의 이름이 되므로
# 파일명 정할 때도 변수 명명 규칙을 위반하지 않도록

# 들여쓰기로 블록을 판단하므로 들여쓰기에 유의
# 함수 작성 키워드는 def

# 연산자 테스트 함수
def arith_oper():
    # 블록을 시작됐지만 구현부가 없을 경우
    #pass
    print("===== 산술 연산")
    # + ,-,*,/
    # / : 정수와 정수의 나눗셈이더라도
    #     소숫점이 발생하면 실수로 변경
    print(7 / 5) #정수를 정수로 나눠도 실수 형태로 보여줌
    print(7 // 5) #나눗셈의 몫
    print(7 % 5) #나눗셈의 나머지
    #나눗셈의 몫과 나머지 구하는 함수 divmod
    print(divmod(7, 5)) #7을 5로 나눈 몫과 나머지
    print("7 / 5의 몫:", divmod(7, 5)[0])
    print("7 / 5의 나머지:", divmod(7, 5)[1])

    print("7의 3승:", 7 **3)
    print("7의 3승:", pow(7, 3))

def complex_ex():
    print("===== 복소수")
    # 형태 : 실수부 + 허수부j
    print(3+4j) # 실수부 3, 허수부 4인 복소수
    print(3+4j.real) # 실수부
    print(3+4j.imag) # 허수부
    print(3+4j.conjugate()) # 켤레복소수

    print(complex(3, 4)) # complex 타입을 이용한 복소수 생성

def tel_oper():
    print("=====비교 연산(관계연산)")
    # == (같다) != (같지않다)
    # >, >= , <, <=
    # 관계연산으로 대소 비교 -> boot(True, False)

    a = 6
    # a가 0보다 크고, 10보다 작다
    print(0 < a and a < 10) # 복합 관계식
    print(0 < a < 10)

    # 수치데이터 이외의 대소 비교
    print("문자열의 대소:", "abcd" > "abce")
    print("순차형의 대소:", (1, 2, 3) < (1, 2, 4))

    # 동질성의 비교 ==  동일성의 비교 is
    a = 10; b = 20; c = a
    print("a == b?", a == b)
    print("a == c?", a == c)
    print("a is c?", a is c)

def variable_ex():
    print("===== 변수")
    # 파이선의 변수는 선언 작업이 없고
    # 최초 할당시 변수가 선언된다
    # 동적 인터렉티브 언어이기 때문에
    # 타입이 지정되지 않는다( 할당시에 타입이 결정)
    # 변수명은 문자, 숫자, _의 조합
    # 숫자로 시작할 수 없다
    # 예약어는 사용할 수 없다

    # 예약어의 확인
    import keyword
    print(keyword.kwlist) # 예약어 목록
    print("예약어의 갯수:", len(keyword.kwlist))

    # 변수의 치환
    a = 1
    # 여러 변수를 한꺼번에 할당
    c, d = 3.5, 5.3 # 변수의 갯수와 값의 갯수는 일치해야 한다
    print(c, d)
    # 같은 값을 여러 변수에 동시 할당
    x = y = z = 10 # 세 변수에 10이 동시할당
    print(x, y, z)

    # 파이썬은 동적 타이핑 언어
    # 값이 할당될 때 타입 결정
    a = 10
    print(a, "is", type(a)) # type 함수로 타입 확인
    # 다른 타입의 객체도 재할당 될 수 있다
    a = "Python"
    print(a, "is", type(a))

    # 별수가 기리키는 객체가 특정 타입인지 확인 : isinstance 함수
    print("a는 str 객체?", isinstance(a, str))
    n = 3.14
    # 변수가 가리키는 객체의 타입을 비교할 때,
    # 여러 개의 타입 중 하나인지 확인
    print("n은 int 혹은 float?", isinstance(n, (int, float)))






if __name__ == "__main__":
    # arith_oper()
    # complex_ex()
    # tel_oper()
    variable_ex()

















