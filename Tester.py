from Arduino import *

ar = Arduino("COM4")

ar.output([], [9])
ar.servoWrite(9, 180)