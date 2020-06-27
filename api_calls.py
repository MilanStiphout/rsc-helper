import requests

baseurl = "https://publiek.usc.ru.nl/app/api/v1/?module={module}&method={method}"


class API:

    def __init__(self, klantid, token):
        self.klantid = klantid
        self.token = token

    def get_agenda(self):
        response = requests.post(baseurl.format(module="locatie", method="getLocaties"),
                                 {'klantId': self.klantid, 'token': self.token})
        return response.json()

    def book(self, moment):
        response = requests.post(baseurl.format(module="locatie", method="addLinschrijving"), {
            'klantId': self.klantid,
            'token': self.token,
            'inschrijvingId': moment['inschrijvingId'],
            'poolId': moment['poolId'],
            'laanbodId': moment['laanbodId'],
            'start': moment['start'],
            'eind': moment['eind']
        })
        return response.json()


def login(username, password):
    response = requests.post(baseurl.format(module="user", method="logIn"),
                             {'username': username, 'password': password})
    if 'authError' in response:
        print("Fout tijdens inloggen: {}").format(response.json()['error'])
    else:
        return response.json()
