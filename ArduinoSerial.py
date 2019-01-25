from time import sleep
import serial

class ArduinoSerial(object):


    def __int__(self, port, output=[]):
        self.serial = serial.Serial(port, 115200)
        self.serial.write(b'99')
        self.setOutput(output)

    def setOutput(self, pins):
        self.sendData(len(pins))

        if ((isinstance(pins, list)) or isinstance(pins, tuple)):
            for pin in pins:
                self.sendData(pin)
        return True

    def setLow(self, pin):
        self.sendData('0')
        self.sendData(pin)
        return True

    def setHigh(self, pin):
        self.sendData('1')
        self.sendData(pin)
        return True

    def digitalRead(self, pin):
        self.sendData('2')
        self.sendData(pin)
        return int(self.receiveData()[0])

    def analogWrite(self, pin, value):
        self.sendData('3')
        self.sendData(pin)
        self.sendData(value)
        return True

    def analogRead(self, pin):
        self.sendData('4')
        self.sendData(pin)
        return self.receiveData()

    def sendData(self, data):
        while(self.receiveData()[0] != "r"):
            pass
        data = str(data).encode('utf-8')
        self.serial.write(data)

    def receiveData(self):
        s = self.serial.readline()
        s = s.decode('utf-8')
        return s.rstrip('\n')

