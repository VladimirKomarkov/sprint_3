from sqlalchemy import create_engine
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


engine = create_engine("postgresql+psycopg2://owner:password@localhost:5432/jip_project")
connection = engine.connect()
print("Подключение к SQLAlchemy установлено")

connection.close()

connection = psycopg2.connect(user="owner", password="password", dbname="jip_project")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor()

cursor.execute("SELECT 1")
result = cursor.fetchone()
print("Результат запроса с помощью psycopg2:", result)

cursor.close()
connection.close()
print("Соединение с помощью psycopg2 закрыто")