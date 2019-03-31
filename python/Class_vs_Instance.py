'''
https://www.hackerrank.com/challenges/30-class-vs-instance/submissions/code/103534389
'''
class Person:
    __age = None

    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            self.__age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.__age = initialAge

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.__age < 13 :
            print("You are young.")
        elif self.__age  < 18 and self.__age  >= 13:
            print("You are a teenager.")  
        else:
            print("You are old.")    

    def yearPasses(self):
        # Increment the age of the person in here
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
