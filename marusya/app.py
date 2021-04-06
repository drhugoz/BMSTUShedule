from flask import Flask
#from werkzeug.contrib.fixers import ProxyFix

import requests
import flask
import json
import dialogflow_v2 as dialogflow
import os
import datetime
import random

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./baumanschedule-dlld-7e617118139b.json"

app = Flask(__name__)

SINGLE_IMAGE_ID = 457239018
MULTI_IMAGE_IDS = [457239018, 457239019, 457239020]

CHATBOT_URL = 'http://chatbot:5005/webhooks/rest/webhook'
BASE_API = 'http://api:4040//RyazMax/BaumanBotApi/1.0.0'

PORT = 2281

df_client = dialogflow.SessionsClient()
project_id = "baumanschedule-dlld"

def default_func(query):
    return query.fulfillment_text

def get_week(query):
    types = {'odd': 'числитель', 'even': 'знаменатель'}

    date = query.parameters["date-time"]
    if date == "" or type(date) != str:
        date = datetime.datetime.now()
    else:
        date = datetime.datetime.strptime(date.split('T')[0], "%Y-%m-%d")

    resp = requests.get(BASE_API + f'/week?date={date.day}.{date.month}.{date.year}')
    obj = json.loads(resp.json())

    num, t  = obj["num"], obj["type"]

    return query.fulfillment_text.format(num=num, type=types[t])

aud_table = {
    "гз": [['512ю', '122'], ['122'], ['419', '395'], ['505'], ['618', '412'], ['345']],
    "улк": [[random.randint(100, 600) for i in range(random.randint(2, 4))] for j in range(5)],
    "СМ": [[random.randint(100, 600) for i in range(random.randint(2, 4))] for j in range(5)],
    "энерго": [[random.randint(100, 600) for i in range(random.randint(2, 4))] for j in range(5)],
    "мт": [[random.randint(100, 600) for i in range(random.randint(2, 4))] for j in range(5)],
}


def get_free_aud(query):
    if not query.all_required_params_present:
        return query.fulfillment_text

    date = query.parameters["date-time"]
    if date == "" or type(date) != str:
        date = datetime.datetime.now()
    else:
        date = datetime.datetime.strptime(date.split('T')[0], "%Y-%m-%d")
    
    campus = query.parameters["campus_name"]
    number = query.parameters["number"] or 3

    if not campus in aud_table:
        return "Извини, я не нашла такого корпуса " + campus
    if number > len(aud_table[campus]) or number < 1:
        return f"Попробуй пару по меньше. В {campus} проходит только {len(aud_table[campus])} пар"

    return query.fulfillment_text.format(aud=random.choice(aud_table[campus][number]))

subjects = [
    'ООП ', 'Линейная алгебра', 'Программирование', 'Сопротивление материалов', 
    'Теоретическая механика', 'Физика', 'Элективный курс по физической культуре', 'Философия',
    'Теория вероятностей', 'Математическая статистика', 'Аналитическая геометрия', 'Инженерная графика',
    'Операционные системы', 'Детали машин', 'Правоведение', 'Web-технологии', 'Тестирование ПО',
    'Квантовая физика', 'Иностранный язык']

def groups():
    groups = {}
    for i in range(4):
        for j in range(0, random.randint(2, 3)):
            groups[str(i+1) + str(j+1)] = week_sched()
    return groups

def week_sched():
    res = []
    for i in range(6):
        res.append([random.choice(subjects) for j in range(0, random.randint(2, 4))])
    return res

facul_prefix = ['иу', 'рл', 'рк', "бмт", "имб", "э", "мт", "л", "см"]
faculties = [prefix + str(i) for i in range(1, 9) for prefix in facul_prefix]
u_groups = {faculty: groups() for faculty in faculties}

import json
with open('test.json', 'w') as fout:
    json.dump(u_groups, fout)

