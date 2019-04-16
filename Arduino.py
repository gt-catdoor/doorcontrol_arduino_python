#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial.tools.list_ports
import serial
from serial import SerialException


class Arduino(object):

    __OUTPUT_PINS = -1
    __SERVO_PINS = -1

    def __init__(self, port="", baudrate=115200):
        self.serial = None
        if port == "":
            ports = list(serial.tools.list_ports.comports())
            for p in ports:
                print(p.device)
            serials = []
            connectedSerial = None
            connected = False
            for p in ports:
                try:
                    print("Attempting to connect: " + p.device)
                    connectedSerial = serial.Serial(p.device, baudrate, timeout=1, write_timeout=1)
                    print("Attempting handshake with: " + p.device)

                    connectedSerial.write(b'97')

                    # print("Preliminary message received: " + self.getDataSerial(connectedSerial))

                    msg = self.getDataSerial(connectedSerial)
                    #print("Response received: (" + msg + ")")

                    if msg == "ready":
                        connectedSerial.write(b'98')
                        print("Response received from: " + p.device)
                        self.serial = connectedSerial
                        print("Arduino Connected.")
                    else:
                        print(p.device + " failed.")
                        connectedSerial.close()

                    # print("Waiting response from: " + p.device)
                    # msg = None
                    # while msg != "ready":
                    #     msg = self.getDataSerial(connectedSerial)
                    #     print("Message returned: '" + msg + "'")
                    #     if msg == "ready":
                    #         self.serial = connectedSerial
                    #         print("Arduino Connected.")
                    #     else:
                    #         print(p.device + " failed.")
                    #         connectedSerial.close()
                except SerialException:
                    print(p.device + " timed out.")
                    pass
        else:
            try:
                self.serial = serial.Serial(port, baudrate)
            except SerialException:
                pass
        if self.serial is not None:
            # self.serial.write(b'99')
            print("Serial connected")
        else:
            print("Serial connection failed")

    def __str__(self):
        return "Arduino is on port %s at %d baudrate" %(self.serial.port, self.serial.baudrate)

    def output(self, pinArray, servoList):
        print("Initializing output pins and servos")
        self.__sendData(len(pinArray))

        if(isinstance(pinArray, list) or isinstance(pinArray, tuple)):
            print("Setting up pins")
            self.__OUTPUT_PINS = pinArray
            for each_pin in pinArray:
                self.__sendData(each_pin)

        self.__sendData(len(servoList))
        if (isinstance(servoList, list) or isinstance(servoList, tuple)):
            print("Setting up servos")
            self.__SERVO_PINS = servoList
            for pin in servoList:
                self.__sendData(pin)

        return True

    def setLow(self, pin):
        self.__sendData('0')
        self.__sendData(pin)
        return True

    def setHigh(self, pin):
        self.__sendData('1')
        self.__sendData(pin)
        return True

    def getState(self, pin):
        self.__sendData('2')
        self.__sendData(pin)
        return self.__formatPinState(self.__getData()[0])

    def analogWrite(self, pin, value):
        self.__sendData('3')
        self.__sendData(pin)
        self.__sendData(value)
        return True

    def analogRead(self, pin):
        self.__sendData('4')
        self.__sendData(pin)
        return self.__getData()

    def servoWrite(self, pin, value):
        self.__sendData('5')
        self.__sendData(pin)
        self.__sendData(value)
        return True

    def turnOff(self):
        for each_pin in self.__OUTPUT_PINS:
            self.setLow(each_pin)
        return True

    def resetServo(self):
        for each_pin in self.__SERVO_PINS:
            self.servoWrite(each_pin, 90)
        return True

    def sendDataSerial(self, ser,  serial_data):
        serial_data = str(serial_data).encode('utf-8')
        ser.write(serial_data)

    def getDataSerial(self, ser):
        input_string = ser.readline()
        input_string = input_string.decode('utf-8')
        return input_string.rstrip('\r\n')

    def __sendData(self, serial_data):
        while(self.__getData()[0] != "r"):
            pass
        serial_data = str(serial_data).encode('utf-8')
        self.serial.write(serial_data)

    def __getData(self):
        input_string = self.serial.readline()
        input_string = input_string.decode('utf-8')
        return input_string.rstrip('\r\n')

    def __formatPinState(self, pinValue):
        if pinValue == '1':
            return True
        else:
            return False

    def close(self):
        self.serial.close()
        return True
