static constexpr uint8_t SwitchPin = 2;
static constexpr uint8_t XPin = 0;
static constexpr uint8_t YPin = 1;
static constexpr uint8_t B5KPin = 2;
// -------------------------------------------

void setup() 
{
	pinMode(SwitchPin, INPUT);
	digitalWrite(SwitchPin, HIGH);
	
	Serial.begin(9600);
}

void loop() 
{
	Serial.print(digitalRead(SwitchPin) == 0);
	Serial.print(":");
	Serial.print(analogRead(XPin));
	Serial.print(":");
	Serial.print(analogRead(YPin));
	Serial.print(":");
	Serial.print(analogRead(B5KPin));
	Serial.print(";");
}
