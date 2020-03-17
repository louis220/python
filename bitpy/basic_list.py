# 리스트 연습
"""
list
-순차 자료형
    -순서있고, 길이(len), 포함여부 확인(in, not, in)
    -인덱싱, 슬라이싱
    -연결(+), 반복(*)
- 가변 자료형(mutable)
    -내부 자료 변경이 된다
"""

def define_list():
    """ 리스트의 정의"""
    lst1 = list() #빈리스트
    print(lst1, type(lst1))
    lst2 = [] # 리터럴을 이용한 빈리스트
    lst3 = [1, 2, "python"] # 내부 요소들은 어떤 객체든 상관 없다
    print(lst3, type(lst3))

    # 다른 순차 자료형을 list() 객체 함수로 list로 변경할 수 있다
    lst4= list("python programming")
    print(lst4)

def list_oper():
    """ 리스트의 연산자"""
    lst = [1, 2, "python"]
    # 길이를 잡을 수 있다 :len
    print(lst, "length:", len(lst))
    # 포함 여부 확인 : in, not in
    print("1이 lst에 있는가?", 1 in lst)

    # 인덱싱 가능
    print("정 인덱싱:", lst[0], lst[1], lst[2])
    print("역 인덱싱:", lst[-3], lst[-2], lst[-1])

    # 슬라이싱
    print(lst[1:3]) # 항상 경계에 유의
    print(lst[1:]) # 끝 경계 생략되면 끝까지
    print(lst[0:2])
    print(lst[:2]) # 시작 경계 생략되면 처음부터
    print(lst[:]) # 리스트 전체

    copy = lst[:] # 전체 리스트의 복제
    print("복제:", copy)
    print("copy is lst?", copy is lst)

    # 연결 (+)
    print(copy + ["Java", True, 3.14159])
    # 반복(*)
    print(copy *2)
    # 연결과 반복은 새로운 리스트를 생성한다( 원본 유지)

    #append vs extend
    #append는 "마지막"에 새 요소를 추가
    print(copy)
    copy.append([3, 4])
    print("APPEND:", copy)
    # 내부에서 4를 찾아내야 한다면
    print(copy[3][1])
    del copy[3]
    # extend는 인자로 부여된 리스트를 뒤에 연결(확장)
    copy.extend([3,4])
    print("Extend:", copy)

    # insert(i, x) : i 인덱스에 x를 추가
    copy.insert(2,[1, 2, 3]) # 2번 인덱스 위치에 [1, 2, 3]
    print("INSERT:", copy)

    # 포함 여부 확인 : in, not in
    # copy리스트 내에서 "python" 요소 있는지 확인
    print("포함 여부:", "python" in copy)

    # 인덱스 확인
    # copy 리스트 내부에 "python" 문자열의 인덱스
    print("Index of python:", copy.index("python"))
    # 만약 찾고자 하는 요소가 내부에 없으면 에러
    # 아쉽게도 find는 없다
    # 없는 요소를 검색할 경우 반드시 포함 여부를 확인
    # copy 리스트에서 "java"를 검색
    if "Java" in lst :
        print("Index of Java:", lst.index("Java"))
    else:
        print("Java는 없어요")
    # 요소의 갯수 파악 :count
    # lst 리스트에서 1의 갯수
    print("Count of 1:", lst.count(1))

    # 요소의 삭제 :del(인덱스로 삭제), remove(요소 값의 삭제)
    # remove도 삭제할 객체가 내부에 없으면 error 가 뜨므로
    # 리스트 내부에 해당 객체가 있는지 먼저 확인
    if 3 in copy:
        copy.remove(3)
    print("Remove 3 from copy:", copy)

    # slice를 이용한 삽입, 변경, 치환, 삭제
    # 메서드를 이용한 삽입, 변경, 치환, 삭제보다
    # slicing을 이용한 부분을 확용할 것을 권장

    lst2 = [1, 12, 123, 1234, 12345] # len ==5인 리스트
    print("lst2", lst2)
    # slicing을 이용한 삽입
    # 2번 인덱스 위치에 [10, 20] 추가
    lst2[2:2] = [10, 20]
    print("lst2:", lst2)
    # slicing을 이용한 삭제
    # 범위를 잡고 해당 범위에 빈리스트[] 할당
    lst2[2:4] = []
    print("lst2:", lst2)
    # Slicing을 이용한 치환
    # 범위를 잡고 해당 범위에 다른 리스트를 할당
    lst2[1:4] = [10, 20]
    print("lst2:", lst2)

    # slicing을 이용, 가장 마지막에 삽입(extend와 비슷)
    lst2[len(lst2):] = [30]
    print("lst2:", lst2)
    # slicing을 이용, 가장 앞쪽에 삽입
    lst2[:0] = [40]
    print("lst2:", lst2)

