import dataGenerator
from datetime import datetime as dt
import pandas as pd
import os

def editLift(workoutName):
    df = pd.read_csv('./Workout-data/{}.csv'.format(workoutName))
    possibleLifts = list(df.columns.values)[3:]
    while True:
        lift = input('Which lift would you like to edit?\nYou can choose: {}.\n'.format(possibleLifts))
        if lift in possibleLifts:
            break
        else:
            print('Please enter a lift from your workout\n')
    while True:
        weight = input('Please enter what weight you would like to start with.\n')
        try:
            float(weight)
            break
        except ValueError:
            print('Please enter a valid weight.\n')
    while True:
        increase = input('Please enter what weight you would like to increase by per workout.\n')
        try:
            float(increase)
            break
        except ValueError:
            print('Please enter a valid weight increase.\n')
    dataGenerator.editLift(workoutName, lift, weight, increase, dt.today())

def generateStronglifts():
    print('Generating your stronglifts program for the next 180 days (6 months)...')
    lifts = ['Squat', 'Bench Press', 'Barbell Row', 'Deadlift', 'Overhead Press']
    dataGenerator.initializeCSV('Stronglifts', dt.today(), lifts, 180)

    # Generate individual lifts and progressions
    dataGenerator.generateAlternatingColumn('Stronglifts', [[0, 2, 4], [0, 2, 4]], 'Squat', 35, 2.5, 4, 0.9)
    dataGenerator.generateAlternatingColumn('Stronglifts', [[0, 4], [2]], 'Bench Press', 20, 2.5, 4, 0.9)
    dataGenerator.generateAlternatingColumn('Stronglifts', [[0, 4], [2]], 'Barbell Row', 30, 2.5, 4, 0.9)
    dataGenerator.generateAlternatingColumn('Stronglifts', [[2], [0, 4]], 'Deadlift', 40, 5, 4, 0.9)
    dataGenerator.generateAlternatingColumn('Stronglifts', [[2], [0, 4]], 'Overhead Press', 20, 2.5, 4, 0.9)

def newWorkout(workoutName):
    print('Creating workout {}.\nYou should first enter what exercises you want to include in your workout. Type next when you are done.\n'.format(workoutName))
    exerciseLoop = True
    exercises = []
    while exerciseLoop:
        exercise = input('Please enter an exercise\n')
        if exercise == 'next':
            exerciseLoop = False
        else:
            exercises.append(exercise)
    print('You have entered: {}\n'.format(exercises))
    while True:
        timeFrame = input('What timeframe (in days) do you want to plan your workouts for?\n'.format(exercises))
        try:
            timeFrame = int(timeFrame)
            break
        except ValueError:
            print('Please enter a number')


    print('You want to plan your workout for the next {} days.'.format(timeFrame))
    dataGenerator.initializeCSV(workoutName, dt.today(), exercises, timeFrame)

    while True:
        workoutType = input('Do you want a standard or alternating workout?\n')
        if workoutType == 'standard':
            standardWorkout(exercises, workoutName)
            break
        elif workoutType == 'alternating':
            alternatingWorkout(exercises, workoutName)
            break
        else:
            print('Please make your choice')

    print('Workout {} made successfully'.format(workoutName))

