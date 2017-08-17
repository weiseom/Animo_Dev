/*
 제목    : 초음파센서로 거리 측정하기
 내용   : 초음파센서로부터 10cm 이내로 물체가 감지되었을때 LED가 켜지도록 만들어 봅시다.
 */

// 초음파센서의 송신부를 8번핀으로 설정합니다.
int trig = 2;
// 초음파센서의 수신부를 9번핀으로 설정합니다.
int echo = 3;
// LED를 A0핀으로 설정합니다.
int led = A0;

// 실행시 가장 먼저 호출되는 함수이며, 최초 1회만 실행됩니다.
// 변수를 선언하거나 초기화를 위한 코드를 포함합니다.
void setup() {
  // 초음파센서의 동작 상태를 확인하기 위하여 시리얼 통신을 설정합니다. (전송속도 9600bps)
  // 메뉴 Tool -> Serial Monitor 클릭
  Serial.begin(9600);
  // 초음파센서의 송신부로 연결된 핀을 OUTPUT으로 설정합니다.
  pinMode(trig, OUTPUT);
  // 초음파센서의 수신부로 연결된 핀을 INPUT으로 설정합니다.
  pinMode(echo, INPUT);
}

// setup() 함수가 호출된 이후, loop() 함수가 호출되며,
// 블록 안의 코드를 무한히 반복 실행됩니다.
void loop() {
  // 초음파 센서는 송신부와 수신부로 나뉘어 있으며,
  // 송신부터 수신까지의 시간을 기준으로 거리를 측정합니다.
  // 트리거로 연결된 핀이 송신부를 담당하며, 에코로 연결된 핀이 수신부를 담당합니다.
  // 송신부에서 2마이크로초 정도 또는 그 이상의 시간동안 초음파를 발생시킵니다.
  // 초음파 발생 전후로, 잡음을 제거하기 위하여 전류를 보내지 않도록 설정합니다.
  digitalWrite(trig, LOW);
  digitalWrite(echo, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(5);
  digitalWrite(trig, LOW);

  // 수신부의 초기 로직레벨을 HIGH로 설정하고, 반사된 초음파에 의하여 ROW 레벨로 바뀌기 전까지의 시간을 측정합니다.
  // 단위는 마이크로 초입니다.
  unsigned long duration = pulseIn(echo, HIGH);

  // 초음파의 속도는 초당 340미터를 이동하거나, 29마이크로초 당 1센치를 이동합니다.
  // 따라서, 초음파의 이동 거리 = duration(왕복에 걸린시간) / 29 / 2 입니다.
  float distance = duration / 29.0 / 2.0;

  // 측정된 거리 값를 시리얼 모니터에 출력합니다.
  Serial.print(distance);
  Serial.println("cm");

  // 측정된 거리가 10cm 이하라면, 아래의 블록을 실행합니다.
  if (distance < 10) {
    // LED가 연결된 핀의 로직레벨을 HIGH (5V)로 설정하여, LED가 켜지도록 합니다.
    //Serial.println("10cm 이하");
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(1000);                       // wait for a second
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    delay(1000);                       // wait for a second digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  }
  // 측정된 거리가 10cm 이상이라면, 아래의 블록을 실행합니다.
  else {
    // LED가 연결된 핀의 로직레벨을 LOW (0V)로 설정하여, LED가 꺼지도록 합니다.
    Serial.println("10cm 이상");
  }
  // 0.2초 동안 대기합니다.
  delay(100);
}
