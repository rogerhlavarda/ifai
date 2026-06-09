"""Fluxo principal: webcam -> MediaPipe -> dedos -> Arduino -> servos.

Este arquivo foi escrito para ser lido em aula. Ele mostra a sequencia
principal do projeto sem esconder a logica em muitas camadas.
"""

import cv2

from arduino_controller import ArduinoController
from config import CAMERA_HEIGHT, CAMERA_INDEX, CAMERA_WIDTH, FINGER_NAMES
from finger_detector import detect_fingers
from hand_tracker import HandTracker


def open_camera():
    """Abre a webcam e aplica as configuracoes definidas em config.py."""
    camera = cv2.VideoCapture(CAMERA_INDEX)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)
    return camera


def write_finger_states(frame, states):
    """Escreve na imagem se cada dedo esta aberto ou fechado."""
    y = 30

    for finger_name in FINGER_NAMES:
        text = "Aberto" if states[finger_name] else "Fechado"
        label = f"{finger_name.capitalize()}: {text}"
        cv2.putText(
            frame,
            label,
            (10, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
        )
        y += 30


def should_exit():
    """Permite sair do programa com ESC ou Q."""
    key = cv2.waitKey(1) & 0xFF
    return key == 27 or key == ord("q")


def main():
    camera = open_camera()

    if not camera.isOpened():
        print("Erro: nao foi possivel abrir a webcam.")
        return

    tracker = HandTracker()
    arduino = None

    try:
        arduino = ArduinoController()
    except Exception as error:
        print("Erro: nao foi possivel conectar ao Arduino.")
        print(f"Detalhes: {error}")
        print("A imagem da webcam sera exibida, mas os servos nao serao movidos.")

    try:
        while True:
            success, frame = camera.read()

            if not success:
                print("Erro: nao foi possivel ler a imagem da webcam.")
                break

            hand_landmarks, handedness = tracker.process_frame(frame)
            states = detect_fingers(hand_landmarks, handedness)

            # Cada dedo detectado controla um servo correspondente no Arduino.
            if arduino is not None:
                arduino.set_hand_state(states)

            tracker.draw_landmarks(frame, hand_landmarks)
            write_finger_states(frame, states)

            cv2.imshow("Mao Robotica - IFAI", frame)

            if should_exit():
                break
    finally:
        camera.release()
        tracker.close()

        if arduino is not None:
            arduino.close()

        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
