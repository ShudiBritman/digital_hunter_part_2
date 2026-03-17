import mysql.connector
import os
import logging
import time


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

host = os.getenv("MYSQL_HOST", "mysql")
port = int(os.getenv("MYSQL_PORT", 3306))
user = os.getenv("MYSQL_USER", "root")
password = os.getenv("MYSQL_ROOT_PASSWORD", "root")
database = os.getenv("MYSQL_DB","digital_hunter")


class DataBase:
    
    @staticmethod
    def get_connection():
        for i in range(10):
            try:
                return mysql.connector.connect(
                    host=host,
                    port=port,
                    user=user,
                    password=password,
                    database=database
                )
            except mysql.connector.Error as err:
                logger.error("Error: %s", err)
            time.sleep(3)
        logger.error("Error DB not available" )
