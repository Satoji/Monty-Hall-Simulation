import random

def createDoors(numDoors):
    doors = ['goat'] * numDoors
    randCar = random.randint(0, numDoors - 1)
    doors[randCar] = 'car'
    return doors


def montyHall(simulations, numDoors, switch, version1, fall):
    winCount = 0
    lossCount = 0

    for i in range(simulations):
        doors = createDoors(numDoors)
        random.shuffle(doors)
        selectedDoor = random.randint(1, numDoors)

        while len(doors) > 2:
            if fall: 
                hostChoices = [i + 1 for i, prize in enumerate(doors) if i != (selectedDoor-1)] # Host choices are everything but the selectedDoor
                revealDoor = random.choice(hostChoices)
                if doors[revealDoor - 1] == 'car': # If host chooses a car, remove this trial from existence
                    break
            else:
                hostChoices = [i + 1 for i, prize in enumerate(doors) if prize == "goat" and i != (selectedDoor-1)]  # Host can only choose doors with goats
                revealDoor = random.choice(hostChoices)

            doors.pop(revealDoor - 1) # Remove revealed door from doors

            if selectedDoor > revealDoor: # Change position of selectedDoor
                selectedDoor = selectedDoor - 1

            if not version1: # Version where we switch doors after every reveal
                if switch:
                    availableDoors = [i + 1 for i in range(len(doors))]
                    selectedDoor = random.choice([door for door in availableDoors if door != selectedDoor])

        if version1: # Version where we don't switch doors after every reveal
            availableDoors =[i + 1 for i, prize in enumerate(doors) if i + 1 != selectedDoor]
            if switch:
                selectedDoor = availableDoors[0]

        if doors[selectedDoor-1] == 'car':
            winCount += 1
        else:
            lossCount += 1

    win_probability = winCount / simulations
    loss_probability = lossCount / simulations

    print(f"Probability of winning: {win_probability}")
    print(f"Probability of losing: {loss_probability}\n")

    
simulations = 1000 
switch = True # Allow to switch doors
version1 = True # Don't switch doors randomly after each reveal    
fall = False # Monty Fall variant        

print("-------------------------------\n")

for numDoorsLoop in [3, 6, 9, 20, 100]:
    print(f"{numDoorsLoop} doors")
    
    print("Monty Hall")
    print(f"Switching door at the end") 
    montyHall(simulations, numDoorsLoop, switch, version1, fall=False)
    
    print(f"Switching door randomly after each reveal") 
    montyHall(simulations, numDoorsLoop, switch, version1 = False, fall = False)

    print(f"Keeping door")
    montyHall(simulations, numDoorsLoop, switch=False, version1=True, fall = False)


    print("Monty Fall")
    print(f"Switching door at the end")
    montyHall(simulations, numDoorsLoop, switch, version1, fall=True)

    print(f"Switching door randomly after each reveal")
    montyHall(simulations, numDoorsLoop, switch, version1=False, fall=True)

    print(f"Keeping door")
    montyHall(simulations, numDoorsLoop, switch=False, version1=True, fall = True)

    print("-------------------------------\n")