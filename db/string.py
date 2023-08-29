
from db.mydb import myDB

connection_string= 'postgresql+psycopg2://'+myDB.db_user+':'+myDB.db_password+'@'+myDB.db_host+':'+ myDB.db_port+'/'+ myDB.db_database