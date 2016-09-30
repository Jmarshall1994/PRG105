


cars = ["Mustang", "Civic", "Carolla", "Corvette", "Pilot", "Crv"]


print (cars[2])
print ("\n")


for car in cars:
    print car
print("\n")


print("Adding a new car to the list:")
cars.append("BMW")
for car in cars:
    print car
print ("\n")


cars.sort()
for car in cars:
    print car
print("\n")

cars = []
newcar = ""

print ("Please enter types of cars, when finished enter done")
while newcar != "done":
    newcat = raw_input("Please enter a type of car: ")
    if newcar != "done":
        cars.append(newcar)

for car in cars:
    print car
print ("\n")