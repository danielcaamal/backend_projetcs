from psycopg2 import connect
from psycopg2.extras import RealDictCursor

if __name__ == '__main__':
    params = {
        'host':'localhost',
        'database':'fastapi_twitter',
        'user':'daniel',
        'password':'caamal',
        'port':'5432'
    }
    conn = connect( **params)# cursor_factory=RealDictCursor)
    with conn:
        with conn.cursor() as cursor:
            query = 'SELECT version();'
            cursor.execute(query)
            print(cursor.fetchall())