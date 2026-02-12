import psycopg2
from psycopg2.extras import RealDictCursor
from config import settings


def get_db_connection():
    """Create and return a database connection."""
    conn = psycopg2.connect(
        host=settings.db_host,
        port=settings.db_port,
        database=settings.db_name,
        user=settings.db_user,
        password=settings.db_password,
        cursor_factory=RealDictCursor
    )
    return conn


def get_datacenters():
    """Fetch all datacenters from the database."""
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT id, name, country, city FROM datacenters ORDER BY id"
            )
            datacenters = cursor.fetchall()
            return [dict(dc) for dc in datacenters]
    finally:
        conn.close()
