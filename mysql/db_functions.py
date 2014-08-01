import MySQLdb

connection = MySQLdb.connect(host, user, password)
cursor = connection.cursor()

# Create database with named db_name
def create(cursor, db_name):
    return cursor.execute("CREATE DATABASE `%s`" % (db_name))

# Check if database exists
def exists(cursor, db_name):
    sql = "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '%s'" % (db_name)
    return cursor.execute(sql)

def backup_db(db_name):
    # mysqldump db_name > db_name.sql
    system("mysqldump %s > %s.sql" % (db_name, db_name)) 

    # multiple databases
    # mysqldump --databases people places things > nouns.sql

    # all databases
    # mysqldump --all-databases > my_database.sql
    
def restore_db(db_name):
    # mysql db_name < db_name.sql
    system("mysql %s > %s.sql" % (db_name, db_name))

