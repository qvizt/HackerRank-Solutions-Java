# Solution for Day 4 Class vs. Instance

class Person:

    def __init__(self, initialAge):
        if (initialAge < 0):
            print("Age is not valid, setting age to 0.")
            initialAge = 0

        self.__age = initialAge

    # Add some more code to run some checks on initialAge
    def amIOld(self):
        if self.__age < 13:
            print("You are young.")
        elif self.__age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        self.__age += 1


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
