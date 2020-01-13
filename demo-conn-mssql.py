from colorama_terminal import _print, Colormsg
import pymssql

DATABASES = {
    'default':{
        "host": '192.168.10.1\\***',
        "user": "sa",
        "database": "******",
        "password": "***********"
    }  #"as_dict" = False
}

def _conn_create(name='default'):
    conn = pymssql.connect(**DATABASES[name])
    cursor = conn.cursor()
    if not cursor:
        raise Exception("数据库连接失败")
    else:
        _print(Colormsg("*" * 32 + "数据库连接成功" + "*" * 32, 'MAGENTA'))
    return (cursor,conn)

_cur, _conn = _conn_create()

def execute(sql):
    _cur.execute(sql)

#修改数据后提交事务
def commit():
    _conn.commit()

#调用存储过程，第一个参数是存储过程名字，存储过程的参数依次后跟。
def callproc(proc_name,*args):
    _cur.callproc(proc_name,args)

def query(sql):
    execute(sql)
    querylist = _cur.fetchall()
    for i in querylist:
        _print(i)
    return Colormsg("%d行受影响"%len(querylist), 'GREEN')

def close(isExit = True):
    try:
        _conn.close()
    except Exception as e:
        _print(e)
    else:
        isExit and exit()
        return Colormsg("游标收回成功，数据库连接已关闭", 'MAGENTA')
    return Colormsg("游标收回异常，数据库连接无法关闭", 'RED')


def query_tables():
    return query("select * from sys.tables")

def query_columns_name(table_name):
    return query("select name from syscolumns where id=(select max(id) from sysobjects where xtype='u' and name=\'"+ table_name +"\')")

#查询所有存储过程
def query_procedures():
    return query("""
select Pr_Name as [存储过程], [参数]=stuff((select '，'+[Parameter]
from (
select Pr.Name as Pr_Name,parameter.name +' ' +Type.Name + ' ('+convert(varchar(32),parameter.max_length)+')' as Parameter
from sys.procedures Pr left join
sys.parameters parameter on Pr.object_id = parameter.object_id
inner join sys.types Type on parameter.system_type_id = Type.system_type_id
where type = 'P'
) t where Pr_Name=tb.Pr_Name for xml path('')), 1, 1, '')
from (
select Pr.Name as Pr_Name,parameter.name +' ' +Type.Name + ' ('+convert(varchar(32),parameter.max_length)+')' as Parameter
from sys.procedures Pr left join
sys.parameters parameter on Pr.object_id = parameter.object_id
inner join sys.types Type on parameter.system_type_id = Type.system_type_id
where type = 'P'
)tb
where Pr_Name not like 'sp_%' --and Pr_Name not like 'dt%'
group by Pr_Name
order by Pr_Name
""")

#查询存储过程内容
def query_procedure_text(proc_name):
    return query("SELECT TEXT FROM syscomments WHERE id = object_id(\'" + proc_name + "\')")


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