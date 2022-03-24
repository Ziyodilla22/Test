import sqlite3

con = sqlite3.connect("evos.db", check_same_thread=False)
cur = con.cursor()


def get_log(user_id):
    sql = f"select * from log where user_id={user_id}"
    cur.execute(sql)
    return cur.fetchone()


def create_log(user_id):
    a = {'state': 0}
    sql = f"""insert into log values({user_id}, "{a}")"""
    cur.execute(sql)
    con.commit() #soxrnit qiladi

    return get_log(user_id)

def change_log(user_id, log):
    sql = f"""update log set habarlar="{log}" where user_id={user_id}"""
    cur.execute(sql)
    con.commit() #soxrnit qiladi


def get_user(user_id):
    sql = f"select * from user where user_id={user_id}"
    cur.execute(sql)
    return cur.fetchone()


def add_user(user_id, log):
    ism = log.get('ism', '')
    familiya = log.get('familiya', '')
    raqam = log.get('raqam', '')


    sql = f"insert into user values({user_id}, '{ism}', '{familiya}', '{raqam}')"
    cur.execute(sql)
    con.commit()

def clear_log(user_id, state): #tablitsani tozalab beradi
    log = {'state': state}
    sql = f"""update log set habarlar="{log}" where user_id={user_id}"""
    cur.execute(sql)
    con.commit()  # soxrnit qiladi

def get_kategiriya():
    sql = "select * from kategoriya"
    cur.execute(sql)
    return cur.fetchall()


def get_product(nomi=None, ctg=None):
    if nomi:
        sql = f"""
        SELECT * from product
        WHERE nomi = "{nomi}"
        """
        return cur.execute(sql).fetchone()
    elif ctg:
        sql = f"""  
        SELECT product.id, product.nomi, product.tarkibi, product.narxi, ctg.nomi, ctg.slag FROM product
        inner join kategoriya ctg on ctg.id = product.ctg
        WHERE ctg.nomi = '{ctg}'
        """
        return cur.execute(sql).fetchall()



