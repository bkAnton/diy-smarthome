int cols[2] = {12, 11};
int rows[2] = {10, 9};

int Button = 0;

void setup() {
    pinMode(cols[0], OUTPUT);
    pinMode(cols[1], OUTPUT);
    pinMode(rows[0], INPUT_PULLUP);
    pinMode(rows[1], INPUT_PULLUP);

    Serial.begin(9600);
    Serial.println(cols[0]);
}

void loop() {
  digitalWrite(cols[0], LOW);
  digitalWrite(cols[1], HIGH);

  if(digitalRead(rows[0]) == 0 && digitalRead(rows[1]) == 1)  {
    Button = 1;
    Serial.println(Button);
  } else if(digitalRead(rows[0]) == 1 && digitalRead(rows[1]) == 0) {
    Button = 2;
    Serial.println(Button);
  }

  digitalWrite(cols[0], HIGH);
  digitalWrite(cols[1], LOW);

    if(digitalRead(rows[0]) == 0 && digitalRead(rows[1]) == 1)  {
    Button = 3;
    Serial.println(Button);
  } else if(digitalRead(rows[0]) == 1 && digitalRead(rows[1]) == 0) {
    Button = 4;
    Serial.println(Button);
  }
}
