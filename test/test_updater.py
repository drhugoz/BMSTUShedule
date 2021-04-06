import json
from swagger_server.db_connection import db_connection
from aud_builder import AudBuilder

f = open("data/aud_res_1.txt", 'w', encoding="utf-8")
r = db_connection.GetAud("ГЗ", "чс", "пн", "1")
f.write(r)
f.close()

f = open("data/aud_res_2.txt", 'w', encoding="utf-8")
r = db_connection.GetAud(None, "чс", "пн", "1")
f.write(r)
f.close()

f = open("data/aud_res_3.txt", 'w', encoding="utf-8")
r = db_connection.GetAud("ГЗ", None, "пн", "1")
f.write(r)
f.close()

f = open("data/aud_res_4.txt", 'w', encoding="utf-8")
r = db_connection.GetAud("ГЗ", "чс", None, "1")
f.write(r)
f.close()

f = open("data/aud_res_5.txt", 'w', encoding="utf-8")
r = db_connection.GetAud(None, None, None, "1")
f.write(r)
f.close()