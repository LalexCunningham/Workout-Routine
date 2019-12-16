import pandas as pd
from datetime import datetime as dt
import math
from twilio.rest import Client

def sendText(workout):
    df = pd.read_csv('./Workout-data/{}.csv'.format(workout))
    date = dt.now().strftime('%d.%m.%Y')

    # Get columns/lifts
    liftNames = list(df.columns.values)[3:]

    todaysLifts = ''

    today = df[df['date'] == date]

    i = 0
    for lift in today.iloc[0, 3:]:
        if math.isnan(lift):
            i += 1
        else:
            todaysLifts += ('{}: {}kg\n'.format(liftNames[i], lift))
            i += 1

    accountSID = 'AC2847c6838a359005a0bc5b636221653d'
    authToken = '681990835404ed57300fdfba1577fed9'
    twilioCli = Client(accountSID, authToken)
    myTwiolioNumber = '+1 205 350 9126'
    myCellPhone = '+353834240688'

    messageBody = '\n\nGood morning, this is your workout routine for today:\n\n{}'.format(todaysLifts)
    message = twilioCli.messages.create(body=messageBody, from_=myTwiolioNumber, to=myCellPhone)

