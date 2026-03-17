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
    cursor.close()

    return value


def detecting_sensitive_targets():
    query = '''SELECT 
                s.entity_id,
                count(*) as reports_count
                FROM intel_signals s
                WHERE s.priority_level = 99
                GROUP BY s.entity_id
                ORDER BY reports_count DESC
                LIMIT 3'''
    cursor = conn.cursor()
    cursor.execute(query)
    value = cursor.fetchall()
    cursor.close()

    return value


def get_target_location_by_day(entity_id):
    conn = DataBase.get_connection()
    cursor = conn.cursor()
    query = '''SELECT
                reported_lon,
                reported_lat
                FROM intel_signals
                WHERE entity_id = %s
                ORDER BY timestamp'''
    cursor.execute(query, (entity_id,))
    result = cursor.fetchall()
    cursor.close
    conn.close()

    return result


def find_active_after_dormant():
    query = '''WITH first_half as (
                SELECT
                    entity_id,
                    DATE(`timestamp`) as day,
                    sum(distance_from_last) as sum
                    FROM intel_signal
                    WHERE TIME(`timestamp`) BETEWEEN
                    "08:00:00" AND "19:59:59"
                    GROUP BY entity_id, day),
                second_half as (
                    SELECT entity_id,
                    DATE(`timestamp`) as day,
                    SUM(distance_from_last)
                    FROM intel_signal
                    WHERE TIME(`timestamp`) BETWEEN
                    "20:00:00" AND "07:59:59"
                    GROUP BY entity_id, day
                      )
                      
                    SELECT
                        fh.entity_id,
                        fh.day,
                        fh.sum,
                        sh.entity_id,
                        sh.day,
                        sh.sum
                    FROM first_half fh
                    JOIN second_half sh
                        ON fh.entity_id = sh.entity_id
                        AND fh.day = sh.day
                    WHERE fh.sum = 0
                    AND sh.sum >= 10
                        '''
    cursor = conn.cursor()
    cursor.execute(query)
    value = cursor.fetchall()
    cursor.close()

    return value
