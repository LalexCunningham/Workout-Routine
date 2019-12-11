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
def generateAlternatingColumn(csv, overload):
    pass
def generateStandardColumn(csv,  schedule, exercise, startingWeight, overload, deload_freq, deload_percent):
    df = pd.read_csv(csv)

    # Add week number to column
    # Create array
    weekNumberAry = []
    weekNum = 1
    firstWeek = True
    for i in range(0, len(df.index)):
        if df.loc[i, 'weekday'] == 0 and firstWeek == True:
            pass
        elif df.loc[i, 'weekday'] == 6:
            firstWeek = False
        elif df.loc[i, 'weekday'] == 0:
            weekNum += 1
        weekNumberAry.append(weekNum)
    df.insert(2, 'week', weekNumberAry)

    weight = startingWeight
    for i in range(0, len(df.index)):
        if df.loc[i, 'weekday'] in schedule:
            deloadWeight = myRound(weight * deload_percent)
            if df.loc[i, 'week'] % deload_freq == 0:
                df.loc[i, [exercise]] = deloadWeight
            else:
                df.loc[i, [exercise]] = weight
                weight += overload
    print(df.head(50))

def myRound(x, prec=2, base=2.5):
    return round(base * round(float(x)/base), prec)

#print(getDates(dt.today(), 10, 5))

generateStandardColumn('./Workout-data/test.csv', [0,1,3], 'Bench Press', 40, 2.5, 3, 0.85)
#df = initializeCSV(dt.today(), exercises, 100)
#df.to_csv('./Workout-data/test.csv', index=False)