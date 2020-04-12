import pymysql
import sys
import os

class Mysql:
    def connect(self):
        conn = pymysql.connect(host='192.168.35.171', user='root', password='1111', db='ubunto', charset='utf8')
        return conn

    def select(self):
        conn = self.connect()
        db = conn.cursor()

        sql = "select * from mytable limit 10"
        db.execute(sql)
        res = db.fetchall()

        arr = []
        for row in res:
            txt = "이름: {}, 연락처: {}".format(row[1], row[2])
            arr.append(txt)
            print("이름: {}, 연락처: {}".format(row[1], row[2]))

        conn.commit()
        conn.close()

        return arr


if __name__ == "__main__":
    main = Mysql();
    main.select()