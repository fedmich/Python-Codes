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
