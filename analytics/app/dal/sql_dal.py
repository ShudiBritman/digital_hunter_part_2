from app.db_connection.sql_connection import DataBase
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

conn = DataBase.get_connection()

def high_priority_moved_targets():
    query = '''SELECT 
                entity_id,
                target_name,
                priority_level
                FROM targets
                WHERE priority_level IN (1, 2)
                AND movement_distance_km > 5'''
    cursor = conn.cursor()
    cursor.execute(query)
    value = cursor.fetchall()
    logger.info("result", value)
    cursor.close()

    return value
