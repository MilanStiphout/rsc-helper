from getpass import getpass
import datetime
import time
import requests

baseurl = "https://publiek.usc.ru.nl/app/api/v1/?module={module}&method={method}"


loginData = login()
keuze_sport = raw_input("Welke sport? (Keuze uit {squash student, zwemmen}): ")
if(keuze_sport in "squash student"):
    keuze_sport = "squash student"
    print("Keuze is squash")
else:
    keuze_sport = "zwemmen"
    print("Keuze is zwemmen")

keuze_begin = int(raw_input("Begintijd? (uur): "))
keuze_eind = int(raw_input("Eindtijd? (uur): "))

# "zwemmen"/"squash student"
if 'authError' in loginData:
    print("Fout tijdens inloggen: {}").format(loginData['error'])
else:
    token = loginData['token']
    klantid = loginData['klantId']
    print("Bot gestart voor {}".format(keuze_sport))
    while(True):
        tijden = get_agenda().json()
        vanaf = datetime.datetime.now() + datetime.timedelta(days=2)
        vanaf = vanaf.replace(hour=keuze_begin, minute=00, second=0, microsecond = 0)
        tot = vanaf.replace(hour=keuze_eind, minute=0, second=0, microsecond = 0)

        for tijd in tijden:
            startTijd = datetime.datetime.fromtimestamp(int(tijd['start']))
            if (startTijd > vanaf and startTijd < tot):
                if(int(tijd['inschrijvingen']) < 10 and tijd['poolNaam'] == "zwemmen" and keuze_sport == "zwemmen"):
                    print ("Er zijn plekken vrij op tijd {}".format(startTijd))
                    booking = book(tijd).json()
                    print("Geboekt op tijd {}".format(startTijd))
                if(int(tijd['inschrijvingen']) < 4 and tijd['poolNaam'] == "squash student" and keuze_sport == "squash student"):
                    print ("Er zijn plekken vrij op tijd {}".format(startTijd))
                    booking = book(tijd).json()
                    print("Geboekt op tijd {}".format(startTijd))
        print("Niks vrij atm.")
        time.sleep(60)
