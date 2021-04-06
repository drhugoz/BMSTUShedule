from swagger_server.models import aud


class AudBuilder:
    def __init__(self):
        self.aud = aud.Aud()

    def with_number(self, number):
        self.aud.number = number
        return self

    def with_location(self, location):
        self.aud.location = location
        return self

    def build(self):
        return self.aud

