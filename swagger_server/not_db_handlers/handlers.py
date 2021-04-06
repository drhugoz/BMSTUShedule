import datetime
import json
from datetime import datetime

def GetWeekNum(date):
    if date == None:
        dt_date = datetime.today()
    else:
        date = str(date)
        datelist = list(date)
        for i in range(0, len(datelist)):
            if datelist[i] == ".":
                datelist[i] = " "
        date = "".join(datelist)
        dt_date = datetime.strptime(date, '%d %m %Y')
    week_number = dt_date.isocalendar()[1]
    
    if dt_date.month <= 6:
        base_num = datetime.strptime("06 02 " + str(dt_date.year), '%d %m %Y')
    else:
        base_num = datetime.strptime("01 09 " + str(dt_date.year), '%d %m %Y')
        
    base_num = base_num.isocalendar()[1]  
    week_number -= base_num - 1
    
    if week_number % 2 == 0:
        week_type = "even"
    else:
        week_type = "odd"
    
    week_res = {"num" : week_number, "type" : week_type}
    
    return json.dumps(week_res, indent = 4, ensure_ascii = False)
