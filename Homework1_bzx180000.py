import fileinput
import re
import pickle

class Person:
    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone

    def printAll(self):
        print("last : " + self.last)
        print("first : " + self.first)
        print("mi : " + self.mi)
        print("id : " + self.id)
        print("phone : " + self.phone)

def parseName(name):
    return name.capitalize()

def parseMiddleInit(initial):
    if not initial:
        return "X"
    return initial[0].capitalize()

def parseId(id):
    pattern = re.compile("^[A-z]{2}[0-9]{4}$")
    while not pattern.match(id):
        print("id is invalid: " + id)
        id = input("Please enter a valid id: ")
    return id

def parsePhone(phoneNum):
    pattern = re.compile("^[0-9]{3}-[0-9]{3}-[0-9]{4}$")
    while not pattern.match(phoneNum):
        print("Phone " + phoneNum + " is invalid")
        print("Enter phone number in form 123-456-7890")
        phoneNum = input("Enter phone number: ")
    return phoneNum
        
people = []
filename = input("Enter filename: ")
with open(filename) as f:
    next(f)
    for line in f:
        lineArr = line.split(",")
        newPerson = Person (parseName(lineArr[0]), parseName(lineArr[1]) , parseMiddleInit(lineArr[2]),parseId(lineArr[3]), parsePhone(lineArr[4]))
        people.append(newPerson)
        
print(len(people))
for person in people:
    person.printAll()

file = open("data/pickle.csv", "wb")
pickle.dump(people, file)