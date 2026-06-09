"""Comunicacao com o Arduino usando pyFirmata.

Este modulo e a ponte entre o Python e a parte fisica do projeto.
O Python decide se cada dedo esta aberto ou fechado; o Arduino recebe
angulos e move os servomotores ligados aos pinos configurados.
"""

from pyfirmata import Arduino, SERVO

from config import ARDUINO_PORT, SERVO_ANGLES, SERVO_PINS


class ArduinoController:
    """Controla os servos da mao robotica."""

    def __init__(self, port=ARDUINO_PORT):
        self.board = Arduino(port)
        self.last_states = {}

        for pin in SERVO_PINS.values():
            self.board.digital[pin].mode = SERVO

    def set_finger_state(self, finger_name, is_open):
        """Envia o angulo de um dedo apenas quando o estado muda."""
        if self.last_states.get(finger_name) == is_open:
            return

        angle_name = "aberto" if is_open else "fechado"
        angle = SERVO_ANGLES[finger_name][angle_name]
        pin = SERVO_PINS[finger_name]

        # Evitar comandos repetidos deixa a comunicacao mais estavel
        # e reduz movimentos desnecessarios nos servos.
        self.board.digital[pin].write(angle)
        self.last_states[finger_name] = is_open

    def set_hand_state(self, states):
        for finger_name, is_open in states.items():
            self.set_finger_state(finger_name, is_open)

    def close(self):
        self.board.exit()
