#include <Servo.h>

Servo *servoList;
int *servoPins;
int servoCount;

void setup() {
	pinMode(LED_BUILTIN, OUTPUT);
	digitalWrite(LED_BUILTIN, LOW);
    Serial.begin(115200);
    Serial.setTimeout(5);

    initializationLoop();

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
			{
				int p = readData();
				for (int i = 0; i < servoCount; i++) {
					if (servoPins[i] == p) {
						servoList[i].write(readData());
					}	
				}
				break;
			}
		case 97:
			setup();
			break;
		case 98:
			Serial.println("ready");
			break;
        case 99:
            break;
    }
}

void initializationLoop() {
	int ready = 0;
	//int ledCount = 0;
	//int ledOn = 0;
	Serial.println("ready");
	while (ready != 1) {
		/*
		if (ledCount >= 10240) {
			ledCount = 0;
			if (ledOn == 0)
			{
				ledOn = 1;
				pinMode(2, OUTPUT);
				digitalWrite(2, HIGH);
			}
			else 
			{
				ledOn = 0;
				pinMode(2, OUTPUT);
				digitalWrite(2, LOW);
			}
		}
		ledCount++;*/
		if (Serial.available() > 0) {
			if (Serial.parseInt() == 98) {
				ready = 1;
				pinMode(LED_BUILTIN, OUTPUT);
				digitalWrite(LED_BUILTIN, HIGH);
			}
		}
	}
}

int readData() {
    Serial.println("r");
    int data = -1;
    while(1) {
        if(Serial.available() > 0) {
			data = Serial.parseInt();
            return data;
        }
    }
}
