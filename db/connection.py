from sqlalchemy import create_engine
from db.string import connection_string
def insert_df_into_db(tablename, df):
    engine = create_engine(connection_string)
    df.to_sql(tablename, engine, if_exists="replace",index=False)
    engine.dispose()


def append_df_into_db(tablename, df):
    engine = create_engine(connection_string)
    df.to_sql(tablename, engine, if_exists="append",index=False)
    engine.dispose()
    