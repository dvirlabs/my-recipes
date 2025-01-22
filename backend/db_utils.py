import psycopg2
from psycopg2.extras import RealDictCursor


###### General functions ######
def connect_to_db():
    conn = psycopg2.connect(
        host="192.168.10.xxx",
        port="5432",
        database="myrecipes",
        user="postgres",
        password="Aa123456"
    )
    return conn

def close_connection(conn):
    conn.close()
#############################


###### Recipe functions ######
def get_all_recipes():
    try:
        conn = connect_to_db()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM recipes")
        recipes = cur.fetchall()
        close_connection(conn)
        return recipes
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
        close_connection(conn)
        
        
