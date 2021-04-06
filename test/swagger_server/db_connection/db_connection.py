import psycopg2
import json
import os.path
from datetime import datetime
from swagger_server.db_connection.queries import temp_db

weekdays = {"пн" : 0, "вт" : 1, "ср" : 2, "чт" : 3, "пт" : 4, "сб" : 5,
            "ПН" : 0, "ВТ" : 1, "СР" : 2, "ЧТ" : 3, "ПТ" : 4, "СБ" : 5}
weektypes = {"ЧС" : 1, "ЗН" : 2,
             "чс" : 1, "зн" : 2}
pairs = [[10, 5], [11, 50], [13, 35], [15, 25], [17, 15], [19, 0],[20, 45]]

def CreateConnection():
    f = open('condata.txt')
    params = f.readline().split(' ')
    f.close()
    
    return psycopg2.connect(
    database = params[0],
    user = params[1],
    password = params[2],
    host = params[3],
    port = params[4])


def MakeQuery(con, query, args=()):
    cur = con.cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.close()
    return r

def FillSchedule(day, empty_slot):
    if len(day) == 0:
        for i in range(0, 7):
            day.append(empty_slot)
        return
    
    j = 0
    while (j < 7):
        if day[j]["number"] != j:
            day.insert(j, empty_slot)
        elif j == (len(day) - 1):
            while (j < 6):
                j += 1
                day.insert(j, empty_slot)
        j += 1

def CurrentWeekType():
    dt_date = datetime.today()
    week_number = dt_date.isocalendar()[1]
    
    if dt_date.month <= 6:
        base_num = datetime.strptime("06 02 " + str(dt_date.year), '%d %m %Y')
    else:
        base_num = datetime.strptime("01 09 " + str(dt_date.year), '%d %m %Y')
        
    base_num = base_num.isocalendar()[1]  
    week_number -= base_num - 1
    
    if week_number % 2 == 0:
        return 2
    else:
        return 1

def CheckGroup(name):
    con = CreateConnection()
    base_query = "SELECT * " \
                 "FROM \"group\" " \
                 "WHERE \"group\".name = " + name
    return bool(MakeQuery(con, base_query, ()))

def CheckProfessor(name):
    con = CreateConnection()
    base_query = "SELECT * " \
                 "FROM professor " \
                 "WHERE professor.name = " + name
    return bool(MakeQuery(con, base_query, ()))

def GetWeek(base_query, name):
    con = CreateConnection()
    cur = con.cursor()
    cur.execute(temp_db)
    #cur.execute(open(os.path.dirname(__file__) + "/../../sql/group_temp_db.sql", "r").read())

    empty_slot = {"from" : "",
                  "name" : "",
                  "location" : "",
                  "to" : "",
                  }
    day_set = []
    for i in range(0, 6):
        query_string = base_query % (name, i, 1)
        query_odd = MakeQuery(con, query_string, ())
        
        query_string = base_query % (name, i, 2)
        query_even = MakeQuery(con, query_string, ())
        
        slot_set = []
        FillSchedule(query_odd, empty_slot)
        FillSchedule(query_even, empty_slot)
        for j in range(0, 7):
            if "number" in query_odd[j]:
                del query_odd[j]["number"]
            if "number" in query_even[j]:
                del query_even[j]["number"]
            slot_set.append({"oddweek" : query_odd[j], "evenweek" : query_even[j]})
        day_set.append(slot_set)
        
    cur.execute("DROP TABLE GroupTempTable;")
    con.close()
    
    return day_set

def GetGroupWeek(group_name):
    if not CheckGroup(group_name):
        return None
    base_query = "SELECT SubjectName AS \"name\", " \
                          "BeginningTime AS \"from\", " \
                          "EndingTime AS \"to\", " \
                          "AudName AS \"location\", " \
                          "number, " \
                          "ProfName AS \"professor\" " \
                          "FROM GroupTempTable " \
                          "WHERE GroupName = %s AND " \
                          "weekday = %d AND " \
                          "(repeat_type = 0 OR repeat_type = %d) " \
                          "ORDER BY weekday;"
    return json.dumps(GetWeek(base_query, group_name), indent = 4, ensure_ascii = False)
    

