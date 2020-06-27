from datetime import datetime, timedelta
from api_calls import API, login
from fitbot import find_session

f = open("login.txt", 'r')
login_data = login(f.readline(), f.readline())
api = API(login_data['klantId'], login_data['token'])
timeframe = {'start': datetime.now().timestamp(), 'end':  (datetime.now() + timedelta(days=10)).timestamp()}


find_session(timeframe, "Fitness", api)
