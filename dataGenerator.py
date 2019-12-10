from datetime import datetime as dt
import csv
import pandas as pd

exercises = ['Pushups', 'Pullups', 'Planks', 'Squats']

def initializeCSV(date, columns, timeframe):
    cols = ['date']
    for exercise in columns:
        cols.append(exercise)
    df = pd.DataFrame
    df.columns = cols
    '''
    datelist = pd.date_range(date, periods=timeframe).to_list()
    datesColumn = []
    for day in datelist:
        datesColumn.append(day.strftime('%d.%m.%Y'))
    df.date = datesColumn
    '''
    df.to_csv(r'./Workout-data/test.csv')

initializeCSV(dt.today(), exercises, 100)