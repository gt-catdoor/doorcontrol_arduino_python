from Arduino import *
import serial.tools.list_ports
import serial
import time
from serial import SerialException

servolist = []
servovals = []
ardun = -1
selected = -1
initialized = 0

def main():
    global servolist
    global servovals
    global ardun
    global selected
    global initialized
    # ports = list(serial.tools.list_ports.comports())
    # for p in ports:
    #     print(p.hwid)
    serials = []
    connectedSerial = None
    connected = False
    # for p in ports:
    #     try:
    #         connectedSerial = serial.Serial(p.device, 115200)
    #         connectedSerial.write(b'98')
    #         msg = connectedSerial.readline()
    #         print(msg)
    #         if msg == "Catronic Ready":
    #             connectedSerial.close()
    #             ardun = Arduino(p.device)
    #     except SerialException:
    #         pass
    # selected = None
    # for s in serials:
    #     s.write(b'98')
    #     msg = s.readline()
    #     print(msg)
    #     if msg == "Catronic Ready":
    #         s.close()
    #         ardun = Arduino(s.device)
    # print("Enter the serial port name: ")
    # comPort = input()
    # ardun = Arduino()
    testInitialize()
    # demoInitialize()
    # doorLock("lock down")
    # print(ardun.analogRead(9))
    # doorLock("unlock")
    # print(ardun.analogRead(9))
    # print("Test complete")
    # print("Enter number of pins to use for servo: ")
    # num = int(input())
    # if num > 0:
    #     for i in range(0, num):
    #         print("Enter pin number to use for servo " + str(i+1))
    #         servolist.append(int(input()))
    # # ardun = Arduino(comPort)
    # ardun.output([], servolist)
    # selected = 0
    # initialize()
    # help()
    # initialized = 1
    # mainLoop()

def testInitialize():
    global servolist
    global servovals
    global ardun
    global selected
    global initialized
    ardun = Arduino()
    ardun.output([2], [])
    selected = 0
    ledOn = 0
    while True:
        if ledOn == 0:
            ardun.setHigh(2)
            ledOn = 1
            print(ardun.getState(2))
            print(ardun.analogRead(8))
        else:
            ardun.setLow(2)
            ledOn = 0
            print(ardun.getState(2))
            print(ardun.analogRead(8))
        time.sleep(1)


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
            printServoList()
            print("Enter the pin number of servo to be controlled:")
            selectServoPin(input().lower())
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
        selectServoPin(num)
        print("Selected pin: " + str(servolist[selected]) + ", selected servo: " + str(selected + 1))



def selectServoPinInput():
    global servolist
    global servovals
    global ardun
    global selected
    printServoList()
    print("Enter the pin number of servo to be controlled:")
    try:
        num = servolist.index(int(input()))
        selectServoPin(num)
    except ValueError:
        pass
    print("Selected pin: " + str(servolist[selected]) + ", selected servo: " + str(selected + 1))

def selectServoPin(num):
    global servolist
    global servovals
    global ardun
    global selected
    #printServoList()
    #print("Enter the pin number of servo to be controlled:")
    try:
        selected = num
    except ValueError:
        pass


def moveServo(index, degree):
    global servolist
    global servovals
    global ardun
    global selected
    if (degree <= 180) and (degree >= 0):
        servovals[index] = degree
        ardun.servoWrite(servolist[index], servovals[index])
        print("Moved servo " + str(index+1) + " to " + str(servovals[index]) + " degrees.")

def doorLock(state):
    global initialized
    global selected
    if initialized == 0:
        demoInitialize()
    if state.lower() == "lock down":
        moveServo(selected, 0)
    elif state.lower() == "let cats in only":
        moveServo(selected, 60)
    elif state.lower() == "let cats out only":
        moveServo(selected, 120)
    elif state.lower() == "unlock":
        moveServo(selected, 180)

# def demoInitialize():
#     global servolist
#     global servovals
#     global ardun
#     global selected
#     global initialized
#     ports = list(serial.tools.list_ports.comports())
#     for p in ports:
#         print(p)
#     serials = []
#     for p in ports:
#         serials.append(serial.Serial(p, 115200))
#     selected = None
#     for s in serials:
#         msg = s.readline()
#         print(msg)
#         if msg == "Catronic Ready":
#             selected = s
#     #print("Enter the serial port name: ")
#     comPort = "COM10" #input()
#     #print("Enter number of pins to use for servo: ")
#     num = 1 #int(input())
#     if num > 0:
#         for i in range(0, num):
#             #print("Enter pin number to use for servo " + str(i+1))
#             #servolist.append(int(input()))
#             servolist.append(9)
#     ardun = Arduino(comPort)
#     ardun.output([], servolist)
#     selected = 0
#     initialize()
#     initialized = 1
#     #help()
#     #mainLoop()


def demoInitialize():
    global servolist
    global servovals
    global ardun
    global selected
    global initialized
    # ports = list(serial.tools.list_ports.comports())
    # for p in ports:
    #     print(p)
    # serials = []
    # for p in ports:
    #     serials.append(serial.Serial(p, 115200))
    # selected = None
    # for s in serials:
    #     msg = s.readline()
    #     print(msg)
    #     if msg == "Catronic Ready":
    #         selected = s
    #print("Enter the serial port name: ")
    # comPort = "COM10" #input()
    #print("Enter number of pins to use for servo: ")
    num = 1 #int(input())
    if num > 0:
        for i in range(0, num):
            #print("Enter pin number to use for servo " + str(i+1))
            #servolist.append(int(input()))
            servolist.append(9)
    ardun = Arduino()
    ardun.output([], servolist)
    selected = 0
    initialize()
    initialized = 1
    #help()
    #mainLoop()


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
