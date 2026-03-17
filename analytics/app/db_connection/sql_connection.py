import mysql.connector
import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

host = os.getenv("MYSQL_HOST")
port = int(os.getenv("MYSQL_PORT", 3306))
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DB")


class DataBase:
    
    @staticmethod
    def get_connection():
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
