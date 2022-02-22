# Python
import traceback
from psycopg2 import pool
from psycopg2.extras import RealDictCursor
import sys

# FastAPI
from fastapi.logger import logger as log

class Connection():
    _PARAMS = {
        'host':'localhost',
        'database':'fastapi_twitter',
        'user':'daniel',
        'password':'caamal',
        'port':'5432'
    }
    _MIN_CONN = 1
    _MAX_CONN = 2
    _pool = None
    
    @classmethod
    def get_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CONN, cls._MAX_CONN, **cls._PARAMS)
                log.debug('Connection with pool successfully.')
                return cls._pool
            except Exception as e:
                log.error('Something went wrong with the connection to the pool: {}'.format(e))
                sys.exit()
        else:
            return cls._pool
    
    @classmethod
    def get_connection(cls):
        try:
            conn = cls.get_pool().getconn()
            log.debug('Connection successfully.')
            return conn
        except Exception as e:
            try:
                cls.close_connections()
            except:
                pass
            log.error('Something went wrong with the connection to the pool: {}'.format(e))
            sys.exit()
    
    @classmethod
    def release_connection(cls, conn):
        try:
            cls.get_pool().putconn(conn)
            log.debug('Connections released.')
        except Exception as e:
            log.error('Something went wrong during the released of the connection: {}'.format(e))
            try:
                cls.close_connections()
            except:
                pass
            sys.exit()
    
    @classmethod
    def close_connections(cls):
        try:
            cls.get_pool().closeall()
        except Exception as e:
            log.error('Something went wrong during the released all connections: {}'.format(e))


class PoolCursor():
    _conn = None
    _cursor = None

    def __init__(self):
        pass

    def __enter__(self):
        self._conn = Connection.get_connection()
        self._cursor = self._conn.cursor(cursor_factory=RealDictCursor)
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tcb):
        if exc_val:
            self._conn.rollback()
            log.error('Something wrong went happened: \n{}'.format(traceback.format_exc()))
        self._conn.commit()
        Connection.release_connection(self._conn)