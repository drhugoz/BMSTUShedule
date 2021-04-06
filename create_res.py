from swagger_server.db_connection import db_connection

f = open("group_res.txt", "w")
f.write(db_connection.GetGroupWeek("'ИУ7-72Б'"))
f.close()

db_connection.GetGroupWeek("'ИУ12-42Б'")

f = open("prof_res.txt", "w")
f.write(db_connection.GetProfWeek("'Рудаков И. В.'"))
f.close()

db_connection.GetProfWeek("'Чапаев В. И.'")

f = open("aud_res_1.txt", "w")
f.write(db_connection.GetAud("ГЗ", "чс", "пн", "1"))
f.close()

f = open("aud_res_2.txt", "w")
f.write(db_connection.GetAud(None, "чс", "пн", "1"))
f.close()

f = open("aud_res_3.txt", "w")
f.write(db_connection.GetAud("ГЗ", None, "пн", "1"))
f.close()

f = open("aud_res_4.txt", "w")
f.write(db_connection.GetAud("ГЗ", "чс", None, "1"))
f.close()

f = open("aud_res_5.txt", "w")
f.write(db_connection.GetAud(None, None, None, "1"))
f.close()

f = open("doc_res_1.txt", "w")
f.write(db_connection.GetDocAll("Волков Дмитрий Александрович", "7", "Кардиология"))
f.close()

f = open("doc_res_2.txt", "w")
f.write(db_connection.GetDocAll(None, "7", "Кардиология"))
f.close()

f = open("doc_res_3.txt", "w")
f.write(db_connection.GetDocAll(None, None, "Кардиология"))
f.close()


