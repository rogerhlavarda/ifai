"""Configuracoes principais do projeto.

Este arquivo centraliza os valores que costumam mudar no laboratorio:
porta do Arduino, pinos dos servos, angulos calibrados e webcam.

Manter tudo aqui evita que os alunos procurem configuracoes espalhadas
pelo projeto. Em aula, este costuma ser o primeiro arquivo a ajustar.
"""

# No Windows, a porta costuma ser COM3, COM4 etc.
# No Linux, normalmente aparece como /dev/ttyACM0 ou /dev/ttyUSB0.
ARDUINO_PORT = "COM3"

FINGER_NAMES = ["polegar", "indicador", "medio", "anelar", "minimo"]

# Cada dedo controla um servo porque a mao robotica precisa movimentar
# cada dedo de forma independente. Os pinos abaixo sao PWM no Arduino Uno.
SERVO_PINS = {
    "polegar": 3,
    "indicador": 5,
    "medio": 9,
    "anelar": 10,
    "minimo": 11,
}

# Os angulos variam conforme a montagem fisica da mao robotica.
# Por isso eles precisam ser calibrados antes do uso com estudantes.
# Calibre com cuidado para nao forcar os servos ou as pecas impressas.
SERVO_ANGLES = {
    "polegar": {"aberto": 20, "fechado": 150},
    "indicador": {"aberto": 20, "fechado": 150},
    "medio": {"aberto": 20, "fechado": 150},
    "anelar": {"aberto": 20, "fechado": 150},
    "minimo": {"aberto": 20, "fechado": 150},
}

CAMERA_INDEX = 0
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

# O MediaPipe Hands detecta pontos da mao chamados landmarks.
# Cada landmark tem coordenadas x, y e z normalizadas pela imagem.
MEDIAPIPE_MAX_HANDS = 1
MEDIAPIPE_DETECTION_CONFIDENCE = 0.7
MEDIAPIPE_TRACKING_CONFIDENCE = 0.7
