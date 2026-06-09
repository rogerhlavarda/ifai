"""Rastreamento da mao com MediaPipe.

Este modulo cuida apenas da visao computacional: recebe uma imagem da
webcam, pede ao MediaPipe para detectar a mao e devolve os landmarks.
Landmark e um ponto de referencia anatomico, como ponta de dedo ou junta.
"""

import cv2
import mediapipe as mp

from config import (
    MEDIAPIPE_DETECTION_CONFIDENCE,
    MEDIAPIPE_MAX_HANDS,
    MEDIAPIPE_TRACKING_CONFIDENCE,
)


class HandTracker:
    """Pequena classe para isolar o uso do MediaPipe Hands."""

    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.drawer = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            max_num_hands=MEDIAPIPE_MAX_HANDS,
            min_detection_confidence=MEDIAPIPE_DETECTION_CONFIDENCE,
            min_tracking_confidence=MEDIAPIPE_TRACKING_CONFIDENCE,
        )

    def process_frame(self, frame):
        """Processa um frame da webcam e retorna landmarks e lado da mao."""
        # OpenCV usa BGR, mas o MediaPipe espera RGB.
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb_frame)

        if not result.multi_hand_landmarks:
            return None, None

        hand_landmarks = result.multi_hand_landmarks[0]
        handedness = None

        if result.multi_handedness:
            handedness = result.multi_handedness[0].classification[0].label

        return hand_landmarks, handedness

    def draw_landmarks(self, frame, hand_landmarks):
        """Desenha os pontos e ligacoes da mao para facilitar a explicacao."""
        if hand_landmarks is None:
            return

        self.drawer.draw_landmarks(
            frame,
            hand_landmarks,
            self.mp_hands.HAND_CONNECTIONS,
        )

    def close(self):
        self.hands.close()
