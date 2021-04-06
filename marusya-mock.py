import requests

#webhook = input('Webhook:')
webhook = 'http://localhost:5555'
obj = {
    "request":{
        "command":"f"
    },
    "session":{
        "session_id":"935a82fe-5a3a-455d-8619-5e33a7b691f9",
        "user_id":"83aa98a4cf81ec2c013883b79b33e8a7fb53becd040227c447907ee6e47ec735",
        "skill_id":"bf29f092-d112-4f10-8895-6b099d22b10f",
        "new":False,
        "message_id":0,
    },
    "state":{
        "session":{},
        "user":{},
    },
    "version":"1.0"
}

while True:
    msg = input('>>')
    obj['request']['command'] = msg
    resp = requests.post(webhook, json=obj)
    print(resp.json()['response']['text'])