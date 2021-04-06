# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.aud import Aud  # noqa: E501
from swagger_server.models.doctor_schedule import DoctorSchedule  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.professor_week import ProfessorWeek  # noqa: E501
from swagger_server.models.week import Week  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_search_audience(self):
        """Test case for search_audience

        Поиск свободных аудиторий
        """
        query_string = [('location', 'location_example'),
                        ('weektype', 'Тип текущей недели'),
                        ('weekday', 'Текущий день недели'),
                        ('pairnum', 'Номер текущей пары')]
        response = self.client.open(
            '/RyazMax/BaumanBotApi/1.0.0/audience',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_group(self):
        """Test case for search_group

        Поиск расписания группы
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/RyazMax/BaumanBotApi/1.0.0/group',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_hospital(self):
        """Test case for search_hospital

        Поиск расписания врачей в поликлинике
        """
        query_string = [('name', 'name_example'),
                        ('aud', 'aud_example'),
                        ('spec', 'spec_example'),
                        ('faculty', 'faculty_example')]
        response = self.client.open(
            '/RyazMax/BaumanBotApi/1.0.0/hospital',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_professor(self):
        """Test case for search_professor

        Поиск расписания преподователя
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/RyazMax/BaumanBotApi/1.0.0/professor',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_week(self):
        """Test case for search_week

        Поиск недели
        """
        query_string = [('_date', 'Текущая дата')]
        response = self.client.open(
            '/RyazMax/BaumanBotApi/1.0.0/week',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
