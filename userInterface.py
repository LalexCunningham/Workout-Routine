import dataGenerator
from datetime import datetime as dt
welcomeMessage = '''Welcome, this is an app to help manage and update you about your workouts.
In order to initialize your workout, type initialize. You will have to answer a few questions.
If you want to view a workout, type view, followed by the workout name.
If you want to edit a workout, type edit, followed by the workout name.
'''

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

    standardWorkout(exercises, workoutName)

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
print(welcomeMessage)
newWorkout('Workout_1')