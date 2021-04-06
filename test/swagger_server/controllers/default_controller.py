import connexion
import six

from swagger_server.models.aud import Aud  # noqa: E501
from swagger_server.models.doctor_schedule import DoctorSchedule  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.professor_week import ProfessorWeek  # noqa: E501
from swagger_server.models.week import Week  # noqa: E501
from swagger_server import util
from swagger_server.db_connection import db_connection
from swagger_server.not_db_handlers import handlers
from flask_api import status


def search_audience(location=None, weektype=None, weekday=None, pairnum=None):  # noqa: E501
    """Поиск свободных аудиторий

    Поиск свободных аудиторий  # noqa: E501

    :param location: Тип корпуса(УЛК, ГЗ, СМ, Энерго)
    :type location: str
    :param weektype: Тип недели(ЧС, ЗН)
    :type weektype: str
    :param weekday: День недели(пн, вт...)
    :type weekday: str
    :param pairnum: Номер пары
    :type pairnum: str

    :rtype: List[Aud]
    """

    res = db_connection.GetAud(location, weektype, weekday, pairnum)
    if res == None:
        return "", status.HTTP_404_NOT_FOUND
    
    return res, status.HTTP_200_OK


def search_group(name):  # noqa: E501
    """Поиск расписания группы

    Поиск расписания группы на неделю  # noqa: E501

    :param name: Полное название группы
    :type name: str

    :rtype: Week
    """

    res  = db_connection.GetGroupWeek("'" + name + "'")
    if res == None:
        return "", status.HTTP_404_NOT_FOUND
    
    return res, status.HTTP_200_OK


def search_hospital(name=None, aud=None, spec=None):  # noqa: E501
    """Поиск расписания врачей в поликлинике

    Поиск расписания врачей в поликлинике  # noqa: E501

    :param name: Фамилия(возможно с инициалами) врача
    :type name: str
    :param aud: Номер кабинета врача
    :type aud: str
    :param spec: Специальность врача
    :type spec: str
    :param faculty: Факультет за который отвечате врач(предполагается, что для не терапевтов любой факультет подходит)
    :type faculty: str

    :rtype: List[DoctorSchedule]
    """

    res = db_connection.GetDocAll(name, aud, spec)
    if res == None:
        return "", status.HTTP_404_NOT_FOUND
    
    return res, status.HTTP_200_OK

def update_hospital(name, date, time):  # noqa: E501
    res = db_connection.UpdateDoctorsTime(name, date, time)

    if not res:
        return "", status.HTTP_404_NOT_FOUND

    return "Updated", status.HTTP_200_OK

def search_professor(name):  # noqa: E501
    """Поиск расписания преподователя

    Поиск расписания преподователя(ей) по фамилии и/или инициалам  # noqa: E501

    :param name: Фамилия(возможно с инициалами) преподователя
    :type name: str

    :rtype: List[ProfessorWeek]
    """

    res = db_connection.GetProfWeek("'" + name + "'")
    if res == None:
        return "", status.HTTP_404_NOT_FOUND
    
    return res, status.HTTP_200_OK


def search_week(date=None):  # noqa: E501
    """Поиск недели

    Номер и тип недели  # noqa: E501

    :param _date: Дата в формате дд.мм.гггг
    :type _date: str

    :rtype: InlineResponse200
    """
    return handlers.GetWeekNum(date), status.HTTP_200_OK
