import requests

class API:
    baseurl = "https://publiek.usc.ru.nl/app/api/v1/?module={module}&method={method}"

    def __init__(self, klantid, token):
        self.klantid = klantid
        self.token = token

    @staticmethod
    def login(self, username, password):
        response = requests.post(self.baseurl.format(module="user", method="logIn"),
                                 {'username': username, 'password': password})
        return response.json()

    def get_agenda(self):
        response = requests.post(self.baseurl.format(module="locatie", method="getLocaties"),
                                 {'klantId': self.klantid, 'token': self.token})
        return response

    def book(self, tijdObject):
        response = requests.post(self.baseurl.format(module="locatie", method="addLinschrijving"), {
            'klantId': self.klantid,
            'token': self.token,
            'inschrijvingId': tijdObject['inschrijvingId'],
            'poolId': tijdObject['poolId'],
            'laanbodId': tijdObject['laanbodId'],
            'start': tijdObject['start'],
            'eind': tijdObject['eind']
        })
        return response
