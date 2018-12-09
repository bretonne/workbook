# Exercise 128: Reverse Lookup
# (Solved—40 Lines)
# Write a function named reverseLookup that finds all of the keys in a dictionary
# that map to a specific value. The function will take the dictionary and the value to
# search for as its only parameters. It will return a (possibly empty) list of keys from
# the dictionary that map to the provided value.
# Include a main program that demonstrates the reverseLookup function as part
# of your solution to this exercise. Your program should create a dictionary and then
# show that the reverseLookup function works correctly when it returns multiple
# keys, a single key, and no keys. Ensure that your main program only runs when
# the file containing your solution to this exercise has not been imported into another
# program.
def getInputs():
    flightMarkets = {}
    line = input()
    while line != "" :
        tokens = line.split(",")
        if (len(tokens)==2):
            flightMarkets[tokens[0]] = tokens[1]
        line = input()
    return flightMarkets

def findFlightsForMarket(connection, flightMarkets):
    flights = []
    for flight, market in flightMarkets.items():
        if (connection==market):
            flights.append(flight)
    return flights


def main():
    flightMarkets = getInputs()
    connection = input("Connection:")
    flights = findFlightsForMarket(connection, flightMarkets)
    print(flights)

main()
