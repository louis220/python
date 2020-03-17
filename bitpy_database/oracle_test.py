# oracle 패키지 cx_Oreacle 설치 필요
# conda install cx_Oracle
# pip install cx_Oracle

import cx_Oracle

# connection 맺기
def create_connection():
    # RDBMS의 경우는 연결 정보가 있어야 한다
    dsn = cx_Oracle.makedsn("localhost", 1521, "xe")
    db = cx_Oracle.connect("hr", "hr", dsn)
    return db

def connect_test():
    conn = create_connection()
    cursor = conn.cursor()
    print("CONN:", conn)
    #SQL 실행
    sql = "SELECT * FROM employees"
    cursor.execute(sql)

    #출력
    for row in cursor:
        print("RECORD", row)

    # 커넥션 닫기
    conn.close()

def dict_record():
    # 전달받은 결과는 키와 함께 출력해보고자 한다
    # 변환 필요 -> dict로
    conn= create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT *FROM employees")
    
    # print(cursor.description)
    # desciption정보를 기반으로 레코드를 사전으로 변환
    for row in cursor:
        rowdict = dict(zip([d[0] for d in cursor.description], row))
        print("RECORD:", rowdict)
    conn.close()

if __name__ == "__main__":
    connect_test()