def GetProfWeek(prof_name):
    if not CheckProfessor(prof_name):
        return None
    base_query = "SELECT SubjectName AS \"name\", " \
                          "BeginningTime AS \"from\", " \
                          "EndingTime AS \"to\", " \
                          "AudName AS \"location\", " \
                          "number, " \
                          "ProfName AS \"professor\" " \
                          "FROM GroupTempTable " \
                          "WHERE ProfName = %s AND " \
                          "weekday = %d AND " \
                          "(repeat_type = 0 OR repeat_type = %d) " \
                          "ORDER BY weekday;"
    week = {"name" : prof_name, "schedule" : GetWeek(base_query, prof_name)}
    return json.dumps(week, indent = 4, ensure_ascii = False)

def GetAud(location, weektype, weekday, pairnum):
    con = CreateConnection()
    base_query = "SELECT auditorium.name AS \"number\", building.name AS \"location\" " \
                 "FROM auditorium JOIN building ON building_id = building.id " \
                 "WHERE auditorium.name != 'Каф' AND auditorium.name != 'СК' AND " \
                 "auditorium.name != 'Лекторий' AND auditorium.name != ''"
    if location != None:
        base_query += " AND building.name = " + "'" + location + "'"
    base_query += " AND auditorium.id NOT IN " \
                  "(SELECT auditorium.id " \
                  "FROM lesson_auditorium JOIN lesson ON lesson.id = lesson_auditorium.lesson_id " \
                  "JOIN auditorium ON auditorium_id = auditorium.id " \
                  "WHERE \"number\" = %s AND lesson.weekday = %d AND " \
                  "(lesson.repeat_type = 0 OR lesson.repeat_type = %d));"
    if weekday == None:
        weekday = datetime.today().weekday()
    else:
        weekday = weekdays[weekday]

    if weektype == None:
        weektype = CurrentWeekType()
    else:
        weektype = weektypes[weektype]

    if pairnum == None:
        now = datetime.now()
        for i in range(0, 7):
            pair_end = now.replace(hour = pairs[i][0], minute = pairs[i][1], second=0, microsecond=0)
            if now < pair_end:
                pairnum = i
                break
        if pairnum == None:
            return None
    
    query_string = base_query % (pairnum, weekday, weektype)
    query_res = MakeQuery(con, query_string, ())
    con.close()

    if not bool(query_res):
        return None
    
    return json.dumps(query_res, indent = 4, ensure_ascii = False)

def GetDoctor(con, name, aud, spec):
    flag = False
    base_query = "SELECT doctor.name, doctor.spec, doctor.office AS aud " \
                 "FROM doctor"
    if (name != None or aud != None or spec != None):
        base_query += " WHERE "
        if (name != None):
            base_query += "doctor.name = " + "'" + name + "'"
            flag = True
        if (aud != None):
            if (flag):
                base_query += " AND doctor.office = " + "'" + aud + "'"
            else:
                base_query += "doctor.office = " + "'" + aud + "'"
                flag = True
        if (spec != None):
            if (flag):
                base_query += " AND doctor.spec = " + "'" + spec + "'"
            else:
                base_query += "doctor.spec = " + "'" + spec + "'"
    return MakeQuery(con, base_query, ())

def GetDoctorSchedule(con, name):
    base_query = "SELECT doctor_schedule.date, doctor_schedule.time " \
                 "FROM doctor JOIN doctor_schedule ON doctor.id = doctor_schedule.doctor_id " \
                 "WHERE doctor.name = " + name
    return MakeQuery(con, base_query, ())
    
def GetDocAll(name, aud, spec):
    con = CreateConnection()
    doc = GetDoctor(con, name, aud, spec)
    if not bool(doc):
        con.close()
        return None
    schedule = []
    for i in range(0, len(doc)):
        schedule.append({"name" : doc[i]["name"],
                         "aud" : doc[i]["aud"],
                         "spec" : doc[i]["spec"],
                         "schedule" : GetDoctorSchedule(con, "'" + doc[i]["name"] + "'")})
    con.close()

    return json.dumps(schedule, indent = 4, ensure_ascii = False)

def UpdateDoctorsTime(name, date, time):
    con = CreateConnection()
    cur = con.cursor()
    select_query = "SELECT id into id_name " \
                   "FROM doctor " \
                   "WHERE doctor.name = '" + name + "';\n"
    update_query = "UPDATE doctor_schedule " \
                   "SET time = '" + time + "' " \
                   "FROM id_name " \
                   "WHERE doctor_id = id_name.id AND date = '" + date + "';\n"
    
    cur.execute(select_query)
    cur.execute("SELECT * FROM id_name")
    if cur.rowcount == 0:
        return False

    cur.execute(update_query)
    if cur.rowcount == 0:
        return False

    cur.execute("DROP TABLE id_name;")

    return True
