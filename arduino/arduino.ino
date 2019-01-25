#include <Servo.h>

Servo *servoList;
int *servoPins;
int servoCount;

void setup() {
    Serial.begin(115200);
    Serial.setTimeout(5);

    int count = readData();
    for (int i = 0; i < count; i++) {
        pinMode(readData(), OUTPUT);
    }

    servoCount = readData();
  	servoList = new Servo[servoCount];
    servoPins = new int[servoCount];
    int pin;
  	for (int i = 0; i < servoCount; i++) {
      pin = readData();
  		servoList[i].attach(pin);
      servoPins[i] = pin;
  	}
}

void loop() {
    switch (readData()) {
        case 0 :
            digitalWrite(readData(), LOW); break;
        case 1 :
            digitalWrite(readData(), HIGH); break;
        case 2 :
            Serial.println(digitalRead(readData())); break;
        case 3 :
            analogWrite(readData(), readData()); break;
        case 4 :
            Serial.println(analogRead(readData())); break;
    		case 5 :
            int pin = readData();
            for (int i = 0; i < servoCount; i++) {
              if (servoPins[i] == pin) {
                servoList[i].write(readData());
              }
            }
            break;
        case 99:
            break;
    }
}

int readData() {
    Serial.println("r");
    while(1) {
        if(Serial.available() > 0) {
            return Serial.parseInt();
        }
    }
}
