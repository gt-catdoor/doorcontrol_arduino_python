from Arduino import *

servolist = []
servovals = []
ardun = -1
selected = -1

def main():
    global servolist
    global servovals
    global ardun
    global selected
    print("Enter the serial port name: ")
    comPort = input()
    print("Enter number of pins to use for servo: ")
    num = int(input())
    if num > 0:
        for i in range(0, num):
            print("Enter pin number to use for servo " + str(i+1))
            servolist.append(int(input()))
    ardun = Arduino(comPort)
    ardun.output([], servolist)
    selected = 0
    initialize()
    help()
    mainLoop()

def mainLoop():
    global servolist
    global servovals
    global ardun
    global selected
    exit = False
    while(not exit):
        command = input().lower()
        if (command == "q"):
            exit = True
        elif (command == "l"):
            printServoList()
        elif (command == "p"):
            selectServoPin()
        elif (command == "i"):
            selectServoIndex()
        elif (command == "h") or (command == "help"):
            help()
        else:
            moveServo(selected, int(command))

def selectServoIndex():
    global servolist
    global servovals
    global ardun
    global selected
    printServoList()
    print("Enter which servo to select from list: ")
    num = int(input()) - 1
    if (num < len(servolist)) and (num >= 0):
        selected = num
        print("Selected pin: " + str(servolist[selected]) + ", selected servo: " + str(selected + 1))

def selectServoPin():
    global servolist
    global servovals
    global ardun
    global selected
    printServoList()
    print("Enter the pin number of servo to be controlled:")
    try:
        num = servolist.index(int(input()))
        selected = num
    except ValueError:
        pass
    print("Selected pin: " + str(servolist[selected]) + ", selected servo: " + str(selected + 1))

def moveServo(index, degree):
    global servolist
    global servovals
    global ardun
    global selected
    if (degree <= 180) and (degree >= 0):
        servovals[index] = degree
        ardun.servoWrite(servolist[index], servovals[index])
        print("Moved servo " + str(index+1) + " to " + str(servovals[index]) + " degrees.")

def initialize():
    global servolist
    global servovals
    global ardun
    global selected
    for i in servolist:
        servovals.append(90)
        ardun.servoWrite(i, 90)
    print("Servos initialized")

def printServoList():
    global servolist
    global servovals
    global ardun
    global selected
    for i in range(0, len(servolist)):
        print("Servo " + str(i+1) + ", pin number: " + str(servolist[i]) + ", value: " + str(servovals[i]))

def help():
    print("Enter degree between 0 and 180 to move selected servo.")
    print("Enter P to select servo by its pin number.")
    print("Enter I to select servo by its index(indexed from 1).")
    print("Enter L to view list of all servos.")
    print("Enter Q to exit.")
    print("Enter H or help to view this instruction.")

if __name__ == "__main__":
    main()