def list_method():
    """리스트의 메서드
    reverse와 sort"""

    # reverse: 리스트 요소의 순서를 뒤집는다
    lst = [80, 90, 85, 70, 60, 75, 100, 95]
    # 복제본
    copy = lst.copy()
    print("Reverse 이전:", copy)

    copy.reverse()
    print("Reverse 이후:", copy)

    # sort: 정렬
    # -sorted : 문법상 정렬 함수 -> 정렬 시도한 객체 내용을 변경하지 않음
    # sort : 객체 내부의 정렬 메서드 -> 객체 내부의 내용을 변경
    # sort, sorted는 그 이외의 사용방법은 동일하다
    print("sorted 이전:", copy)
    print("sorted 수행:", sorted(copy)) # 기본적으로는 오름차순 정렬이다
    print("Sorted 수행 이후:", copy) # sorted는 객체 내부 데이터 변경 없음

    # copy 객체 내부의 sort 매서드를 수행
    copy.sort()
    print("sort 수행 이후:", copy) # sort는 객체 내부의 데이터를 변경

    # 역순 정렬 : sort, sorted에 reverse= true를 부여하면 역순 정렬
    copy = lst.copy()
    print("역순 정렬 이전:", copy)
    print("역순 정렬:", sorted(copy, reverse=True))

    # copy를 정수형이 아닌 str 기준으로 역순 정렬
    print("lst str 기준 역순 정렬", sorted(copy, key=str, reverse=True))

    # key 인자값에 두 값을 비교하는 함수를 부여
    # 사용자 정의 정렬 기준을 마련할 수 있다
    lst = [19, 46, 37, 35, 91, 55, 64]
    # 각 요소 값들을 10으로 나눈 나머지를 정렬기준으로 설정
    # sort를 위한 key 함수 선언
    def key_func(val):
        return val % 10
    lst2 =  sorted(lst, key=key_func)
    print("Custom Sort:", lst2)

    # 문자열을 기준으로 문자열의 길이를 대상으로 sort하는 key 함수
    def key_length(val):
        return len(val)

    words = "Life is too short you need python".split()
    print("WORDS:", words)
    # 단어 길이의 역순으로 정렬
    print("단어 길이의 역순 정렬:", sorted(words, key=key_length, reverse=True))

def loop():
    """리스트의 순화"""
    words = "Life is too short you need Python".split()
    print("WORDS", words)

    # 순차형 자료형은 for ... in... 문으로 차례대호
    # 요소를 반환받을 수 있다.( 별도의 인덱스 변수는 없다)
    for word in words:
        print("Word in words:", word)



def stack_ex():
    """
    리스트를 활용한 Srack 구현
    append와 pop 메서드를 이용하면 stack 자료형을 구현할 수 있다
    """
    stack = []

    # input
    stack.append(10)
    stack.append(20)
    stack.append(30)

    # output: input 방향과 동일
    print(stack.pop())
    print(stack.pop(-1))
    print(stack.pop())
    # pop하기 전에 비어있는지 체크
    if len(stack) > 0:
        print(stack.pop())
    else:
        print("스텍이 비어있음")
    print("STACK:", stack)

def queue_ex():
    """
    리스트를 응용한 Queue 자료형의 구현
    리스트의 append, pop(0)를 이용하면
    Queue 구현 가능
    """
    queue = []
    queue.append(1)
    queue.append(2)
    queue.append(3)

    print("QUEUE:", queue)
    # output은 앞에서부터 0번 인덱스
    print(queue.pop(0))

    while(len(queue) > 0):
        print("Queue item:", queue.pop(0))




if __name__=="__main__":
    # define_list()
    # list_oper()
    # list_method()
    # loop()
    # stack_ex()
    queue_ex()
































