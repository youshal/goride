import databases
import sqlalchemy

DATABASE_URL = "postgresql://goride_usr:goride@localhost/goride"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DATABASE_URL,
)
metadata.create_all(engine)