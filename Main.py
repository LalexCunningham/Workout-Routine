import pandas as pd
from datetime import datetime as dt
import math
from twilio.rest import Client

def sendText():
    try:
        active_workout = open('./Workout-data/active_workout', 'r')
        workout = active_workout.readline()

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

        if todaysLifts == '':
            print('No workout for today.')
        else:
            token = open('twilio_info', 'r')

            accountSID = 'AC2847c6838a359005a0bc5b636221653d'
            authToken = token.readlines()[0]
            twilioCli = Client(accountSID, authToken)
            myTwiolioNumber = '+1 205 350 9126'
            myCellPhone = '+353834240688'

            messageBody = '\n\nGood morning, this is your workout routine for today:\n\n{}'.format(todaysLifts)
            message = twilioCli.messages.create(body=messageBody, from_=myTwiolioNumber, to=myCellPhone)
            print('Message Sent.')

    except FileNotFoundError:
        print('Workout doesnt exist')


sendText()