def get_group_sched(query):
    if not query.all_required_params_present:
        return query.fulfillment_text

    date = query.parameters["date-time"]
    print("DATE", date)
    try:
        if type(date) != str:
            date = date[0]
    except:
        pass
    if date == "" or type(date) != str:
        date = datetime.datetime.now()
    else:
        date = datetime.datetime.strptime(date.split('T')[0], "%Y-%m-%d")
    print(date)
    faculty = query.parameters["faculty"]
    number = int(query.parameters["number"])

    weekday = date.weekday()
    if weekday == 6:
        return "Эх, везет этим людям у них выходной"
        
    #string = "\n".join([f"{i + 1}я пара - {subj}" for i, subj in enumerate(u_groups[faculty][str(number)][weekday])])
    full_name = faculty + '-' + str(number) + 'Б'
    print(full_name)
    obj = requests.get(BASE_API + f'/group?name={full_name.upper()}')
    if obj.status_code != 200:
        return f"Я не нашла расписание группы {full_name.upper()}."
    obj = json.loads(obj.json())
    day = obj[weekday]
    # todo chisl znam check
    lections = []
    for item in day:
        if item['oddweek']['name'] != '':
            lections.append(item['oddweek']['name'])
    
    return query.fulfillment_text.format(sched=','.join(lections))

doctors = {
    "стоматолог": "Водзинская Татьяна Владимировна",
    "терапевт": "Алексеева Людмила Анатольевна",
    "хирург": "Гладская Марина Владимировна",
    "невролог": "Щиголь Богдан Игоревич",
    "кардиолог": "Волков Дмитрий Александрович",
}

def get_doctor(query):
    if not query.all_required_params_present:
        return query.fulfillment_text

    spec = query.parameters["doctor"]
    fio = doctors.get(spec)
    if fio is None:
        return f"Я не нашла такого врача - {spec}"
    return f'{spec} {fio} не принимает на этой неделе, попробуй позднее, расписание обновляется каждый день.'


action_to_func = {
    "get_week": get_week,
    "get_free_aud": get_free_aud,
    "get_group_schedule": get_group_sched,
    "get_doctor": get_doctor,
}

def proxy_to_chatboot(data):
    user_id = data['session']['user_id']
    message = data['request']['command']
    session = df_client.session_path(project_id, user_id)
    text_input = dialogflow.types.TextInput(
                text=message, language_code="ru")

    query_input = dialogflow.types.QueryInput(text=text_input)
    response = df_client.detect_intent(
            session=session, query_input=query_input)
    func = action_to_func.get(response.query_result.action, default_func)
    return func(response.query_result)

def create_response_session_object(data):
    return {
        "session_id": data['session']['session_id'],
        "user_id": data['session']['user_id'],
        "message_id":data['session']['message_id'],
    }

def text_response(text, end):
    return {
        "text": text,
        "end_session": end,
    }

def create_button(title, url=None, payload=None):
    return {
        "title": title,
        #"url": url,
        #"payload": payload,
    }

def create_card(image_id):
    if type(image_id) == list:
        return {
            "type": "ItemsList",
            "items": [{"image_id": id} for id in image_id],
        }
    else:
        return {
            "type": "BigImage",
            "image_id": image_id,
        }

def create_response(data):
    req = data['request']
    cmd = req['command']
    if cmd == "привет" or data['session']['new']:
        return text_response("Привет! Это навык расписание МГТУ имени Баумана. Я могу подсказать твое и не только расписание, найти свободные аудитории, а также сказать номер и тип учебной недели. Начнем?", False)
        return text_response("До встречи!", True)
    if cmd == "картинка":
        resp = text_response("Вот так выглядит главное здание МГТУ имени Баумана", False)
        resp["card"] = create_card(SINGLE_IMAGE_ID)
        return resp
    if cmd == "карусель":
        resp = text_response("А это разные корпуса Бауманки", False)
        resp["card"] = create_card(MULTI_IMAGE_IDS)
        return resp
    if cmd == "кнопки":
        resp = text_response("Идешь на пары?", False)
        resp["buttons"] = [create_button("Да"), create_button("Нет")]
        return resp
    

    return text_response(proxy_to_chatboot(data), False)


@app.route('/', methods=['GET', 'POST'])
def main():
    data = flask.request.get_json()
    return {
        "response": create_response(data),
        "session": create_response_session_object(data),
        "version": "1.0",
    }

#app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT, debug=True)