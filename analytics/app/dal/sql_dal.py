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


def count_signal_type():
    query = '''SELECT 
                signal_type,
                count(*) as count
                FROM intel_signals
                GROUP BY signal_type
                ORDER BY count DESC'''
    cursor = conn.cursor()
    cursor.execute(query)
    value = cursor.fetchall()
    logger.info("result", value)
    cursor.close()

    return value


def detecting_sensitive_targets():
    query = '''SELECT 
                s.entity_id,
                count(*) as reports_count
                FROM intel_signals s
                JOIN targets t
                    ON s.entity_id = t.entity_id
                WHERE priority_level = 99
                GROUP BY s.entity_id
                ORDER BY reports_count DESC
                LIMIT 3'''
    cursor = conn.cursor()
    cursor.execute(query)
    value = cursor.fetchall()
    logger.info("result", value)
    cursor.close()

    return value