def alternatingWorkout(exercises, workoutName):
    while True:
        deload = input('Please enter how often you want to deload (deload every x weeks):\n')
        try:
            deload = int(deload)
            break
        except ValueError:
            print('Please enter a valid number')

    while True:
        deloadWeight = input('Please enter how much (weight) you want to deload by:\n')
        try:
            deloadWeight = float(deloadWeight)
            if deloadWeight < 1:
                deloadWeight = 1 - deloadWeight
                break
            else:
                print('Please enter a decimal less than one')
        except ValueError:
            print('Please enter a valid number')
    weeksInputArray = []

    for exercise in exercises:
        weeksInputArray.append([])

    for i in range(0,2):
        print('Enter your workouts for week {}'.format(i+1))
        j = 0
        for exercise in exercises:
            days = []
            print('What days do you want to {} on?'.format(exercise))
            while True:
                day = input('Please enter a day:\n')
                if day.lower() == 'monday':
                    days.append(0)
                elif day.lower() == 'tuesday':
                    days.append(1)
                elif day.lower() == 'wednesday':
                    days.append(2)
                elif day.lower() == 'thursday':
                    days.append(3)
                elif day.lower() == 'friday':
                    days.append(4)
                elif day.lower() == 'saturday':
                    days.append(5)
                elif day.lower() == 'sunday':
                    days.append(6)
                elif day == 'next':
                    break
                else:
                    print('Please Enter a valid day')
            weeksInputArray[j].append(days)
            j += 1

    i = 0
    for exercise in exercises:
        while True:
            weight = input('What weight do you want to start your {} at?:\n'.format(exercise))
            try:
                weight = float(weight)
                break
            except ValueError:
                print('Please enter a valid starting weight:\n')

        while True:
            overload = input('Please enter how much weight you want to increase each workout:\n')
            try:
                overload = float(overload)
                break
            except ValueError:
                print('Please enter a valid weight')

        dataGenerator.generateAlternatingColumn(workoutName, weeksInputArray[i], exercise, weight, overload, deload, deloadWeight)
        i += 1

def standardWorkout(exercises, workoutName):
    while True:
        deload = input('Please enter how often you want to deload (deload every x weeks):\n')
        try:
            deload = int(deload)
            break
        except ValueError:
            print('Please enter a valid number')

    while True:
        deloadWeight = input('Please enter how much (weight) you want to deload by:\n')
        try:
            deloadWeight = float(deloadWeight)
            if deloadWeight < 1:
                deloadWeight = 1 - deloadWeight
                break
            else:
                print('Please enter a decimal less than one')
        except ValueError:
            print('Please enter a valid number')

    daysInputArray = []
    for exercise in exercises:
        days = []
        print('What days do you want to {} on?'.format(exercise))
        while True:
            day = input('Please enter a day:\n')
            if day.lower() == 'monday':
                days.append(0)
            elif day.lower() == 'tuesday':
                days.append(1)
            elif day.lower() == 'wednesday':
                days.append(2)
            elif day.lower() == 'thursday':
                days.append(3)
            elif day.lower() == 'friday':
                days.append(4)
            elif day.lower() == 'saturday':
                days.append(5)
            elif day.lower() == 'sunday':
                days.append(6)
            elif day == 'next':
                break
            else:
                print('Please Enter a valid day')
        daysInputArray.append(days)

    i = 0
    for exercise in exercises:
        while True:
            weight = input('What weight do you want to start your {} at?:\n'.format(exercise))
            try:
                weight = float(weight)
                break
            except ValueError:
                print('Please enter a valid starting weight:\n')

        while True:
            overload = input('Please enter how much weight you want to increase each workout:\n')
            try:
                overload = float(overload)
                break
            except ValueError:
                print('Please enter a valid weight')

        dataGenerator.generateStandardColumn(workoutName, daysInputArray[i], exercise, weight, overload, deload, deloadWeight)
        i += 1

def getWorkouts():
    workouts = []
    for filename in os.listdir('./Workout-data/'):
        if filename.endswith('.csv'):
            workouts.append(filename[0:-4])
    return workouts

def mainMenu():

    welcomeMessage = \
'''Welcome, this is an app to help manage and update you about your workouts.
In order to initialize a new workout, type new. You will have to answer a few questions.
If you want to view a workout, type view.
If you want to edit a workout, type edit.'''

    selection =  input(welcomeMessage + '\n')
    if selection == 'new':
        name = input('Please enter a name for your workout:\n')
        newWorkout(name)
    elif selection == 'edit':
        print('Saved workouts: {}'.format(getWorkouts()))
        name = input('Which workout would you like to edit?\n')
        editLift(name)
    elif selection == 'view':
        print('Saved workouts: {}'.format(getWorkouts()))

mainMenu()