import json
from swagger_server.db_connection import db_connection
from aud_builder import AudBuilder
import pytest

def TestGetAud():
    print("Тестирование нахождения аудиторий...")
    with open("data/aud_res_1.txt", encoding="utf-8") as json_file:
        right_data = json.load(json_file)
        test_data = json.loads(db_connection.GetAud("ГЗ", "чс", "пн", "1"))
        assert test_data == right_data
        '''
            print("Первый тест НЕ прошел проверку")
        else:
            print("Первый тест прошел проверку")
        '''
    with open("data/aud_res_2.txt", encoding="utf-8") as json_file:
        right_data = json.load(json_file)
        test_data = json.loads(db_connection.GetAud(None, "чс", "пн", "1"))
        assert test_data == right_data
        '''if not test_data == right_data:
            print("Второй тест НЕ прошел проверку")
        else:
            print("Второй тест прошел проверку")
        '''
    with open("data/aud_res_3.txt", encoding="utf-8") as json_file:
        right_data = json.load(json_file)
        test_data = json.loads(db_connection.GetAud("ГЗ", None, "пн", "1"))
        assert test_data == right_data
        '''if not test_data == right_data:
            print("Третий тест НЕ прошел проверку")
        else:
            print("Третий тест прошел проверку")
            '''
    with open("data/aud_res_4.txt", encoding="utf-8") as json_file:
        right_data = json.load(json_file)
        test_data = json.loads(db_connection.GetAud("ГЗ", "чс", None, "1"))
        assert test_data == right_data
        '''if not test_data == right_data:
            print("Четвертый тест НЕ прошел проверку")
        else:
            print("Четвертый тест прошел проверку")
            '''
    with open("data/aud_res_5.txt", encoding="utf-8") as json_file:
        right_data = json.load(json_file)
        test_data = json.loads(db_connection.GetAud(None, None, None, "1"))
        assert test_data == right_data
        '''if not test_data == right_data:
            print("Пятый тест НЕ прошел проверку")
        else:
            print("Пятый тест прошел проверку")
            '''
    print()

def TestGetDoc():
    print("Тестирование нахождения расписания докторов...")
    with open("data/doc_res_1.txt", encoding="utf-8") as json_file:
        right_data = json.load(json_file)
        test_data = json.loads(db_connection.GetDocAll("Волков Дмитрий Александрович", "7", "Кардиология"))
        assert test_data == right_data
        '''if not test_data == right_data:
            print("Первый тест НЕ прошел проверку")
        else:
            print("Первый тест прошел проверку")
            '''
    with open("data/doc_res_2.txt", encoding="utf-8") as json_file:
        right_data = json.load(json_file)
        test_data = json.loads(db_connection.GetDocAll(None, "7", "Кардиология"))
        assert test_data == right_data
        '''if not test_data == right_data:
            print("Второй тест НЕ прошел проверку")
        else:
            print("Второй тест прошел проверку")
            '''
    with open("data/doc_res_3.txt", encoding="utf-8") as json_file:
        right_data = json.load(json_file)
        test_data = json.loads(db_connection.GetDocAll(None, None, "Кардиология"))
        assert test_data == right_data
        '''if not test_data == right_data:
            print("Третий тест НЕ прошел проверку")
        else:
            print("Третий тест прошел проверку")
            '''
    print()

def TestGetGroupWeek():
    print("Тестирование нахождения расписания группы...")
    with open("data/group_res.txt", encoding="utf-8") as json_file:
        right_data = json.load(json_file)
        test_data = json.loads(db_connection.GetGroupWeek("'ИУ7-72Б'"))
        assert test_data == right_data
        assert db_connection.GetGroupWeek("'ИУ12-42Б'") == None
        '''if not test_data == right_data:
            print("Первый тест НЕ прошел проверку")
        else:
            print("Первый тест прошел проверку")
        
        if not db_connection.GetGroupWeek("'ИУ12-42Б'") == None:
            print("Второй тест НЕ прошел проверку")
        else:
            print("Второй тест прошел проверку")'''
    print()

def TestGetProfWeek():
    print("Тестирование нахождения расписания преподаваетля...")
    with open("data/prof_res.txt", encoding="utf-8") as json_file:
        right_data = json.load(json_file)
        test_data = json.loads(db_connection.GetProfWeek("'Рудаков И. В.'"))
        assert test_data == right_data
        assert db_connection.GetProfWeek("'Чапаев В. И.'") == None
        '''if not test_data == right_data:
            print("Первый тест НЕ прошел проверку")
        else:
            print("Первый тест прошел проверку")
        
        if not db_connection.GetProfWeek("'Чапаев В. И.'") == None:
            print("Второй тест НЕ прошел проверку")
        else:
            print("Второй тест прошел проверку")
            '''
    print()

def TestAudBuilder():
    print("Тестирование создания объекта класса \"Aud\"")
    new_aud_1 = AudBuilder().with_number("1337").build()
    new_aud_2 = AudBuilder().with_location("ГЗ").build()
    assert new_aud_1.number and new_aud_2.location
    '''print("Создана аудитория с номером: ", new_aud_1.number)
    print("Создана аудитория с расположением: ", new_aud_2.location)
    '''
    print()

def TestAll():
    print("Тестирование сценариев.\n")
    TestGetAud()
    TestGetDoc()
    TestGetGroupWeek()
    TestGetProfWeek()
    TestAudBuilder()

TestAll()
