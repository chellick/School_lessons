# Lessson

$$ 10001011_{2} = 1 * 2 ^{4} + 1 * 2 ^{1} + 1 * 2 ^{0} = -11_{10} $$


0001 0001

1110 1111

0111 1001

1000 0111

![img.png](img.png)

1011 1111 = 1011 1110 = 0100 0001 = -65
0001 1110 = 0001 1101 = 1110 0010 = 30
1011 0111 = 1011 0110 = 0100 1001 = -73


```
int trigPin = 12; 
int echoPin = 11;
int r = 0;
bool i = true;
bool q = false;


void setup() { 
    Serial.begin (9600); 
    //пины УЗ
    pinMode(trigPin, OUTPUT); 
    pinMode(echoPin, INPUT);

    // left motor
    pinMode(5, OUTPUT);
    pinMode(6, OUTPUT);
    
    // right motor
    pinMode(9, OUTPUT);
    pinMode(10, OUTPUT);
}

void forward(int timeDelay=100) {
    Serial.println("вперёд");
    delay(timeDelay);
    digitalWrite(5, 0);
    digitalWrite(6, 1);
    
    digitalWrite(9, 0);
    digitalWrite(10, 1);    
}


void stop(int timeDelay=100) {
    Serial.println("стоп");
    digitalWrite(5, 0);
    digitalWrite(6, 0);
    
    digitalWrite(9, 0);
    digitalWrite(10, 0);
    delay(timeDelay);
}

void right(int timeDelay=100) {
    Serial.println("вправо");
    digitalWrite(5, 1);
    digitalWrite(6, 0);
    
    digitalWrite(9, 0);
    digitalWrite(10, 1);
    delay(timeDelay);
}

int dist(int timeDelay=100)
{
  int duration, distance;
  // установить высокий уровень на пине Trig
  digitalWrite(trigPin, HIGH);
  // подождать 
  delay(timeDelay); 
  digitalWrite(trigPin, LOW); 
  // узнаем длительность высокого сигнала на пине Echo
  duration = pulseIn(echoPin, HIGH); 
  // вычисляем расстояние
  distance = duration * 0.034/2;
  Serial.println(distance);
  return (distance);
}

void loop() {    
    int d = dist(10);
    delay(30); // ОБЯЗАТЕЛЬНО!
    if ((d == 0) || (d > 50))
        forward(30);
    if ((d > 0) && (d < 50)){
        if (q == true)
            forward(60);
            q = false;
            Serial.println("дальше");
        stop(30);
        r = r + 1;
        if((r > 5) && (i == true)){
            right(225);
            stop(30);
            i = false;
            q = true;}
}
}
```
## Как вещественные числа хранятся в оператвиной памяти

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |


$$
a = 2^^b
$$