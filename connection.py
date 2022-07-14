import cx_Oracle
import sett
# import psycopg2,cx_Oracle


# class con_postgre():
# 	def connection():
# 		psycopg2.connect(user="postgres", password="123",  host="localhost", port="5432", database="db_mos")

# class con_dummy():
# 	def connection():
# 	    dsn_tns = cx_Oracle.makedsn('10.234.152.2', '4747', 'IRISHO')
# 	    conn = cx_Oracle.connect(user='NMS', password='NMSTORE', dsn=dsn_tns)
# 	    return conn

class con_dummy():
	def connection():
	    dsn_tns = cx_Oracle.makedsn(sett.DBhost, sett.DBport, sett.DBdatabase)
	    conn = cx_Oracle.connect(sett.DBuser, sett.DBpassword, dsn=dsn_tns)
	    return conn  

