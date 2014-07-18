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

