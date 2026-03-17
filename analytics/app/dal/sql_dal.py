from db_connection.sql_connection import DataBase


conn = DataBase.get_connection()

def high_priority_moved_targets():
    query = ""
    cursor = conn.cursor()
    cursor.execute()
    value = cursor.fetchall()

    cursor.close()

    return value
