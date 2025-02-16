workout = {}

def action():
    while True:
        act = input("a - add exercise\ni - import data\nv - view workout\ne - export\nr - reset\nq - quit\n")
        if act == "a":
            addEx()
        if act == "i":
            importData(workout)
        if act == "v":
            viewWorkout(workout)
        if act == "e":
            exportFile(workout)
        if act == "r":
            resetData(workout)
        if act == "q":
            print("Godspeed!")
            break

def addEx():
    entry = input("Entere exercise (name,sets,reps,weight):")
    info = entry.split(",")

    name = str(info[0])
    sets = str(info[1])
    reps = str(info[2])
    weight = str(info[3])

    workout[name] = {'sets': sets, 'reps': reps, 'weight': weight}
    print(f"'{name}' logged!")

    return workout

def viewWorkout(workout):
    if not workout:
        print("No exercises logged yet!")
        return

    for name, info in workout.items():
        sets = info['sets']
        reps = info['reps']
        weight = info['weight']
        print(f"{name}: {sets} sets of {reps} reps, at {weight}kg")

def importData(workout):
    confirm = input("will override current workout, proceed? y/n\n")
    
    if confirm == "y":
        file = open("workout.txt")

        for line in file:
            split = line.strip().split(',')
            name = split[0]
            sets = split[1]
            reps = split[2]
            weight = split[3]

            workout[name] = {'sets': sets, 'reps': reps, 'weight': weight}

        print("data logged!")

def exportFile(workout):
    with open('workout.txt', 'w') as f:
        for name, info in workout.items():
            sets = info['sets']
            reps = info['reps']
            weight = info['weight']
            
            f.write(f"{name},{sets},{reps},{weight}\n")
        print("data exported!")
    
def resetData(workout):
    confirm = input("will erase all data, proceed? y/n\n")

    if confirm == "y":
        workout.clear()

    return workout

action()