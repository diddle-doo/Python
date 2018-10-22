# Car-rental system
# car - display details, calculate the fare
# fare=typeofcar's cost*number of days

class Car():
    def __init__(self):
        self.carFare={'Hatchback':30,'Sedan':50,'SUV':100}

    def displayFareDetails(self):
        print("Cost per day")
        print("Hatchback", self.carFare['Hatchback'])
        print("Sedan", self.carFare['Sedan'])
        print("SUV",self.carFare['SUV'])

    def calculateFar(self,typeOfCar,numOfDays):
        return self.carFare[typeOfCar]*numOfDays

car=Car()
while True:
    print("Enter 1 , for display car details")
    print("ENter 2 for entering the type of car")
    print("Enter 3 for quitting")
    userChoice=int(input())
    if userChoice == 1:
        car.displayFareDetails()
    elif userChoice ==2:
        print("Enter the type of car you want to rent: ")
        typeOfCar=input()
        print("ENter the number of days you want to rent the car: ")
        numOfDays=int(input())
        fare=car.calculateFar(typeOfCar,numOfDays)
        print("Total Payable Amount: ", fare)
    elif userChoice == 4:
        quit()


