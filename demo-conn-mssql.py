from colorama_terminal import _print, Colormsg
import pymssql

DATABASES = {
    'default':{
        "host": '192.168.10.1\\***',
        "user": "sa",
        "database": "******",
        "password": "***********"
    },
}

def conn_create(name='default'):
    conn = pymssql.connect( **DATABASES['default'])
    cursor = conn.cursor()
    if not cursor:
        raise Exception("数据库连接失败")
    else:
        _print(Colormsg("*" * 32 + "数据库连接成功" + "*" * 32, 'MAGENTA'))
    return (cursor,conn)

cur, conn = conn_create()

def _query(sql):
    cur.execute(sql)
    querylist = cur.fetchall()
    for i in querylist:
        _print(i)
    return Colormsg("%d行受影响"%len(querylist), 'GREEN')

#输入_query("select TOP 2 RfbillNo, RfRuleID, * from GSPInDt")

'''
conn.commit() #修改数据后提交事务
'''
if __name__ == "__main__":
    while 1:
        ex = input('>>> ')
        try:
            try:
                _print(eval(ex))
            except SyntaxError as e:
                exec(ex)
        except Exception as e:
            print("Traceback (most recent call last):")
            _print(e)