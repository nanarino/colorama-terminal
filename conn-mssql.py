from colorama_terminal import _print, Colormsg
import pymssql

DATABASES = {
    "host": '192.168.10.1\\***',
    "user": "sa",
    "database": "******",
    "password": "***********",
    "autocommit": True,
    "as_dict" : True
}

with pymssql.connect(**DATABASES) as conn:
    with conn.cursor() as cur:
        while 1:
            if (sql := input('>>> ')) == 'q':
                exit()
            try:
                cur.execute(sql)
                qs = cur.fetchall()
                for row in qs:
                    _print(row)
                    print("")
                print(f"结果集共计{len(qs)}行")
            except Exception as e:
                print("Traceback (most recent call last):")
                _print(e)