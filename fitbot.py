from datetime import datetime, timedelta
import time


def show_results(moment_list):
    print("Gevonden plaatsen voor {} in opgegeven tijdsframe:".format(moment_list[0]['catalogusId']))
    for moment in moment_list:
        print("[{} {} - {}]: {} plaatsen".format(moment['datum'],
                                                 format_time(int(moment['start'])),
                                                 format_time(int(moment['eind'])),
                                                 str(int(moment['maxInschrijvingen']) - int(moment['inschrijvingen']))))


def format_time(t):
    return datetime.utcfromtimestamp(t).strftime('%H:%S')


def find_session(timeframe, ticket, api):
    booked = False
    while not booked:
        candidates = [t for t in api.get_agenda() if t['catalogusId'] == ticket and
                      t['inschrijvingen'] < t['maxInschrijvingen'] and
                      int(t['start']) >= timeframe['start'] and int(t['eind']) <= timeframe['end']]
        if candidates:
            show_results(candidates)
            # TODO: iets boeken
            booked = True
        else:
            print("Geen vrije plaatsen gevonden. Opnieuw proberen over 1 minuut.")
            time.sleep(60)
