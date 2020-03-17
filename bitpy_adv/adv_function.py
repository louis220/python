# 함수의 스코핑 룰
# Local -> Enclosed ->Global -> Bulitin
x = 1 # Global 영역

def scope_func(a):
    print("scope_func:", locals())
    # a -> 외부로부터 넘어온 객체가 local 심볼에 할당
    # -> 로컬이 아니다
    print("x is in global?", "x" in globals())
    return a + x

# scope_func(10)
def scope_func2(a):
    x = 2 # global x와 다른 객체다
    print("scope_func2:", locals())
    return a + x

# print(scope_func2(10))

def scope_func3(a):
    # 글로벌 객체를 함수 내부에서 사용하고자 할 경우
    # global 키워드 사용
    global x # 지금부터 사용할 x는 로컬로 만들지 않고 글로벌 객체를 사용할 것을 선언한 것
    # 주의: 가능하면 글로벌 객체를 내부에서 변경하지 않을 것을 권장
    # 어디에서 글로벌 객체가 변경되었는지 추적이 힘들기 때문
    x = 3
    print("scope_func3:", locals())
    return a + x
# print(scope_func3(10))
# print("x:", x)

# 함수의 선언 ( 주로 가변인자와 키워드 인자 중심으로 정리)
# 프로그래밍에서의 함수는 기능의 집합
# 입력값이 없을 수도 있고, 출력이 없을 경우도 있다
# 함수를 종료할 떄는 return
# return 뒤에 반환값을 명시하면 결과를 받을 수 있다
# 값을 return 하지 않았더나 끝날떄까지 아무 return도 없는 경우
# ->None( Java의 null과 비슷)

def times(a, b):
    return a * b

#함수자체도 객체로 판단
# 다른 식별자에 할당할 수 있고
# 다른 함수의 인수로 전달할 수 있다
fun = times
print("fun:", type(fun))
# 객체가 호출 가능한 객체인지(함수) 판별하려면 callable 함수
print("is fun callable?", callable(fun))

# 만약 객체가 함수인지 판별한 이후에 호출
if callable(fun): print(fun(10, 20))

# 인수의 기본값
def incr(a, step=1): # 두번째 인자값은 1이 기본값이다
    return a + step

print(incr(10)) # 두번쨰 인자 step이 기본값을 가지고 있으므로 기본값으로 세팅

print(incr(10, 2)) # 기본값을 무시하고 있으므로 새로운 값을 할당

# 기본적으로 python은 인수의 이름을 명시 인자 전달할 수 있다
# 인자의 순서가 중요하지 않게 된다

print(incr(step=3, a=10))

# 가변 인수
# 정해지지 않은 개수의 인자를 받을 때
# 가변 인자를 받을 변수의 앞에 * 명시
# -> 순차 자료형으로 변환되어 입력

# 연습 : 여러개의 인자를 넘겨 받아서
#        해당 인자가 int, float이면 합산
#        그렇지 않으면 합산에서 제외
#        합계를 return

def get_total(*args):
    total = 0
    # print(args, type(args))
    for x in args:
        # 합산 가능한 타입인지 체크
        if isinstance(x, (int, float)):
            total += x
    return total

print(get_total(1, 2, 3, 4, 5))
print(get_total(1, 2, 3, 4, 5, "Python", (1, 2, 3)))

# 고정인자와 가변인자 키워드 인자
# 순서가 중요
# 고정인자 -> 가변인자(*) -> 키워드 인자(**)
def func_args(a, b, *args, **kwd):
    # a, b,는 고정인자 : 반드시 넘겨주어야 한다
    # 그 뒤에 나온 인자의 목록은 args로 넘어올 것이다(tuple)
    # 그 뒤에 나온 인자는 키워드(dict)로 넘어옴
    print("고정인자:", a, b)
    print("가변인자:", args)
    print("키워드 인자:", kwd)

    if "option1" in kwd:
        print("option 1이 {}로 설정되었습니다.".format(kwd['option1']))
    else:
        print("option 1이 설정되지 않았습니다")
func_args(1, 2, 3, 4, 5, 6, option1="옵선1", option2="옵션2")

# 함수도 객체이므로 다른 함수의 인자로 넘겨줄 수 있다
# callback 패턴
def calc(a, b, func):
    # 계산을 위한 수 2개
    # 계산 식 함수 func 를 전달
    # 넘겨 받은 func가 호출 가능 객체인지 확인
    if callable(func): # func은 함수?
        return func(a, b) # 계산 함수는 외부로부터 주입

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

print(calc(10, 20, plus))
print(calc(10, 20, minus))

# lambda 함수 : 익명 함수
print(calc(10, 20, lambda a, b: a * b)) # 즉석에서 곱셈 함수 전달

# lambda 함수를 이용한 sort(sorted) 키함수 정의
words = "life is too short, you need python".upper()\
    .replace(",", "").split()
print("WORDS:", words)
# sort 할때 정렬기준 key 함수를 lambda로 전달
# 단의 길이의 역순 정렬 함수를 람다로
sorted_words = sorted(words, key=lambda word: len(word),
                      reverse=True)
print("sorted words:", sorted_words)

# 1부터 20까지 수열을 4로 나누었을 때의 나머지 순으로 정렬
nums = range(1, 21) # 20까지이므로
print("nums:", list(nums))
print("Sorted num % 4 ASC:", sorted(nums, key=lambda n: n % 4))


























































