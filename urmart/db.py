import pymysql
db_config = {}
db_config['db_host'] = 'localhost'
db_config['db_port'] = 3306
db_config['db_user'] = 'urmart'
db_config['db_passwd'] = 'urmartaaa'
db_config['db_database'] = 'urmart'

def exec_sql_with_commit(sql):
    conn = pymysql.connect(host=db_config['db_host'], port=db_config['db_port'], user=db_config['db_user'],
                           passwd=db_config['db_passwd'], db=db_config['db_database'])
    cur = conn.cursor()
    last_insert = 0
    try:
        cur.execute(sql)
        cur.fetchall()
        last_insert = conn.insert_id()
        conn.commit()
    except:
        conn.rollback()
    finally:
        cur.close()
        conn.close()
    return last_insert

def exec_sql(sql):
    conn = pymysql.connect(host=db_config['db_host'], port=db_config['db_port'], user=db_config['db_user'],
                           passwd=db_config['db_passwd'], db=db_config['db_database'])
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result


def exec_sql_with_header(sql):
    conn = pymysql.connect(host=db_config['db_host'], port=db_config['db_port'], user=db_config['db_user'],
                           passwd=db_config['db_passwd'], db=db_config['db_database'])
    cur = conn.cursor()
    cur.execute(sql)
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    cur.close()
    conn.close()

    temp_out = []
    for result in rv:
        temp_out.append(dict(zip(row_headers, result)))
    return temp_out
