# Exercise 82:Taxi Fare
# (22 Lines)
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25
# for every 140 meters traveled. Write a function that takes the distance traveled (in
# kilometers) as its only parameter and returns the total fare as its only result. Write a
# main program that demonstrates the function.

def taxi_fare(km):
    return 4+(0.25*km*1000/140)

kmStr = input("Please enter km traveled:\n")
distance = float(kmStr)
print("You taxi fare is {0:.2f}".format(taxi_fare(distance)))