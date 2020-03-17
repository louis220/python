# 파일 IO 연습
"""
-open : 파일을 연다
    모드 r(읽기: 기본) w(쓰기) a(추가)
    타입 w( 텍스트: 기본) b(바이너리)
"""

def write01():
    # 파일을 열기 위해 open
    # w 모드는 이미 파일이 있어도 새로 파일을 작성
    f = open("./sample/test.txt", "w", encoding="utf-8")
    # t가 기본값이어서 생략
    write_size = f.write("Life is short, You need Python.")
    print("{}만큼 저장:", write_size)
    f.close() # 파일 사용 후 반드시 닫아주기


def write02():
    # append 모드 : 이미 파일이 있으면 내용은 그대로 두고
    # 뒷쪽에 새로운 데이터를 추가한다
    f = open("./sample/test.txt", "a", encoding="utf-8")
    f.write("Append 모드로 저장하였습니다.")
    f.close()

def copy_binary():
    # 이전 데이터 파일을 다룰 때는 파일 형식을 b로 설정
    f_src = open("./sample/rose-flower.jpeg", "rb")
    # r이 기본값 -> 생략 가능
    data = f_src.read()
    f_src.close()

    f_target = open("./sample/rose-flower-copy.jpeg", "wb")
    f_target.write(data)
    f_target.close()

def read01():
    # 파일 읽기
    f = open("./sample/sangbuk.csv", "rt", encoding="utf-8")
    text = f.read()
    print(text)
    f.close()

def read02():
    # 파일 읽기 : 줄 단위(\n)으로 읽기
    f = open("./sample/sangbuk.csv", "rt", encoding="utf-8")
    print(f.readline().replace("\n", ""))
    while True:
        line = f.readline() # 읽어올 데이터 없으면 "" -> false
        if not line: # 비어 있으면
            break
        print(line)
    f.close()

def read03():
    # 한번에 읽어와서 줄 단위로 리스트 생성:readlines
    f = open("./sample/sangbuk.csv", "rt", encoding="utf-8")
    lines = f.readlines()
    print("lines:", type(lines))


    # list니까 순회가 가능
    for index, line in enumerate(lines):
        print("{}번째 line: {}".format(index, line))

    f.close()

def safe_open():
    # 파일 등 시스템 자원을 열어 줬으면 반드시 닫아줘야 하는데
    # with ~ as 를 사용하면 해당 블록이 끝났을 때
    # 자동으로 close
    with open("./sample/test.txt", "rt", encoding="utf-8") as f:
        print(f.read())
        # close 해주지 않아도 됨


# pickle의 사용
# python 객체의 직렬화 - 역직렬화를 위한 모듈
# 프로토콜 버전이 있고, 필요할 경우 특정 프로토콜 버전을 이용해 저장할 수 있다
# 파일 저장 기능은 없고, 직렬화 역직렬화에 대한 기능만 가지고 있다
# pickle 모듈을 import
import pickle

def pickle_dump():
    # 직렬화 :dump
    # 사전 객체를 생성 -> 직렬화
    with open("./sample/players.bin", "wb") as f: # 반드시 binary 모드여야 한다
        data = {"baseball": 9}
        pickle.dump(data, f)
        # 필요할 시는 3번쨰 인자로 pickle protocol의 버전을 명시


def pickle_load():
    # 역직렬화 : load
    # load의 경우, dump시 프로토콜 버전을 명시했어도
    # load시에는 명시할 필요 없음
    print(" 현재의 pickle pritocol:", pickle.HIGHEST_PROTOCOL)
    # players.bin에서 pickle 객체 역직렬화
    with open("./sample/players.bin", "rb") as f:
        data = pickle.load(f)
        print(data, type(data))


def pickle_dump_multi():
    # 복수 객체의 직렬화
    with open("./sample/players.bin", "wb") as f:
        pickle.dump({"baseball" :9}, f)
        pickle.dump({"soccer" : 11}, f, 1) # 하위 호환을 위한 버전 변경
        pickle.dump({"basketball": 5}, f, pickle.HIGHEST_PROTOCOL)


def pickle_load_multi():
    # 복수 객체의 역직렬화
    with open("./sample/players.bin", "rb") as f:
        # print(pickle_load(f))
        # print(pickle_load(f))
        # print(pickle_load(f))

        while True:
            try:
                print(pickle.load(f))
            except EOFError:
                print("더이상 역직렬화 할 객체 없음")
                break


def example():
    # sangbuk.csv -> 불러와서 dict의 list 생성
    # pickle로 저장
    players =[]

    with open("./sample/sangbuk.csv", "rt", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            # print("member:", line)
            lst = line.replace("\n", "").replace(" ", "").split(",")
            # print("lst:", lst)
            player = {
                "name": lst[0],
                "back": lst[1],
                "height": lst[2],
                "position": lst[3]
            }
            players.append(player) # 리스트에 적재
    print("선수 명단:", players)

    # pickle로 객체 저장
    with open("./sample/sangbuk.pickle", "wb") as f:
        pickle.dump(players,f)
    del players

    # sangbuk.pickle로부터 역직렬화 players 적재
    with open("./sample/sangbuk.pickle", "rb") as f:
        players = pickle.load(f)
    print("복원된 선수 목록:", players)


if __name__ == "__main__":
    # write01()
    # write02()
    # copy_binary()
    # read01()
    # read02()
    # read03()
    # safe_open()
    # pickle_dump()
    # pickle_load()
    # pickle_dump_multi()
    # pickle_load_multi()
    example()


































