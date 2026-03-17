from app.db_connection.sql_connection import DataBase


conn = DataBase.get_connection()

def high_priority_moved_targets():
    query = '''SELECT 
                entity_id,
                target_name,
                priority_level
                FROM targets
                WHERE priority IN (1, 2)'''
    cursor = conn.cursor()
    cursor.execute()
    value = cursor.fetchall()

    cursor.close()

    return value
