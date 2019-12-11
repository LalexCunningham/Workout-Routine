from datetime import datetime as dt
import datetime
import re
import pandas as pd

exercises = ['Squat', 'Deadlift', 'Barbell Row', 'Bench Press', 'Overhead Press']

def getWeekday(date):

    '''
    returns integer representing the weekday
    0: Monday
    1: Tuesday
    2: Wednesday
    3: Thursday
    4: Friday
    5: Saturday
    6: Sunday
    '''

    splitDate = date.split('.')

    dtDate = datetime.date(int(splitDate[2]), int(splitDate[1]), int(splitDate[0]))
    return dtDate.weekday()


def getDates(date, timeframe, columns):
    datelist = pd.date_range(date, periods=timeframe).to_list()
    datesColumn = []
    for day in datelist:
        datesColumn.append([day.strftime('%d.%m.%Y')])

    for date in datesColumn:
        date.append(getWeekday(date[0]))
        for i in range(0,columns):
            date.append(None)
    return datesColumn

def initializeCSV(date, columns, timeframe):
    # Create a list that will become the column names
    cols = ['date', 'weekday']
    for exercise in columns:
        cols.append(exercise)

    df = pd.DataFrame(getDates(date, timeframe, len(columns)), columns=cols)
    return df
def generateDailyColumn(csv, overload):
    pass
def generateWeeklyColumn(csv, overload, schedule, exercise):
    df = pd.read_csv(csv)
    print(df['date', exercise])


#print(getDates(dt.today(), 10, 5))

#generateWeeklyColumn('./Workout-data/test.csv', 2.5, [0,1,3], 'Squat')
df = initializeCSV(dt.today(), exercises, 100)
df.to_csv('./Workout-data/test.csv', index=False)