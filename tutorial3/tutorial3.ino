#define BAUD 9600

void setup() {
  Serial.begin(BAUD);
}

void loop() {
  char command = Serial.read();
  switch (command) {
    case 'f':
      break;
    case 'b':
      break;
    case 'l':
      break;
    case 'r':
      break;
    default:
      break;
  Serial.flush();
  }
}
