import sqlite3

con = sqlite3.connect("FasFod.db", check_same_thread=False)
cur = con.cursor()

def get_main(id=None):
    sql = "select * from FasFod  "
    if id:
        sql +=f"where id={id}"

    cur.execute(sql)
    if id:
        result = cur.fetchone()
    else:
        result = cur.fetchall()

    return result



