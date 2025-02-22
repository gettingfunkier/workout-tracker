import json

filename = "workout.json"
def importData(): # gets information from JSON file
    workout = {}
    with open(filename, "r") as file:
        return json.load(file)

def saveFile(workout): # saves information to JSON file
    with open(filename, "w") as file:
        json.dump(workout, file, indent = 4)

def addEx(workout): # writes a new exercise
    name = input("name: ")
    sets = input("sets: ")
    reps = input("reps: ")
    weight = input("weight: ")
    workout[name] = {'sets': sets, 'reps': reps, 'weight': weight}
    print(f"'{name}' logged!")
    saveFile(workout)

def viewWorkout(): # prints current workout
    if not workout:
        print("No exercises logged yet!")
        return

    for name, info in workout.items():
        sets = info['sets']
        reps = info['reps']
        weight = info['weight']
        print(f"{name}: {sets} sets of {reps} reps, at {weight}kg")

def exportFile(workout): # creates a txt file with workout info
    workout = importData()
    with open("workout.txt", "w") as file:
        heading = input("give your workout a title: ")
        weekday = input(f"weekdays for {heading}: ")
        file.write(f"{heading}\nTo practice on {weekday}:\n")
        for name, info in workout.items():
            sets = info['sets']
            reps = info['reps']
            weight = info['weight']
            file.write(f"{name}: {sets} sets of {reps} reps, @ {weight}kg\n")
        print("exported successfully!")
            
def resetData(workout): # erases all data
    confirm = input("will erase all data, proceed? y/n\n")

    if confirm == "y":
        workout.clear()
        with open(filename, "w") as file:
            json.dump(workout, file,)
        
        with open("workout.txt", "r+") as file:
            for line in file:
                file.write("")


while True:
    act = input("(a) - add exercise (v) - view workout (e) - export (r) - reset (q) - quit\n")
    workout = importData()
    if act == "a":
        addEx(workout)
    if act == "v":
        viewWorkout()
    if act == "e":
        exportFile(workout)
    if act == "r":
        resetData(workout)
    if act == "q":
        print("Godspeed!")
        break