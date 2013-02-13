def FetchOneAssoc(cursor) :
	data = cursor.fetchone()
	if data == None :
		return None
	desc = cursor.description

	dict = {}

	for (name, value) in zip(desc, data) :
		dict[name[0]] = value

	return dict

def GetSQL_arr(cursor) :
	rows = []
	while (1):
		row = FetchOneAssoc(cursor)
		if row == None:
			break
		rows.append(row)

	return rows

def sample_connect():
	
	import MySQLdb
	conn = MySQLdb.connect (host = "localhost",
						user = "root",
						passwd = "",
						db = "dbname")
	cursor = conn.cursor ()
	sql = "SELECT id, field1, field2 FROM table WHERE field1 = 1"
	cursor.execute (sql)

	rows = GetSQL_arr(cursor)

	cursor.close ()
	conn.close ()