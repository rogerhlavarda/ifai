/*
  Mao Robotica com 5 dedos - sketch didatico alternativo.

  O programa Python deste projeto usa pyFirmata. Para isso, carregue no Arduino:
  Arquivo > Exemplos > Firmata > StandardFirmata

  Este arquivo fica como referencia para uma comunicacao serial simples no futuro.
  Ele recebe linhas como: polegar:150
*/

#include <Servo.h>

Servo servoPolegar;
Servo servoIndicador;
Servo servoMedio;
Servo servoAnelar;
Servo servoMinimo;

const int PINO_POLEGAR = 3;
const int PINO_INDICADOR = 5;
const int PINO_MEDIO = 9;
const int PINO_ANELAR = 10;
const int PINO_MINIMO = 11;

void setup() {
  Serial.begin(9600);

  servoPolegar.attach(PINO_POLEGAR);
  servoIndicador.attach(PINO_INDICADOR);
  servoMedio.attach(PINO_MEDIO);
  servoAnelar.attach(PINO_ANELAR);
  servoMinimo.attach(PINO_MINIMO);
}

void loop() {
  if (!Serial.available()) {
    return;
  }

  String comando = Serial.readStringUntil('\n');
  comando.trim();

  int separador = comando.indexOf(':');
  if (separador == -1) {
    return;
  }

  String dedo = comando.substring(0, separador);
  int angulo = comando.substring(separador + 1).toInt();
  angulo = constrain(angulo, 0, 180);

  moverDedo(dedo, angulo);
}

void moverDedo(String dedo, int angulo) {
  if (dedo == "polegar") {
    servoPolegar.write(angulo);
  } else if (dedo == "indicador") {
    servoIndicador.write(angulo);
  } else if (dedo == "medio") {
    servoMedio.write(angulo);
  } else if (dedo == "anelar") {
    servoAnelar.write(angulo);
  } else if (dedo == "minimo") {
    servoMinimo.write(angulo);
  }
}

